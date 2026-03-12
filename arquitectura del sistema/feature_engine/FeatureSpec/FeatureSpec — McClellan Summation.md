**FeatureSpec — McClellan Summation**

**Identidad**

* **name**: mcclellan_summation
* **version**: 1.0
* **category**: EXTERNAL_SERIES
* **source**: csv_external

Serie externa diaria cargada desde CSV. La semantica vive en `FeatureSpec`; la clave persistida se mantiene simple por decision operacional.

**Semántica temporal**

**Frecuencia base**
* **timeframe**: 1d

**Disponibilidad**
* **availability**: NEXT_SESSION
* El valor del dia D pasa a estar disponible para consumo en la sesion siguiente.

**Política de alineación**
* **alignment**: LINEAR_INTERPOLATION
* **interpolation**: LINEAR
* La alineacion a timeframes menores puede interpolar entre puntos diarios.

**Lookback y madurez**

* **lookback_required**: 0
* **warmup_policy**: NONE

**Calidad del dato**

Estados posibles:

* READY — valor original del CSV.
* DEGRADED — valor alineado/interpolado fuera de su timeframe base.
* MISSING — no hay dato disponible.

**Dependencias**

* **depends_on**: ninguna feature interna.
* **external_sources**: `McClellanSumOsc.csv`

**Persistencia**

* **storage_key**: `mcclellan_summation`

Nota:

Aunque el `FeatureSpec` tiene version `1.0`, la clave persistida no usa `@1.0`. Esta excepcion se tomo para mantener simples las series externas manuales respaldadas por CSV.

**Output**

* **output_type**: float
* **output_column**: `mcclellan_summation`