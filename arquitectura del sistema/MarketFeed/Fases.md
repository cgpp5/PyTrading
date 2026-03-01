Fases

sábado, 28 de febrero de 2026

20:18

**Fase 0 — Orquestador base**

* MarketFeed como orquestador central.
* Contrato MarketDataProvider.
* Manejo correcto de:
  + errores de proveedor → fallback,
  + errores internos → abortar.
* Observability básica.

**Fase 1 — Normalización canónica**

* normalize\_ohlcv() como única fuente de verdad.
* Invariantes cerrados:
  + timestamps UTC,
  + columnas fijas,
  + tipos estrictos,
  + deduplicación determinista,
  + control de NaNs.
* DataFrame canónico.

**Fase 2 — Primer proveedor real (yfinance)**

* yfinance como Tier 3 (degradado).
* Tests sin red.
* Integración limpia con normalización.

**Fase 3 — Fallback determinista**

* Cadena Alpaca → Tiingo → yfinance.
* Tests de integración de fallback.
* Observability validada.

**Fase 4 — Agregación temporal alineada a mercado**

* Agregación 4h **alineada a sesión real**, no arbitraria.
* Independiente del proveedor.
* Marca is\_gap correctamente.
* Tests exhaustivos.

**Fase 5 — Calendario real + detección de gaps reales**

* Integrar pandas\_market\_calendars.
* Resolver sesiones reales por exchange.
* Detectar:
  + días no operativos,
  + early closes,
  + sesiones incompletas.
* Marcar is\_gap con conocimiento real de mercado.

**Fase 6 — Integración end‑to‑end**

* Que MarketFeed.get\_ohlcv():
  + pida 1h,
  + agregue a 4h si procede,
  + use calendario real automáticamente.
* Flujo completo sin llamadas manuales.

**Fase 7 — Observability real**

* Logs estructurados.
* Métricas de:
  + fallback,
  + latencia,
  + calidad de datos.
* Alertas (no ahora, pero preparado).