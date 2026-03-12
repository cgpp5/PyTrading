**FeatureSpec — ATR (Average True Range)**

**Estado**

Implementado en Fase 4.

La base primitiva `true_range@1.0` sigue existiendo y ATR ya vive como feature derivada formal en `feature_engine.composition.atr`.

**Identidad**

* **name**: `atr_{period}`
* **version**: 1.0
* **category**: DERIVED
* **module**: `feature_engine.composition.atr`

ATR es una medida de volatilidad suavizada a partir de True Range. Su objetivo es capturar el rango efectivo medio reciente incluyendo gaps, sin depender de la direccion del precio.

**Semántica temporal**

**Frecuencia base**
* **timeframe**: configurable (default `1d`)

**Disponibilidad**
* **availability**: AT_CLOSE
* El valor del bar `t` existe a partir del cierre de `t`.

**Política de alineación**
* **alignment**: NONE
* No se proyecta fuera de su timeframe base.

**Lookback y madurez**

* **lookback_required**: `period`
* **warmup_policy**: FIXED_LOOKBACK
* Los primeros `period - 1` bars no deben considerarse maduros.

**Calidad del dato**

Estados actuales esperados:

* READY — True Range disponible y ventana/suavizado maduros.
* WARMUP — observaciones insuficientes para estabilizar ATR.
* DEGRADED — dependencia `true_range` degradada o datos subyacentes degradados.
* MISSING — columnas `high`, `low` o `close` no disponibles.

**Dependencias**

* **depends_on**: `true_range`
* **external_sources**: ninguna.

Interpretacion:

* ATR no depende directamente de OHLCV a nivel semantico de Fase 4.
* Su dependencia declarativa es `true_range`, que encapsula la logica base del rango real.

**Parámetros soportados**

| Parámetro | Tipo | Default | Descripción |
|-----------|------|---------|-------------|
| period | int | 14 | Periodo de suavizado de Wilder |
| timeframe | Timeframe | "1d" | Resolución temporal |

**Cálculo objetivo**

Definicion clasica de Wilder:

```text
ATR_t = WilderMean(TR, period)
```

Forma recurrente equivalente:

$$
ATR_t = \frac{(ATR_{t-1} \cdot (n - 1)) + TR_t}{n}
$$

donde $n = period$.

La implementacion actual usa la forma de `ewm` equivalente a Wilder smoothing con `alpha = 1 / period`, `adjust=False` y `min_periods=period`.

**Output**

* **output_type**: float
* **output_column**: `atr_<period>@1.0`
* Una feature, una columna, una semantica.

**Presentación esperada en TradingUI**

* indicador escalar simple
* actualmente en panel separado, no como overlay sobre precio

**Notas de implementación**

Para mantener separacion por fases:

* `TrueRange` sigue siendo la primitive de Fase 2.
* `ATR` vive como feature derivada de Fase 4.
* Puede declararse y validarse a traves del registry formal y el DAG de composicion ya existentes.