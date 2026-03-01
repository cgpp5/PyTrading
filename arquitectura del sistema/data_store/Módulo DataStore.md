# Módulo: data_store (Capa de Persistencia Transversal)

## Posición en la arquitectura

data_store es un módulo **transversal** que se interpone entre productores (market_feed, feature_engine) y consumidores (strategy_logic, trading_ui). No pertenece a ningún flujo vertical: cualquier módulo puede escribir y cualquier módulo puede leer.

## Objetivo operativo

Actuar como **Única Fuente de la Verdad (SSOT) en disco**. Desacopla temporal y espacialmente el cálculo de la ejecución y la visualización. El sistema puede apagarse, reiniciarse o perder energía sin que se pierda una sola vela, indicador o estado de estrategia, manteniendo una huella de RAM cercana a 0 MB.

---

## Principios de diseño

### 1. Idempotencia absoluta (UPSERT)

Escribir la vela de las 15:00h diez veces seguidas produce exactamente una fila. La clave primaria compuesta `(symbol, timeframe, timestamp)` resuelve colisiones silenciosamente mediante `INSERT OR REPLACE`.

### 2. Esquema Híbrido (Rígido + Dinámico)

Las columnas vitales (OHLCV, metadatos de calidad) usan tipos estrictos e indexados en la tabla. Los cálculos mutables del FeatureEngine se empaquetan en una columna `JSON` versionada. Añadir un nuevo indicador no requiere migración de esquema.

### 3. Store sin lógica (Dumb Store)

data_store **no calcula, no limpia y no interpreta**. Recibe datos y los persiste fielmente. La única validación que realiza es **estructural** sobre el JSON de features (ver sección Validación). No importa tipos de feature_engine ni de market_feed.

### 4. Concurrencia WAL

SQLite en modo Write-Ahead Logging permite lecturas concurrentes mientras se ejecuta una escritura, sin bloqueos de disco.

---

## Esquema de base de datos

### Tabla `market_data`

Histórico canónico de velas OHLCV con columnas de control de market_feed.

```sql
CREATE TABLE IF NOT EXISTS market_data (
    symbol      TEXT NOT NULL,
    timeframe   TEXT NOT NULL,
    timestamp   TEXT NOT NULL,
    open        REAL,
    high        REAL,
    low         REAL,
    close       REAL,
    volume      REAL,
    source      TEXT,
    quality     TEXT,
    is_gap      INTEGER DEFAULT 0,
    latency_sec REAL,
    features    JSON,
    PRIMARY KEY (symbol, timeframe, timestamp)
);
```

**Decisiones clave:**

| Columna | Decisión | Justificación |
|---------|----------|---------------|
| `volume` | `REAL`, no `INTEGER` | market_feed normaliza todo a `float64`. INTEGER no soporta NaN (filas de gap) ni volúmenes fraccionarios |
| `latency_sec` | Incluida | Forma parte del esquema canónico de market_feed (`CONTROL_COLS = [source, quality, is_gap, latency_sec]`). Omitirla pierde contexto operativo |
| `timestamp` | `TEXT` ISO 8601 UTC | Representación única, sin duplicar con epoch. Formato canónico: `2026-03-01T15:00:00+00:00`. A la escala del sistema (~250k filas/año) la diferencia TEXT vs INTEGER es despreciable; se gana legibilidad directa en cualquier SQLite browser |
| `is_gap` | `INTEGER` (0/1) | SQLite no tiene BOOLEAN nativo. El repo layer convierte explícitamente `bool ↔ int` |
| Índice explícito | No se crea | La PRIMARY KEY ya genera un índice implícito sobre `(symbol, timeframe, timestamp)`. Un INDEX redundante ocupa espacio sin beneficio |

### Tabla `market_requests`

Persiste `MarketDataMeta` — la metadata a nivel de request que `MarketData.df` no contiene.

```sql
CREATE TABLE IF NOT EXISTS market_requests (
    symbol          TEXT NOT NULL,
    timeframe       TEXT NOT NULL,
    requested_at    TEXT NOT NULL,
    provider_used   TEXT NOT NULL,
    fallback_used   INTEGER DEFAULT 0,
    start_ts        TEXT NOT NULL,
    end_ts          TEXT NOT NULL,
    coverage_ratio  REAL,
    gap_count       INTEGER,
    quality         TEXT,
    notes           TEXT,
    PRIMARY KEY (symbol, timeframe, requested_at)
);
```

**Justificación:** `MarketData` es un par `(df, meta)`. Sin esta tabla, la metadata (`provider_used`, `fallback_used`, `coverage_ratio`) se pierde al apagar el sistema. La SSOT queda incompleta.

### Tabla `system_state`

Memoria transversal para TradeStateMachine: cooldowns, flags, multiplicadores.

```sql
CREATE TABLE IF NOT EXISTS system_state (
    key        TEXT PRIMARY KEY,
    value      JSON NOT NULL,
    updated_at TEXT NOT NULL
);
```

---

## Validación del JSON de features

data_store valida **estructura**, no **semántica**. No importa nada de feature_engine.

Antes de escribir, cada entrada del JSON debe cumplir:

1. La clave contiene `@` (formato `nombre@versión`, e.g. `returns@1.0`).
2. El valor es un dict con exactamente las claves `value` y `quality`.
3. `value` es `float`, `int` o `null`.
4. `quality` ∈ `{"ready", "warmup", "degraded", "missing"}`.

Si cualquier entrada falla → se rechaza **todo el JSON** antes de escribir.

**Sobre el set de quality values:** Se declara como constante local en data_store:

```python
_VALID_QUALITIES = {"ready", "warmup", "degraded", "missing"}
```

No se importa de `feature_engine.feature_spec.quality`. Si `FeatureQuality` evoluciona, se actualiza manualmente en ambos sitios — coste mínimo frente al acoplamiento que se evita.

---

## Conversiones de tipo (repo layer)

| Pandas (`MarketData.df`)   | SQLite (`market_data`)   | Lectura → Pandas                |
|:---------------------------|:-------------------------|:--------------------------------|
| `float64` (OHLCV)          | `REAL`                   | `float64`                       |
| `bool` (is_gap)            | `INTEGER` (0/1)          | `.astype(bool)` explícito       |
| `float64` (latency_sec)    | `REAL`                   | `float64`                       |
| `str` (source, quality)    | `TEXT`                   | `str`                           |
| `DatetimeIndex[ns, UTC]`   | `TEXT` ISO 8601          | `pd.to_datetime(..., utc=True)` |

---

## Ciclo de vida de conexiones

```python
def get_connection(self) -> sqlite3.Connection:
    conn = sqlite3.connect(self.db_path, timeout=10.0)
    conn.row_factory = sqlite3.Row
    # PRAGMAs per-connection (no se heredan entre conexiones)
    conn.execute("PRAGMA journal_mode=WAL")
    conn.execute("PRAGMA synchronous=NORMAL")
    conn.execute("PRAGMA temp_store=MEMORY")
    return conn
```

`journal_mode=WAL` es per-database y persiste, pero se reafirma por seguridad. `synchronous` y `temp_store` son **per-connection** y DEBEN configurarse en cada `get_connection()`, no solo en `__init__`.

El caller es responsable de cerrar la conexión. Patrón recomendado:

```python
conn = core.get_connection()
try:
    # ... operaciones ...
    conn.commit()
finally:
    conn.close()
```

---

## Dirección de dependencias

```
market_feed    ──→ data_store    (escribe MarketData)
feature_engine ──→ data_store    (escribe FeatureValues en JSON)
strategy_logic ──→ data_store    (lee features, escribe estado)
trading_ui     ──→ data_store    (lee todo)

data_store     ──→ (nada)        (no importa de módulos de dominio)
```

market_repo acepta `pd.DataFrame` y parámetros primitivos (`str`, `float`, `dict`), no tipos de dominio como `MarketData` o `FeatureSpec`. La conversión `MarketData → parámetros` ocurre en el **caller** (orquestador o módulo productor).

---

## Estructura de archivos

```
data_store/
├── __init__.py          Exporta la fachada pública
├── core.py              Motor SQLite: conexión, PRAGMAs, DDL de esquema
├── market_repo.py       CRUD market_data + market_requests, JSON pack/unpack
└── state_repo.py        CRUD system_state (key-value)
```

---

## Trade-off: JSON embebido vs tabla normalizada de features

**Decisión actual:** JSON embebido en la columna `features` de `market_data`.

**Ventajas:**

- Una sola escritura por vela (OHLCV + todas las features juntas).
- No requiere JOINs para reconstruir el DataFrame completo.
- Añadir features no modifica el esquema.

**Coste conocido:**

- Actualizar **una sola feature** requiere read-modify-write del JSON completo.
- Aceptable porque el patrón predominante es batch: FeatureEngine calcula todas las features de una barra de golpe.

**Escape hatch:** Si feature updates individuales se convierten en cuello de botella → migrar a tabla `feature_values(symbol, timeframe, timestamp, feature_key, value, quality)` con UPSERTs atómicos. El contrato de serialización (keys del JSON) se mapea directamente a la columna `feature_key`.
