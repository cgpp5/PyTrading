**FeatureSpec — Simple Returns**

**Identidad**

* **name**: returns
* **version**: 1.0
* **category**: TECHNICAL
* **module**: feature\_engine.primitives.returns.SimpleReturns

Retorno bar-a-bar del precio de cierre: $(close_t - close_{t-1}) / close_{t-1}$.

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
* El primer bar siempre produce NaN (no hay bar previo).

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
df["close"].pct_change(fill_method=None)
```

**Output**

* **output\_type**: float
* **output\_column**: returns@1.0
* Una feature, una columna, una semántica.
