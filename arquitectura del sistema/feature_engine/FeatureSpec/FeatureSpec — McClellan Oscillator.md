**FeatureSpec — McClellan Oscillator**

**Identidad**

* **name**: mcclellan\_oscillator
* **version**: 1.0
* **category**: EXTERNAL_SERIES
* **source**: csv\_external

La version es semantica: si cambian reglas de interpolacion o disponibilidad, **sube la version**, aunque el calculo sea el mismo.

**Semántica temporal (clave)**

**Frecuencia base**
* base\_timeframe: 1D

**Disponibilidad**
* El valor del día **D** está disponible **a partir del cierre de D**.
* Para timeframes intradía, el valor se considera válido **durante la sesión D+1**.

**Política de alineación**
* **alignment**: LINEAR_INTERPOLATION
* **projection\_rule**:
  + diario -> intradia: interpolacion lineal al alinearse
  + diario -> diario: valor exacto por fecha normalizada

**Política de interpolación**
* **interpolation**: LINEAR
* **interpolate\_gaps**: true
* **interpolate\_intraday**: true

Importante:

* La interpolación **no modifica la serie original**.
* El resultado interpolado se marca como calidad degradada.

**Lookback y madurez**

* **lookback\_required**: 0
* **warmup\_policy**: none

No necesita histórico previo para existir, pero sí puede degradarse si hay gaps.

**Calidad del dato**

Estados posibles:

* READY — valor original del CSV.
* DEGRADED — valor interpolado (gap o intradía).
* MISSING — no hay dato disponible aún.

Nunca se devuelve NaN silencioso.

**Dependencias**

* **depends\_on**: ninguna feature interna.
* **external\_sources**: `McClellanOsc.csv`

**Output**

* **output\_type**: float
* **output\_columns**:
  + mcclellan\_oscillator

**Persistencia**

* **storage_key**: `mcclellan_oscillator`

Nota:

Aunque el `FeatureSpec` tiene version `1.0`, la clave persistida no usa `@1.0`. Esta excepcion se tomo para mantener simples las series externas manuales respaldadas por CSV.

Una feature, una columna, una semántica.

**Observabilidad esperada**

Eventos que debe emitir FeatureEngine al calcularla:

* feature\_loaded\_external
* feature\_interpolated
* feature\_degraded
* feature\_missing