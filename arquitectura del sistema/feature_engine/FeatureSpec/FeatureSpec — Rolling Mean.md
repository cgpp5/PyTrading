**FeatureSpec — Rolling Mean (SMA)**

**Identidad**

* **name**: sma\_{window} (ej. sma\_50)
* **version**: 1.0
* **category**: TECHNICAL
* **module**: feature\_engine.primitives.rolling.RollingMean

Media móvil simple sobre una ventana de **window** barras. Nombre dinámico: el parámetro `window` se incorpora al nombre de la feature.

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

* **lookback\_required**: window
* **warmup\_policy**: FIXED\_LOOKBACK
* Los primeros **window − 1** barras producen NaN.

**Calidad del dato**

Estados posibles:

* READY — ventana completa de datos válidos.
* WARMUP — barras insuficientes para completar la ventana.
* DEGRADED — datos subyacentes degradados o con gaps dentro de la ventana.
* MISSING — dato de la columna fuente no disponible.

**Dependencias**

* **depends\_on**: ninguna feature.
* **external\_sources**: ninguna.
* Requiere la columna indicada por `column` (default `close`) en el DataFrame OHLCV.

**Parámetros**

| Parámetro | Tipo | Default | Descripción |
|-----------|------|---------|-------------|
| window | int | — | Tamaño de la ventana (≥ 1) |
| column | str | "close" | Columna del DataFrame sobre la que se calcula |
| timeframe | Timeframe | "1d" | Resolución temporal |

**Cálculo**

```python
df[column].rolling(window).mean()
```

**Output**

* **output\_type**: float
* **output\_column**: sma\_{window}@1.0 (ej. sma\_50@1.0)
* Una feature, una columna, una semántica.
