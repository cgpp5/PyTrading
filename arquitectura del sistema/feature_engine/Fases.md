Fases

domingo, 1 de marzo de 2026

15:41

**Fase 1 — Contrato de Feature (modelo conceptual)**

**Objetivo**

Definir **qué es una feature** antes de calcular ninguna.

**Qué se cierra aquí**

* Modelo de datos Feature / FeatureSpec.
* Metadatos obligatorios.
* Semántica temporal explícita.

**Elementos clave del contrato**

* name — identificador estable (rsi\_14, volatility\_20d).
* timeframe — resolución temporal.
* lookback — ventana histórica requerida.
* alignment — close, open, end‑of‑bar, etc.
* dependencies — datos o features requeridas.
* version — cambios semánticos, no de implementación.

**Resultado**

Un contrato que permite afirmar:

“Esta feature significa exactamente esto, y nada más”.

**Fase 2 — Features primitivas (atómicas)**

**Objetivo**

Implementar **features básicas**, directamente derivadas de MarketData.

**Ejemplos**

* returns / log\_returns
* rolling\_mean / rolling\_std
* true\_range
* volume\_zscore

**Restricciones**

* Una sola fuente de datos.
* Una sola ventana.
* Sin dependencia entre features.

**Resultado**

Bloques simples, testeables y reutilizables.

**Fase 3 — Alineación temporal y sincronización**

**Objetivo**

Resolver el problema más peligroso del sistema: **el tiempo**.

**Decisiones explícitas**

* Cuándo una feature “existe”.
* Qué timestamp se le asigna.
* Cómo se alinea con otras features.

**Casos típicos**

* RSI calculado con cierre → disponible solo tras el close.
* Feature diaria usada en timeframe horario → forward‑fill controlado.
* Features multi‑timeframe → reglas de sincronización explícitas.

**Resultado**

Imposibilidad estructural de leakage accidental.

**Fase 4 — Composición de features**

**Objetivo**

Construir features complejas a partir de otras features.

**Ejemplos**

* momentum\_adjusted\_volatility
* trend\_strength = f(rsi, slope, volatility)
* regime\_classification

**Reglas**

* Dependencias explícitas.
* Grafo acíclico.
* Orden de cálculo determinista.

**Resultado**

Un DAG de features reproducible y auditable.

**Fase 5 — Calidad y validez de features**

**Objetivo**

Detectar cuándo una feature **no es fiable**, igual que MarketFeed hace con los datos.

**Señales típicas**

* Lookback insuficiente.
* Gaps en datos subyacentes.
* Forward‑fill excesivo.
* Dependencia de datos degradados.

**Resultado**

Cada feature se marca como:

* válida,
* degradada,
* inválida,

y esa información se propaga aguas arriba.

**Fase 6 — Observabilidad de FeatureEngine**

**Objetivo**

Saber **qué features se calcularon, cuándo y con qué calidad**.

**Eventos**

* feature\_computed
* feature\_degraded
* feature\_missing\_dependency
* feature\_skipped

**Métricas**

* coverage por feature,
* latencia de cálculo,
* tasa de degradación.

**Resultado**

FeatureEngine es tan explicable como MarketFeed.

**Fase 7 — Interfaz de consumo**

**Objetivo**

Exponer features de forma segura y no ambigua.

**Formas típicas**

* DataFrame alineado.
* Snapshot en un timestamp.
* Ventana temporal para backtesting.
* Streaming incremental (opcional).

**Garantía**

El consumidor **no puede pedir algo ambiguo** ni temporalmente inconsistente.

**Qué FeatureEngine no hace**

Para evitar solapamientos futuros:

* No decide trades.
* No optimiza modelos.
* No ajusta hiperparámetros.
* No corrige errores de MarketFeed.
* No introduce heurísticas silenciosas.