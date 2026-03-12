**FeatureSpec — True Range**

**Identidad**

* **name**: true\_range
* **version**: 1.0
* **category**: TECHNICAL
* **module**: feature\_engine.primitives.volatility.TrueRange

True Range de Wilder: la mayor de tres distancias que capturan tanto el rango intrabar como los gaps respecto al cierre anterior. Base para ATR y otros indicadores de volatilidad.

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
* El primer bar siempre produce NaN (necesita el cierre anterior).

**Calidad del dato**

Estados posibles:

* READY — high, low y close actuales + close anterior disponibles.
* WARMUP — primer bar de la serie (lookback insuficiente).
* DEGRADED — datos subyacentes degradados o con gaps.
* MISSING — columna high, low o close no disponible.

**Dependencias**

* **depends\_on**: ninguna feature.
* **external\_sources**: ninguna.
* Requiere columnas `high`, `low` y `close` en el DataFrame OHLCV.

**Parámetros**

| Parámetro | Tipo | Default | Descripción |
|-----------|------|---------|-------------|
| timeframe | Timeframe | "1d" | Resolución temporal |

**Cálculo**

```python
prev_close = df["close"].shift(1)
tr = pd.concat([
    df["high"] - df["low"],
    (df["high"] - prev_close).abs(),
    (df["low"]  - prev_close).abs(),
], axis=1).max(axis=1)
```

$$TR_t = \max\bigl(H_t - L_t,\; |H_t - C_{t-1}|,\; |L_t - C_{t-1}|\bigr)$$

**Output**

* **output\_type**: float
* **output\_column**: true\_range@1.0
* Una feature, una columna, una semántica.
