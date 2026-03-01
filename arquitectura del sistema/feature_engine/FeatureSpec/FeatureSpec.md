FeatureSpec

domingo, 1 de marzo de 2026

16:12

**Ficha de FeatureSpec**

Entidad declarativa que define **la identidad, semántica temporal, dependencias y reglas de validez** de una feature dentro de FeatureEngine. Es la **fuente de verdad** sobre qué representa una feature y cuándo sus valores existen y son utilizables.

**Identidad**

* **name** — Identificador estable y único de la feature dentro del sistema.
* **version** — Versión semántica que distingue cambios de significado (no de implementación).
* **category** — Naturaleza de la señal (técnica, derivada, serie externa, etc.).

**Semántica temporal**

* **base\_timeframe** — Resolución nativa en la que la feature existe originalmente.
* **availability** — Regla que define el instante a partir del cual un valor pasa a existir (point‑in‑time).
* **alignment** — Política que define cómo se proyecta la feature fuera de su timeframe base.

Estas propiedades fijan **cuándo** existe un valor y **cómo** puede usarse en otros marcos temporales.

**Dependencias**

* **depends\_on** — Conjunto de otras features requeridas para su existencia.
* **external\_sources** — Fuentes externas versionadas necesarias para su cálculo o carga.

Permiten construir el grafo de dependencias y auditar los inputs.

**Madurez**

* **lookback\_required** — Número mínimo de observaciones previas necesarias.
* **warmup\_policy** — Regla que define la transición desde estado de calentamiento a estado válido.

Determinan **cuándo** una feature puede considerarse madura.

**Calidad**

* **interpolation** — Política declarada para tratar huecos en la serie base, si aplica.
* **degrades\_on\_alignment** — Indica si la proyección temporal degrada la calidad del valor.

Estas reglas gobiernan el estado operativo del valor en cada instante.

**Propiedades estructurales**

* Inmutable.
* Comparable y versionable.
* Hashable y serializable.
* Independiente de cualquier lógica de cálculo o ejecución.

**Resultado**

Un FeatureSpec encapsula **toda la semántica necesaria** para que el motor pueda validar, ordenar, alinear y evaluar la calidad de una feature sin conocer cómo se calcula. Es el contrato mínimo y completo que habilita un FeatureEngine determinista y auditable.