**FeatureSpec — Volume ZScore**

**Identidad**

* **name**: volume\_zscore\_{window} (ej. volume\_zscore\_20)
* **version**: 1.0
* **category**: TECHNICAL
* **module**: feature\_engine.primitives.volume.VolumeZScore

Z-score del volumen respecto a su media y desviación móvil sobre **window** barras. Detecta barras de volumen anómalo (> 2σ o < −2σ) de forma normalizada e independiente de la escala absoluta del activo.

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
* **Restricción**: window ≥ 2 (se necesitan al menos dos observaciones para calcular la desviación).
* Los primeros **window − 1** barras producen NaN.

**Calidad del dato**

Estados posibles:

* READY — ventana completa de volumen válido.
* WARMUP — barras insuficientes para completar la ventana.
* DEGRADED — datos subyacentes degradados o con gaps dentro de la ventana.
* MISSING — dato de volumen no disponible.

**Dependencias**

* **depends\_on**: ninguna feature.
* **external\_sources**: ninguna.
* Requiere columna `volume` en el DataFrame OHLCV.

**Parámetros**

| Parámetro | Tipo | Default | Descripción |
|-----------|------|---------|-------------|
| window | int | 20 | Tamaño de la ventana (≥ 2) |
| timeframe | Timeframe | "1d" | Resolución temporal |

**Cálculo**

```python
rolling_mean = df["volume"].rolling(window).mean()
rolling_std  = df["volume"].rolling(window).std(ddof=1)
zscore = (df["volume"] - rolling_mean) / rolling_std
```

$$z_t = \frac{V_t - \bar{V}_{t,w}}{\sigma_{t,w}}$$

**Output**

* **output\_type**: float
* **output\_column**: volume\_zscore\_{window}@1.0 (ej. volume\_zscore\_20@1.0)
* Una feature, una columna, una semántica.
