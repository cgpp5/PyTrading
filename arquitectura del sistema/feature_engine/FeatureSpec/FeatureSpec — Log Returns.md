**FeatureSpec — Log Returns**

**Identidad**

* **name**: log\_returns
* **version**: 1.0
* **category**: TECHNICAL
* **module**: feature\_engine.primitives.returns.LogReturns

Retorno logarítmico bar-a-bar: $\ln(close_t / close_{t-1})$.

Preferido sobre Simple Returns para análisis estadístico por su propiedad de aditividad temporal: la suma de log-returns sobre N periodos equivale al log-return total.

**Semántica temporal**

**Frecuencia base**
* **timeframe**: configurable (default 1d)

**Disponibilidad**
* **availability**: AT\_CLOSE
* El valor del bar **t** existe a partir del cierre de **t**.

**Política de alineación**
* **alignment**: NONE
* No se proyecta a otros timeframes.

**Lookback y madurez**

* **lookback\_required**: 1
* **warmup\_policy**: FIXED\_LOOKBACK
* El primer bar siempre produce NaN.

**Calidad del dato**

Estados posibles:

* READY — valor calculado a partir de dos cierres consecutivos válidos.
* WARMUP — primer bar de la serie (lookback insuficiente).
* DEGRADED — datos subyacentes degradados o con gaps.
* MISSING — dato de cierre no disponible.

**Dependencias**

* **depends\_on**: ninguna feature.
* **external\_sources**: ninguna.
* Requiere columna `close` en el DataFrame OHLCV.

**Parámetros**

| Parámetro | Tipo | Default | Descripción |
|-----------|------|---------|-------------|
| timeframe | Timeframe | "1d" | Resolución temporal |

**Cálculo**

```python
np.log(df["close"] / df["close"].shift(1))
```

**Output**

* **output\_type**: float
* **output\_column**: log\_returns@1.0
* Una feature, una columna, una semántica.
