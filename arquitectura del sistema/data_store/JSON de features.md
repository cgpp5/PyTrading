# JSON de features — Contrato de serialización

## Formato canónico

Cada feature se serializa como una entrada independiente en el campo `features` de la tabla `market_data`:

```json
{
  "returns@1.0":    {"value": 0.0023,  "quality": "ready"},
  "sma_50@1.0":     {"value": 398.1,   "quality": "warmup"},
  "true_range@1.0": {"value": 2.34,    "quality": "ready"},
  "rsi_14@1.0":     {"value": null,    "quality": "missing"}
}
```

## Invariantes

1. **Clave:** siempre `nombre@versión` (e.g. `returns@1.0`). Sin prefijo `v`.
2. **value:** escalar (`float`, `int`) o `null` (para features no calculadas).
3. **quality:** obligatorio. Valor del enum `FeatureQuality`: `ready` | `warmup` | `degraded` | `missing`.
4. **Sin campos adicionales.** No hay `is_stale` ni metadatos extra. La calidad se expresa exclusivamente a través de `quality`.
5. **Sin estructuras anidadas.** Cada entrada es plana: `{"value": ..., "quality": "..."}`.

## Correspondencia con el código existente

| Aspecto | Valor correcto | Fuente de verdad |
|---------|----------------|-------------------|
| Formato de versión | `1.0` (sin prefijo `v`) | `FeatureSpec.version` en primitivas existentes |
| Valores de quality | `ready`, `warmup`, `degraded`, `missing` | `FeatureQuality` enum en `feature_engine/feature_spec/quality.py` |
| Nombre de feature | snake_case, descriptivo | `FeatureSpec.name` |

## Responsabilidades por capa

| Capa | Rol |
|------|-----|
| **feature_engine** | Produce `{"value": ..., "quality": "..."}` por feature. Conoce `FeatureSpec`. Decide `quality`. |
| **data_store** | Valida estructura mínima (clave con `@`, dict con `value` + `quality`, quality ∈ set cerrado). Persiste y reconstruye fielmente. **No interpreta.** |
| **Consumidores** (strategy_logic, trading_ui) | Leen el DataFrame reconstruido. Filtran por quality según sus necesidades (e.g. solo `ready`, reaccionar a `degraded`). |
