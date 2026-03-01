domingo, 1 de marzo de 2026

16:12

**FeatureSpec — McClellan Oscillator**

**Identidad**

* **name**: mcclellan\_oscillator
* **version**: 1.0
* **category**: external\_macro
* **source**: csv\_external

La versión es semántica: si cambian reglas de interpolación o disponibilidad, **sube la versión**, aunque el cálculo sea el mismo.

**Semántica temporal (clave)**

**Frecuencia base**

* base\_timeframe: 1D

**Disponibilidad**

* El valor del día **D** está disponible **a partir del cierre de D**.
* Para timeframes intradía, el valor se considera válido **durante la sesión D+1**.

Esto sustituye de forma explícita el -86400 del código MT5.

**Política de alineación**

* **alignment\_mode**: forward\_projected
* **projection\_rule**:
  + diario → intradía: interpolación lineal opcional
  + diario → diario: valor exacto

La interpolación **no es obligatoria**; es una política declarada.

**Política de interpolación**

* **interpolation**: linear
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
* **external\_dependency**: mcclellan\_csv\_vX

Esto permite:

* versionar el CSV,
* reproducir backtests antiguos,
* auditar cambios de fuente.

**Output**

* **output\_type**: float
* **output\_columns**:
  + mcclellan\_oscillator

Una feature, una columna, una semántica.

**Observabilidad esperada**

Eventos que debe emitir FeatureEngine al calcularla:

* feature\_loaded\_external
* feature\_interpolated
* feature\_degraded
* feature\_missing

Esto es crítico para explicar decisiones posteriores.

**Qué NO hace este FeatureSpec**

* No escribe CSV.
* No corrige histórico.
* No asume timezone implícito.
* No depende del timeframe del gráfico.
* No decide cómo se usa en una estrategia.

**Correspondencia directa con el código MT5**

|  |  |
| --- | --- |
| **Comportamiento MT5** | **Estado en FeatureEngine** |
| Lectura CSV | ✔️ |
| Interpolación gaps | ✔️ (declarada) |
| Interpolación intradía | ✔️ (declarada) |
| Escritura CSV | ❌ |
| Ajuste -86400 | ❌ (regla explícita) |
| Mutación histórica | ❌ |

Nada esencial se pierde; todo lo peligroso se elimina.

**Por qué este es el test correcto para FeatureEngine**

Si FeatureEngine puede manejar **esta feature** correctamente:

* exógena,
* diaria,
* interpolada,
* con semántica temporal no trivial,

entonces puede manejar:

* RSI,
* MACD,
* spreads,
* señales macro,
* cualquier cosa que venga después.

Este FeatureSpec es un **canario en la mina** arquitectónica.

El siguiente paso natural es definir **el FeatureSpec del McClellan Summation Index**, que será casi idéntico pero nos permitirá validar reutilización y versionado. ¿Seguimos con ese o prefieres que traduzcamos este contrato a una estructura de clases concreta (FeatureSpec, ExternalSeriesSpec) antes?