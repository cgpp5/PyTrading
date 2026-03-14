**FeatureSpec — ADX (Average Directional Index, Wilder)**

**Estado**

Implementado en Fase 4.

El modulo objetivo es `feature_engine.composition.adx`.

**Identidad**

ADX se define como una family compuesta de tres series relacionadas:

* **adx**: `adx_{period}`
* **plus_di**: `plus_di_{period}`
* **minus_di**: `minus_di_{period}`

Version objetivo:

* **version**: 1.0
* **category**: DERIVED
* **module objetivo**: `feature_engine.composition.adx`

La family representa fuerza de tendencia y direccion relativa segun la formulacion de Wilder.

Interpretacion semantica:

* `plus_di` mide presion direccional alcista normalizada por rango verdadero suavizado.
* `minus_di` mide presion direccional bajista normalizada por rango verdadero suavizado.
* `adx` mide fuerza de tendencia sin direccion.

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

Lookback objetivo minimo de la family:

* **plus_di / minus_di**: `period`
* **adx**: `2 * period - 1`
* **warmup_policy**: FIXED_LOOKBACK

Razon:

* `plus_di` y `minus_di` requieren suavizado Wilder de `+DM`, `-DM` y `TR`.
* `adx` requiere primero una serie madura de `DX` y luego una segunda etapa de suavizado Wilder sobre `DX`.

**Calidad del dato**

Estados esperados:

* READY — `TR`, `+DM`, `-DM`, `DI`, `DX` y `ADX` maduros.
* WARMUP — historia insuficiente para alguna etapa de Wilder smoothing.
* DEGRADED — dependencia degradada o datos OHLC subyacentes degradados.
* MISSING — columnas `high`, `low` o `close` no disponibles.

**Dependencias**

Dependencias semanticas objetivo:

* **plus_di** depende de:
  - `true_range`
  - movimiento direccional positivo derivado de OHLC
* **minus_di** depende de:
  - `true_range`
  - movimiento direccional negativo derivado de OHLC
* **adx** depende de:
  - `plus_di_{period}`
  - `minus_di_{period}`

Nota arquitectural:

* La implementacion puede encapsular internamente `+DM`, `-DM` y `DX` o modelarlos como nodos internos no persistidos.
* El contrato minimo visible hacia persistencia y UI son `plus_di`, `minus_di` y `adx`.

**Parámetros soportados**

| Parámetro | Tipo | Default | Descripción |
|-----------|------|---------|-------------|
| period | int | 14 | Periodo Wilder para TR, DM y ADX |
| timeframe | Timeframe | "1d" | Resolución temporal |

Restricciones objetivo:

* `period >= 2`

**Cálculo objetivo**

Movimiento direccional:

```text
up_move = high_t - high_{t-1}
down_move = low_{t-1} - low_t

+DM_t = up_move   if up_move > down_move and up_move > 0 else 0
-DM_t = down_move if down_move > up_move and down_move > 0 else 0
```

Rango verdadero:

```text
TR_t = max(
    high_t - low_t,
    abs(high_t - close_{t-1}),
    abs(low_t - close_{t-1})
)
```

Suavizado Wilder:

```text
ATR_t = WilderMean(TR, period)
+DMs_t = WilderMean(+DM, period)
-DMs_t = WilderMean(-DM, period)

+DI_t = 100 * (+DMs_t / ATR_t)
-DI_t = 100 * (-DMs_t / ATR_t)

DX_t = 100 * abs(+DI_t - -DI_t) / (+DI_t + -DI_t)
ADX_t = WilderMean(DX, period)
```

Forma recurrente de Wilder para cualquier serie suavizada `S`:

$$
S_t = \frac{(S_{t-1} \cdot (n - 1)) + x_t}{n}
$$

con semilla inicial igual a la media simple de los primeros $n$ valores validos.

**Persistencia**

Cada serie visible se persiste por separado como feature escalar:

* `adx_<period>@1.0`
* `plus_di_<period>@1.0`
* `minus_di_<period>@1.0`

Los nodos intermedios como `+DM`, `-DM`, `DX` o sus suavizados no forman parte del contrato de persistencia v1.

**Presentación en TradingUI**

Objetivo visual:

* un solo indicador agrupado
* panel separado
* tres series visuales:
  - `adx`
  - `plus_di`
  - `minus_di`

Nota:

* la clave agrupada de UI debe evitar colisionar con la clave escalar `adx_<period>@1.0` si la API mantiene ambos contratos simultaneamente.

**Notas de implementación**

Para mantener consistencia con ATR y el resto de Fase 4:

* el suavizado debe ser Wilder real, no una aproximacion informal;
* la family debe poder validarse en el registry formal y ejecutarse via DAG;
* si se reutiliza `true_range`, la semantica de ADX debe quedar desacoplada de detalles de persistencia;
* la implementacion debe ser contrastada contra una referencia externa como MT5 antes de considerarse cerrada para uso algorítmico.