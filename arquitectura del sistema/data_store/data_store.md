# data_store — Plan de desarrollo

## Visión general

4 pasos incrementales. Cada paso produce código funcional con tests que validan el contrato antes de avanzar. Los tests usan `:memory:` como base de datos para evitar efectos secundarios en disco.

---

## Paso 0 — Fundaciones y conexión (`core.py`)

**Objetivo:** Conexión a SQLite con optimizaciones de concurrencia. Creación del esquema completo (3 tablas: `market_data`, `market_requests`, `system_state`).

**Implementación:**

- `DataStoreCore.__init__(db_path)` → crea el fichero de base de datos si no existe.
- `get_connection()` → devuelve `sqlite3.Connection` con PRAGMAs configurados **en cada llamada** (`journal_mode=WAL`, `synchronous=NORMAL`, `temp_store=MEMORY`).
- DDL: las 3 tablas definidas en el Módulo DataStore.md, sin índices redundantes.

**Test (`data_store/tests/test_core.py`):**

1. Instanciar con `:memory:`.
2. Verificar que las 3 tablas (`market_data`, `market_requests`, `system_state`) existen en `sqlite_master`.
3. Verificar que `PRAGMA journal_mode` devuelve `wal`.
4. Abrir una segunda conexión con `get_connection()` y verificar que `PRAGMA synchronous` devuelve `1` (NORMAL) — confirma que los PRAGMAs per-connection se aplican siempre, no solo en init.

---

## Paso 1 — Repositorio de mercado: UPSERT y OHLCV (`market_repo.py`)

**Objetivo:** Guardar y recuperar DataFrames OHLCV manteniendo tipos, índice UTC y columnas de control. Idempotencia validada. Persistencia de MarketDataMeta.

**Implementación:**

- `save_market_data(conn, symbol, timeframe, df)` → INSERT OR REPLACE por fila.
  - Conversión `is_gap: bool → int` al escribir.
  - Conversión `DatetimeIndex → ISO 8601 TEXT` al escribir.
  - La columna `features` se deja `NULL` en este paso.
- `load_market_data(conn, symbol, timeframe, start=None, end=None)` → DataFrame canónico.
  - Reconstrucción: `int → bool` para `is_gap`, `TEXT → DatetimeIndex[ns, UTC]`.
  - Si no hay filas, retorna DataFrame vacío con schema correcto.
- `save_request_meta(conn, symbol, timeframe, meta_dict)` → INSERT OR REPLACE en `market_requests`.
- `load_request_meta(conn, symbol, timeframe)` → dict más reciente o None.

**Test (`data_store/tests/test_market_repo.py`):**

1. Guardar 3 velas de SPY/1d con `source="yfinance"`, `quality="normal"`, `is_gap=False`, `latency_sec=0.42`.
2. Cargar y verificar: 3 filas, tipos correctos (`float64` para OHLCV, `bool` para is_gap, `float64` para latency_sec, `DatetimeIndex[ns, UTC]`).
3. Modificar el volumen de la vela 2 en Python. Volver a guardar las 3 velas.
4. Cargar y verificar: sigue habiendo exactamente 3 filas y el volumen de la vela 2 se actualizó (idempotencia).
5. Guardar una vela con `is_gap=True` y `latency_sec=NaN`. Cargar y verificar que `is_gap` es `True` (bool, no int) y `latency_sec` es `NaN`.
6. Guardar metadata de request (`provider_used`, `fallback_used`, `coverage_ratio`, `gap_count`, `quality`, `notes`). Cargar y verificar todos los campos.

---

## Paso 2 — Contrato JSON de features (`market_repo.py`)

**Objetivo:** Permitir que FeatureEngine inyecte features empaquetadas bajo el contrato FeatureValue. Validación estructural antes de escribir. Desempaquetado al leer.

**Implementación:**

- `save_features(conn, symbol, timeframe, timestamp, features_dict)`:
  - Valida estructura: clave tiene `@`, valor tiene `value` + `quality`, quality ∈ `_VALID_QUALITIES`.
  - Si falla → `ValueError` antes de tocar la DB.
  - Serializa a JSON string, actualiza la columna `features` de la fila existente.
- Extensión de `load_market_data`: deserializa el JSON y expone columnas `{feature_key}` con los values. Las filas sin features devuelven NaN en esas columnas.

**Constante local (no importada de feature_engine):**

```python
_VALID_QUALITIES = {"ready", "warmup", "degraded", "missing"}
```

**Test (`data_store/tests/test_features_json.py`):**

1. Guardar 3 velas. Inyectar features en la vela 2: `{"returns@1.0": {"value": 0.0023, "quality": "ready"}, "sma_50@1.0": {"value": 398.1, "quality": "warmup"}}`.
2. Cargar el DataFrame. Verificar que las columnas `returns@1.0` y `sma_50@1.0` existen con los valores correctos.
3. Verificar que las filas sin features (vela 1 y 3) tienen NaN en esas columnas.
4. Intentar guardar con clave sin `@` → `ValueError`.
5. Intentar guardar con quality `"COMPUTED"` → `ValueError`.
6. Intentar guardar sin campo `quality` → `ValueError`.
7. Guardar una feature con `"value": null, "quality": "missing"` → se acepta sin error. Al cargar, la columna tiene NaN para esa fila.

---

## Paso 3 — Repositorio de estado (`state_repo.py`)

**Objetivo:** Memoria persistente transversal. KV store para variables de sistema.

**Implementación:**

- `save_state(conn, key, value)` → INSERT OR REPLACE con `updated_at` automático (ISO 8601 UTC).
- `load_state(conn, key)` → valor deserializado (dict/list/scalar) o None si no existe.
- `delete_state(conn, key)` → elimina la entrada.
- `list_keys(conn)` → lista de claves existentes.

**Test (`data_store/tests/test_state_repo.py`):**

1. Guardar `"cb_active"` → `{"active": true, "since": "2026-03-01T10:00:00+00:00"}`.
2. Recuperar y verificar el dict completo.
3. Actualizar `"cb_active"` → `{"active": false, "since": "2026-03-01T14:00:00+00:00"}`. Verificar que hay 1 fila (no 2) y el valor cambió.
4. Guardar `"dca_multiplier"` → `{"value": 1.5}`. Listar keys. Verificar 2 keys.
5. Eliminar `"cb_active"`. Verificar que `load_state("cb_active")` devuelve None. `list_keys` devuelve 1 key.
