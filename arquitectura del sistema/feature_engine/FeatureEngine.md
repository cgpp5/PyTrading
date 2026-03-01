FeatureEngine

domingo, 1 de marzo de 2026

15:41

**Objetivo operativo de FeatureEngine**

**FeatureEngine transforma MarketData en un conjunto determinista de features temporales, alineadas, versionadas y semánticamente explícitas, listas para ser consumidas por estrategias, modelos o pipelines de investigación, sin introducir leakage temporal ni decisiones implícitas.**

En términos operativos:

* MarketFeed garantiza **datos correctos y observables**.
* FeatureEngine garantiza **señales correctas y explicables**.

No optimiza, no decide trades, no “arregla” datos: **interpreta**.

**Principios de diseño (no negociables)**

Estos principios gobiernan todas las fases:

* **Cero leakage temporal** — ninguna feature puede usar información futura, ni directa ni implícita.
* **Determinismo total** — mismos inputs → mismas features → mismos valores.
* **Alineación explícita** — cada feature sabe a qué timestamp pertenece y por qué.
* **Semántica fuerte** — una feature es un concepto definido, no una columna arbitraria.
* **Composición controlada** — features simples → features derivadas, sin acoplamientos ocultos.
* **Observabilidad** — se puede explicar qué se calculó, cuándo y con qué calidad.

La estructura del **módulo FeatureSpec** debe reflejar una sola idea: **el contrato semántico es estable, pequeño y aislado**. No debe crecer con el motor ni con las implementaciones. Su función es fijar vocabulario, invariantes y tipos que el resto del sistema **no puede violar**.

**Estructura de archivos — módulo featurespec**

featureengine/
└── featurespec/
 ├── \_\_init\_\_.py
 ├── enums.py
 ├── temporal.py
 ├── quality.py
 ├── spec.py
 └── tests/
 ├── test\_enums.py
 ├── test\_temporal\_rules.py
 └── test\_feature\_spec.py

**enums.py — vocabulario semántico base**

Define **qué tipos de features existen** y **qué políticas son legales**.

Define los **tipos cerrados** que describen la naturaleza de una feature.

* FeatureCategory
* BaseTimeframe
* AlignmentPolicy
* InterpolationPolicy
* WarmupPolicy

Este archivo no contiene lógica. Solo define **qué conceptos existen** en el sistema.

**temporal.py — reglas de existencia en el tiempo**

Define **cuándo un valor pasa a existir** (point‑in‑time).

Agrupa todo lo relacionado con **point‑in‑time semantics**.

* AvailabilityRule
* Validaciones temporales básicas (por ejemplo, combinaciones legales de base timeframe + availability).
* Tipos auxiliares si fueran necesarios para expresar reglas temporales complejas.

Aquí se fija **cuándo un valor pasa a existir**, no cómo se calcula.

**quality.py — estados operativos de una feature**

Define **el estado operativo del valor**, no su cálculo.

Define el estado de validez de un valor en un instante concreto.

* FeatureQuality
* Reglas de transición permitidas (por ejemplo, WARMUP → READY, READY → DEGRADED).

No hay inferencia automática; solo definición de estados posibles.

**spec.py — contrato FeatureSpec**

Este es el **contrato central**. Todo FeatureEngine gira alrededor de esto.

Contiene **una única entidad central**:

* FeatureSpec

Responsabilidades:

* Declarar identidad, versión y categoría.
* Declarar semántica temporal completa.
* Declarar dependencias y fuentes externas.
* Declarar reglas de madurez y calidad.

Debe ser:

* inmutable,
* hashable,
* serializable,
* validada en construcción.

No contiene:

* cálculo,
* caché,
* ejecución,
* referencias a pandas, numpy o librerías externas.

**tests/ — cierre contractual**

Tests que garantizan que el contrato **no se degrada con el tiempo**.

* test\_enums.py
  Verifica que los enums son cerrados y coherentes.
* test\_temporal\_rules.py
  Verifica combinaciones legales e ilegales de reglas temporales.
* test\_feature\_spec.py
  Verifica que:
  + no se puede crear un FeatureSpec incompleto,
  + las dependencias están bien declaradas,
  + las reglas de calidad y madurez son obligatorias.

Estos tests son el equivalente a los tests de Fase 0 de MarketFeed.

**Invariante estructural clave**

Nada fuera de featurespec/ puede:

* definir nuevos estados de calidad,
* inventar reglas temporales,
* reinterpretar una feature.

El motor, el DAG y las implementaciones **solo consumen este contrato**.