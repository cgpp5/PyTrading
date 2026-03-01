Roadmap v1

sábado, 28 de febrero de 2026

16:03

**🧱 Visión global del sistema**

El sistema final es un **motor algorítmico multi‑estrategia, orientado a eventos**, con:

* adquisición de datos desacoplada,
* cálculo determinista de features,
* múltiples motores de señal concurrentes,
* control de estado transversal,
* ejecución diferida y auditable,
* observabilidad completa,
* UI separada y no crítica.

Todo corre **headless en el VPS**, salvo la UI.

**🧩 Arquitectura final (módulos definitivos)**

MarketFeed ha pasado de ser un “lector de precios” a convertirse en **la capa de adquisición resiliente y consciente del estado del dato**. La descripción general debe reflejar ese salto sin introducir complejidad innecesaria.

**1️⃣ MarketFeed**

**Responsabilidad:** adquisición, armonización y exposición controlada de datos de mercado externos, con tolerancia explícita a fallos y degradación.

* **Diseño en cadena de responsabilidad (fallback controlado):**
  + **Tier 1:** Alpaca (paper trading). Fuente primaria, datos limpios y baja latencia.
  + **Tier 2:** Tiingo. Fallback intermedio con límites de uso conocidos.
  + **Tier 3:** yfinance. Último recurso; datos potencialmente ruidosos o incompletos.
  + Nunca se mezclan proveedores dentro de una misma serie temporal; cada request se resuelve con **un único proveedor**, etiquetado explícitamente.
* **Timeframes discretos y validados:** conjunto cerrado (p. ej. 15m, 1h, 4h, 1d). No resampling ni agregaciones implícitas.
* **Output principal:**
  + **OHLCV armonizado** en un DataFrame canónico, indexado por timestamp UTC.
  + Columnas de control por fila (source, quality, is\_gap, latency\_sec) para exponer contexto operativo del dato.
  + **Metadata estructurada** a nivel de request (proveedor usado, fallback, cobertura, gaps).
* **Normalización estricta:**
  + Esquema de DataFrame universal.
  + Deduplicación determinista por timestamp.
  + Forzado de zona horaria a UTC.
  + Detección y marcaje de gaps; **sin interpolación**.
* **Degradación consciente:** ante caídas o anomalías, el módulo sigue entregando datos cuando es posible, **informando explícitamente de su calidad** para que capas superiores decidan cómo actuar.

**2️⃣ FeatureEngine**

**Responsabilidad:** cálculo puro y reproducible de features.

* Indicadores técnicos (RSI, ADX, ATR, MACD, SMA…).
* Derivadas (pendientes, distancias, % change).
* Caché histórico controlado.
* Funciones puras, sin estado.

Todo lo que hoy calculas *antes* de evaluar condiciones.

**3️⃣ StrategyLogic (plugin‑based)**

**Responsabilidad:** evaluar condiciones y emitir señales abstractas.

* Cada bloque del EA = **una estrategia independiente**:
  + DCA
  + Circuit Breaker
  + Buy Oversold
  + Trend vs Breadth Divergence
* Consume features.
* Produce **intenciones**, no órdenes.
* Sin cooldowns globales ni ejecución.

Traducción directa de CheckDCA, CheckCB, CheckBOS, CheckTVBD.

**4️⃣ TradeStateMachine**

**Responsabilidad:** gestionar estado transversal y temporal.

* Cooldowns.
* Flags de zona (CB).
* Multiplicadores históricos (BOS).
* Ventanas de reentrada (TVBD).
* Persistencia mínima del estado.
* Base de datos SQLite

Aquí vive todo lo que en el EA son static, g\_\*, contadores y flags.

**5️⃣ SignalEngine**

**Responsabilidad:** orquestar señales antes de ejecutar.

* Recibe señales de múltiples estrategias.
* Aplica reglas globales:
  + expiración,
  + deduplicación,
  + prioridad,
  + coherencia temporal.
* Mantiene cola de señales.

Es la formalización de g\_signal\_queue.

**6️⃣ ExecutionController**

**Responsabilidad:** ejecutar intenciones en el broker.

* Traducción señal → orden T212.
* Idempotencia.
* Confirmación post‑ejecución.
* Registro de resultados.

Nunca decide *qué* hacer, solo *cómo* hacerlo.

**7️⃣ Observability**

**Responsabilidad:** visibilidad y control humano.

* Logs semánticos.
* Eventos.
* Alertas (Telegram, webhooks).
* Integración con n8n (errores, cron).

Todo lo que hoy haces con Print, CSVs, eventos visuales.

**8️⃣ TradingUI (headful)**

**Responsabilidad:** visualización y configuración.

* Charts (solo lectura inicialmente).
* Visualización de señales y estado.
* Definición de objetos (futuro).
* Configuración de estrategias.

Nunca ejecuta lógica de trading.

**🗄️ Módulo Transversal: DataStore (Capa de Persistencia)**

**Responsabilidad:** Actuar como la única fuente de la verdad en disco que separa el motor de cálculo de la visualización, permitiendo al sistema retener el estado entre ciclos de ejecución (evitando la "amnesia" de la memoria RAM).

* **Almacenamiento de series temporales:** Guarda el histórico validado de OHLCV y el valor numérico de las *features* calculadas.
* **Memoria del sistema:** Almacena los multiplicadores, contadores de *cooldown* y *flags* activos.
* **Registro de eventos:** Consolida el log estructurado de las intenciones de señal y las confirmaciones de ejecución.