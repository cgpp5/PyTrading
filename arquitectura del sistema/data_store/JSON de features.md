# JSON de features — Contrato de serialización

## Formato canónico

Cada feature se serializa como una entrada independiente en el campo `features` de la tabla `market_data`:

```json
{
  "returns@1.0":    {"value": 0.0023,  "quality": "ready"},
  "sma_50@1.0":     {"value": 398.1,   "quality": "warmup"},
  "true_range@1.0": {"value": 2.34,    "quality": "ready"},
  "rsi_14@1.0":     {"value": null,    "quality": "missing"},
  "mcclellan_oscillator": {"value": -12.5, "quality": "ready"}
}
```

## Invariantes

1. **Clave:** identificador simple o `nombre@versión` (e.g. `returns@1.0`, `mcclellan_oscillator`). Sin prefijo `v`.
2. **value:** escalar (`float`, `int`) o `null` (para features no calculadas).
3. **quality:** obligatorio. Valor del enum `FeatureQuality`: `ready` | `warmup` | `degraded` | `missing`.
4. **Sin campos adicionales.** No hay `is_stale` ni metadatos extra. La calidad se expresa exclusivamente a través de `quality`.
5. **Sin estructuras anidadas.** Cada entrada es plana: `{"value": ..., "quality": "..."}`.
6. **Scalar-per-feature.** Cada clave representa exactamente una serie numérica. Un indicador visual multi-linea debe agruparse por encima de esta capa.

## Correspondencia con el código existente

| Aspecto | Valor correcto | Fuente de verdad |
|---------|----------------|-------------------|
| Formato de versión | `1.0` (sin prefijo `v`) cuando la clave va versionada | `FeatureSpec.version` |
| Valores de quality | `ready`, `warmup`, `degraded`, `missing` | `FeatureQuality` enum en `feature_engine/feature_spec/quality.py` |
| Nombre de feature | snake_case, descriptivo | `FeatureSpec.name` |

## Responsabilidades por capa

| Capa | Rol |
|------|-----|
| **feature_engine** | Produce `{"value": ..., "quality": "..."}` por feature. Conoce `FeatureSpec`. Decide `quality`. |
| **data_store** | Valida estructura mínima (clave simple o con `@version`, dict con `value` + `quality`, quality ∈ set cerrado). Persiste y reconstruye fielmente. **No interpreta.** |
| **Consumidores** (strategy_logic, trading_ui) | Leen el DataFrame reconstruido. Si necesitan un indicador compuesto, lo agrupan por encima de estas claves escalares. |

## Casos especiales implementados

### Features externas simples

Las series externas McClellan se guardan con clave simple:

```json
{
  "mcclellan_oscillator": {"value": -12.5, "quality": "ready"},
  "mcclellan_summation": {"value": 1023.4, "quality": "ready"}
}
```

Se eligio este formato para evitar sobrecargar una serie manual respaldada por CSV con semantica de versionado en la clave persistida.

### Indicadores visuales multi-linea

Bollinger Bands se persiste como tres features escalares independientes:

- `bollinger_middle_20@1.0`
- `bollinger_upper_20_2@1.0`
- `bollinger_lower_20_2@1.0`

La agrupacion como un unico indicador visual ocurre en TradingUI, no en DataStore.
