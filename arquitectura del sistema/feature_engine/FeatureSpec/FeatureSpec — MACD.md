**FeatureSpec — MACD**

**Estado**

Implementado en Fase 4.

La family vive en `feature_engine.composition.macd` y hoy ya forma parte del conjunto de indicadores agrupados de TradingUI.

**Identidad**

MACD se define como una family compuesta de tres series relacionadas:

* **line**: `macd_line_{fast}_{slow}_{signal}_{apply_to}`
* **signal**: `macd_signal_{fast}_{slow}_{signal}_{apply_to}`
* **histogram**: `macd_histogram_{fast}_{slow}_{signal}_{apply_to}`

Version actual:

* **version**: 1.0
* **category**: DERIVED
* **module objetivo**: `feature_engine.composition.macd`

La family representa momentum y convergencia/divergencia entre dos medias exponenciales, mas una serie de señal y un histograma derivado.

**Semántica temporal**

**Frecuencia base**
* **timeframe**: configurable (default `1d`)

**Disponibilidad**
* **availability**: AT_CLOSE
* Cada valor existe al cierre del bar `t`.

**Política de alineación**
* **alignment**: NONE
* No se proyecta fuera de su timeframe base.

**Lookback y madurez**

Lookback objetivo minimo:

* **lookback_required**: `slow + signal - 1`
* **warmup_policy**: FIXED_LOOKBACK

Razon:

* la linea MACD necesita que la EMA lenta madure primero,
* la signal necesita suficiente historia de la propia linea MACD.

**Calidad del dato**

Estados esperados:

* READY — todas las EMAs y derivados maduros.
* WARMUP — historia insuficiente para la linea, la signal o el histograma.
* DEGRADED — datos subyacentes degradados o dependencia degradada.
* MISSING — columna fuente no disponible.

**Dependencias**

Dependencias semanticas actuales:

* **MACD line** depende de:
  - `ema_{fast}_{apply_to}`
  - `ema_{slow}_{apply_to}`
* **Signal** depende de:
  - `macd_line_{fast}_{slow}_{signal}_{apply_to}`
* **Histogram** depende de:
  - `macd_line_{fast}_{slow}_{signal}_{apply_to}`
  - `macd_signal_{fast}_{slow}_{signal}_{apply_to}`

Nota:

La implementacion actual ya declara estas dependencias en `FeatureSpec` y puede validarlas mediante el registry formal y el DAG general de ejecucion.

**Parámetros soportados**

| Parámetro | Tipo | Default | Descripción |
|-----------|------|---------|-------------|
| fast | int | 12 | Periodo de la EMA rápida |
| slow | int | 26 | Periodo de la EMA lenta |
| signal | int | 9 | Periodo de la EMA de señal |
| apply_to | str | "close" | Columna fuente |
| timeframe | Timeframe | "1d" | Resolución temporal |

Restricciones actuales:

* `fast >= 1`
* `slow >= 2`
* `signal >= 1`
* `fast < slow`

**Cálculo**

```text
macd_line = EMA(apply_to, fast) - EMA(apply_to, slow)
signal = EMA(macd_line, signal)
histogram = macd_line - signal
```

Equivalentemente:

$$
MACD_t = EMA_{fast}(P_t) - EMA_{slow}(P_t)
$$

$$
Signal_t = EMA_{signal}(MACD_t)
$$

$$
Histogram_t = MACD_t - Signal_t
$$

**Persistencia**

Cada serie se persiste por separado como feature escalar:

* `macd_line_<fast>_<slow>_<signal>_<apply_to>@1.0`
* `macd_signal_<fast>_<slow>_<signal>_<apply_to>@1.0`
* `macd_histogram_<fast>_<slow>_<signal>_<apply_to>@1.0`

**Presentación en TradingUI**

Visualmente se trata como un solo indicador compuesto:

* clave agrupada: `macd_<fast>_<slow>_<signal>_<apply_to>@1.0`
* series visuales:
  - line
  - signal
  - histogram

Visualizacion actual:

* panel separado
* line y signal como lineas
* histogram como barras

**Notas de implementación**

Para evitar drift con la arquitectura actual:

* MACD ya se apoya en el registry formal de composicion y el DAG general.
* La agrupacion visual ocurre en TradingUI, no en DataStore.