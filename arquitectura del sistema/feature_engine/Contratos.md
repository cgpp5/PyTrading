Contratos

domingo, 1 de marzo de 2026

15:45

FeatureEngine debe reflejar **contratos explícitos, separación semántica y evolución por fases**, igual que MarketFeed. La estructura de carpetas no es solo organización: **codifica las decisiones arquitectónicas** y evita que se mezclen responsabilidades con el tiempo.

La siguiente estructura asume que marketfeed ya existe y queda **cerrado**.

**Estructura de alto nivel**

featureengine/
├── \_\_init\_\_.py
├── engine.py
├── registry.py
├── errors.py
├── observability.py
├── types/
├── specs/
├── primitives/
├── composition/
├── alignment/
├── quality/
├── execution/
└── tests/

Cada carpeta corresponde **directamente a una fase** o a un contrato estable.

**Núcleo del sistema**

**engine.py**

Responsabilidad única: **orquestar el cálculo de features**.

* Recibe MarketData
* Resuelve dependencias
* Ejecuta el DAG
* Devuelve features alineadas

No contiene lógica matemática ni reglas temporales.

**registry.py**

Registro explícito de features disponibles.

* Mapea FeatureSpec → implementación
* Evita imports implícitos
* Permite versionado y validación

Es el equivalente conceptual al resolver de calendario en MarketFeed.

**errors.py**

Errores semánticos del dominio de features.

* FeatureNotRegistered
* MissingDependency
* InvalidAlignment
* InsufficientLookback

Nunca se lanzan errores genéricos.

**observability.py**

Observabilidad semántica de FeatureEngine.

* record\_feature\_computed
* record\_feature\_degraded
* record\_feature\_skipped
* métricas de cobertura y latencia

Debe ser paralela (no idéntica) a la de MarketFeed.

**Contratos y tipos (Fase 1)**

**types/**

Modelos de datos **puros**, sin lógica.

types/
├── feature.py # Feature, FeatureValue
├── feature\_spec.py # FeatureSpec, Alignment, Lookback
├── feature\_set.py # Colección alineada de features
└── enums.py # Estados, calidades, alineaciones

Aquí se define **qué es una feature**, no cómo se calcula.

**specs/**

Definiciones declarativas de features.

specs/
├── base.py # FeatureSpec base
├── returns.py
├── volatility.py
├── momentum.py
└── volume.py

Cada archivo define **el contrato**, no la implementación.

**Cálculo de features**

**primitives/ (Fase 2)**

Features atómicas, sin dependencias.

primitives/
├── returns.py
├── rolling.py
├── volatility.py
└── volume.py

Reglas:

* Una fuente
* Una ventana
* Sin composición

**alignment/ (Fase 3)**

Toda la lógica temporal vive aquí.

alignment/
├── aligner.py
├── forward\_fill.py
├── resample.py
└── rules.py

Nada fuera de esta carpeta puede decidir timestamps.

**composition/ (Fase 4)**

Features derivadas de otras features.

composition/
├── dag.py
├── composed\_features.py
└── validators.py

Aquí se construye el grafo acíclico y se valida.

**quality/ (Fase 5)**

Gestión de validez y degradación.

quality/
├── evaluator.py
├── rules.py
└── propagation.py

Equivalente conceptual a quality en MarketFeed, pero a nivel de señal.

**execution/ (Fase 6–7)**

Ejecución controlada y exposición.

execution/
├── executor.py
├── snapshot.py
├── window.py
└── streaming.py

Define **cómo se consumen** las features, no cómo se calculan.

**Tests**

**tests/**

Estructura paralela al código.

tests/
├── test\_specs.py
├── test\_primitives.py
├── test\_alignment.py
├── test\_composition.py
├── test\_quality.py
└── test\_engine.py

Los tests validan **semántica y contratos**, no implementaciones internas.