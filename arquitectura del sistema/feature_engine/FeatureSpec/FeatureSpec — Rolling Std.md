**FeatureSpec — Rolling Std**

**Identidad**

* **name**: rolling\_std\_{window} (ej. rolling\_std\_20)
* **version**: 1.0
* **category**: TECHNICAL
* **module**: feature\_engine.primitives.rolling.RollingStd

Desviación estándar móvil (muestral, ddof=1) sobre una ventana de **window** barras. Proxy directo de volatilidad realizada en la escala del timeframe configurado.

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
* **Restricción**: window ≥ 2 (se necesitan al menos dos observaciones para calcular la desviación muestral).
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
| window | int | — | Tamaño de la ventana (≥ 2) |
| column | str | "close" | Columna del DataFrame sobre la que se calcula |
| timeframe | Timeframe | "1d" | Resolución temporal |

**Cálculo**

```python
df[column].rolling(window).std(ddof=1)
```

**Output**

* **output\_type**: float
* **output\_column**: rolling\_std\_{window}@1.0 (ej. rolling\_std\_20@1.0)
* Una feature, una columna, una semántica.
