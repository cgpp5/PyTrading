Features Complejas
, 
Estado actual de implementacion: parcial.

## Implementado

### Bollinger Bands

Parametros soportados:

- Period
- Deviation
- Timeframe

Estado actual:

- Ya implementado en `feature_engine/composition/bollinger.py`.
- Se modela como tres series derivadas:
  - `bollinger_middle_<period>@1.0`
  - `bollinger_upper_<period>_<deviation>@1.0`
  - `bollinger_lower_<period>_<deviation>@1.0`
- En persistencia siguen siendo tres features escalares.
- En TradingUI ya se agrupan como un solo indicador visual:
  - `bollinger_bands_<period>_<deviation>@<version>`

Apply to:

- Actualmente queda fijo a `close`.
- El parametro `Apply to` todavia no esta expuesto en la implementacion.

## Pendiente

### ATR (Average True Range)

Parametros:

- Period (14)

Estado:

- Ya implementado en `feature_engine/composition/atr.py`.
- El calculo primitivo `TrueRange` sigue siendo la base de Fase 2.
- Nombre persistido:
  - `atr_<period>@1.0`
- En TradingUI sale como indicador escalar en pane separado.

### MACD

Parametros:

- Fast EMA
- Slow EMA
- MACD SMA
- Apply to

Estado:

- Ya implementado en `feature_engine/composition/macd.py`.
- Family persistida como tres features derivadas:
  - `macd_line_<fast>_<slow>_<signal>_<apply_to>@1.0`
  - `macd_signal_<fast>_<slow>_<signal>_<apply_to>@1.0`
  - `macd_histogram_<fast>_<slow>_<signal>_<apply_to>@1.0`
- En TradingUI ya se agrupa como un solo indicador visual:
  - `macd_<fast>_<slow>_<signal>_<apply_to>@<version>`
- El caso implementado por defecto usa:
  - `fast=12`
  - `slow=26`
  - `signal=9`
  - `apply_to=close`

### Bollinger Bands Width

Parametros:

- Period (20)
- Deviation

Estado:

- Ya implementado como feature derivada escalar.
- Nombre persistido:
  - `bollinger_width_<period>_<deviation>@1.0`
- Formula actual:
  - `((upper - lower) / middle) * 100`
- Reutiliza la family ya implementada de Bollinger Bands.

### Average Directional Movement Index (ADX)

Parametros:

- Period (14)

Estado:

- No implementado todavia.

### SMA Osc (Distance to SMA)

Estado:

- No implementado todavia.
		