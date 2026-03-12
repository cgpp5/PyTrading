**FeatureSpec — Bollinger Bands**

**Identidad**

Esta family se implementa hoy como tres features derivadas relacionadas:

* **middle**: `bollinger_middle_{period}`
* **upper**: `bollinger_upper_{period}_{deviation}`
* **lower**: `bollinger_lower_{period}_{deviation}`

Version actual:

* **version**: 1.0
* **category**: DERIVED
* **module**: `feature_engine.composition.bollinger`

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

* **Middle** depende de `sma_{period}`.
* **Upper** depende de `sma_{period}` y `rolling_std_{period}`.
* **Lower** depende de `sma_{period}` y `rolling_std_{period}`.

**Parámetros soportados**

| Parámetro | Tipo | Default | Aplicación |
|-----------|------|---------|------------|
| period | int | 20 | middle / upper / lower |
| deviation | float | 2.0 | upper / lower |
| timeframe | Timeframe | "1d" | all |

**Cálculo**

```text
middle = sma(close, period)
upper = sma(close, period) + deviation * rolling_std(close, period)
lower = sma(close, period) - deviation * rolling_std(close, period)
```

**Persistencia**

Cada linea se persiste como una feature escalar independiente:

* `bollinger_middle_<period>@1.0`
* `bollinger_upper_<period>_<deviation>@1.0`
* `bollinger_lower_<period>_<deviation>@1.0`

**Presentación en TradingUI**

En la UI estas tres series ya no se exponen como tres overlays distintos. El backend las agrupa como un solo indicador visual:

* `bollinger_bands_<period>_<deviation>@<version>`

Esto preserva el contrato scalar-per-feature de DataStore sin perder la semantica visual correcta del indicador.

**Bollinger Band Width**

Tambien se implemento la feature derivada:

* `bollinger_width_{period}_{deviation}`

Semantica actual:

* **category**: DERIVED
* **availability**: AT_CLOSE
* **alignment**: NONE
* **lookback_required**: `period`
* **warmup_policy**: FIXED_LOOKBACK

Dependencias declaradas:

* `bollinger_middle_{period}`
* `bollinger_upper_{period}_{deviation}`
* `bollinger_lower_{period}_{deviation}`

Formula implementada:

```text
width = ((upper - lower) / middle) * 100
```

Persistencia:

* `bollinger_width_<period>_<deviation>@1.0`

Presentacion actual:

* hoy sale como indicador escalar simple en TradingUI
* no forma parte del grupo visual `bollinger_bands_*`