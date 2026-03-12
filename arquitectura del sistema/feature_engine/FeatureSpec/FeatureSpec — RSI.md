**FeatureSpec — RSI (Relative Strength Index)**

**Identidad**

* **name**: rsi\_{period} (ej. rsi\_14)
* **version**: 1.0
* **category**: TECHNICAL
* **module**: feature\_engine.primitives.rsi.RSI

Oscilador de momentum acotado entre 0 y 100 que mide la magnitud relativa de ganancias recientes frente a pérdidas. Utiliza el suavizado exponencial de Wilder ($\alpha = 1/period$). Valores por encima de 70 se interpretan convencionalmente como sobrecompra; por debajo de 30, como sobreventa.

**Semántica temporal**

**Frecuencia base**
* **timeframe**: configurable (default 1d)

**Disponibilidad**
* **availability**: AT\_CLOSE
* El valor del bar **t** existe a partir del cierre de **t**.

**Política de alineación**
* **alignment**: NONE
* No se proyecta a otros timeframes.

**Política de interpolación**
* **interpolation**: None (no aplica a features TECHNICAL por restricción del contrato)
* Al ser un oscilador acotado, interpolar valores entre barras carece de significado estadístico.

**Lookback y madurez**

* **lookback\_required**: period
* **warmup\_policy**: FIXED\_LOOKBACK
* Los primeros **period** barras producen NaN (se necesitan **period** deltas para la media inicial de ganancias/pérdidas).
* **degrades\_on\_alignment**: False

**Calidad del dato**

Estados posibles:

* READY — ventana completa de cierres consecutivos válidos.
* WARMUP — barras insuficientes para completar la ventana inicial.
* DEGRADED — datos subyacentes degradados o con gaps dentro de la ventana.
* MISSING — dato de cierre no disponible.

**Dependencias**

* **depends\_on**: ninguna feature.
* **external\_sources**: ninguna.
* Requiere la columna indicada por `column` (default `close`) en el DataFrame OHLCV.

**Parámetros**

| Parámetro | Tipo | Default | Descripción |
|-----------|------|---------|-------------|
| period | int | 14 | Período del RSI (≥ 1) |
| column | str | "close" | Columna del DataFrame sobre la que se calcula |
| timeframe | Timeframe | "1d" | Resolución temporal |

**Cálculo**

Método de Wilder (suavizado exponencial con $\alpha = 1/period$):

```python
delta = df[column].diff()
gain  = delta.where(delta > 0, 0.0)
loss  = (-delta).where(delta < 0, 0.0)

avg_gain = gain.ewm(alpha=1/period, min_periods=period, adjust=False).mean()
avg_loss = loss.ewm(alpha=1/period, min_periods=period, adjust=False).mean()

rs  = avg_gain / avg_loss
rsi = 100 - (100 / (1 + rs))
```

$$RSI_t = 100 - \frac{100}{1 + RS_t}, \quad RS_t = \frac{\overline{Gain}_t}{\overline{Loss}_t}$$

Donde las medias se actualizan recursivamente:

$$\overline{Gain}_t = \frac{(period - 1) \cdot \overline{Gain}_{t-1} + Gain_t}{period}$$

**Output**

* **output\_type**: float (rango [0, 100])
* **output\_column**: rsi\_{period}@1.0 (ej. rsi\_14@1.0)
* Una feature, una columna, una semántica.
