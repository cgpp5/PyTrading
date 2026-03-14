**FeatureSpec — SMA Osc (Distance to SMA)**

**Estado**

Implementado en Fase 4.

Vive en `feature_engine.composition.sma_osc`.

**Identidad**

* **name**: `sma_osc_{period}`
* **version**: 1.0
* **category**: DERIVED
* **module**: `feature_engine.composition.sma_osc`

SMA Osc representa la distancia porcentual del precio de cierre respecto de su SMA de periodo configurable.

**Semántica temporal**

**Frecuencia base**
* **timeframe**: configurable (default `1d`)

**Disponibilidad**
* **availability**: AT_CLOSE
* El valor del bar `t` existe al cierre del propio bar `t`.

**Política de alineación**
* **alignment**: NONE
* No se proyecta fuera de su timeframe base.

**Lookback y madurez**

* **lookback_required**: `period`
* **warmup_policy**: FIXED_LOOKBACK

**Dependencias**

* **depends_on**: `sma_{period}`

La implementacion actual queda fija a `close` como serie fuente, igual que la familia de Bollinger actual.

**Parámetros soportados**

| Parámetro | Tipo | Default | Descripción |
|-----------|------|---------|-------------|
| period | int | 20 | Periodo de la SMA base |
| timeframe | Timeframe | "1d" | Resolución temporal |

**Cálculo**

```text
sma_osc = ((close - sma(close, period)) / sma(close, period)) * 100
```

**Persistencia**

Se persiste como feature escalar:

* `sma_osc_<period>@1.0`

**Presentación en TradingUI**

Presentacion actual:

* indicador escalar simple
* panel separado
* una sola linea visual

**Notas de implementación**

* Devuelve `NaN` cuando la SMA base vale cero para evitar divisiones invalidas.
* Puede validarse y ejecutarse por el registry formal y el DAG de composicion existentes.