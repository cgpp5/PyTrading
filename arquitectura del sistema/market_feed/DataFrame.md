**DataFrame**

sábado, 28 de febrero de 2026

19:55

**🧱 Estructura base (OHLCV)**

Cada fila representa **una vela cerrada** para un (symbol, timeframe).

Columnas obligatorias:

|  |  |  |
| --- | --- | --- |
| **Columna** | **Tipo** | **Significado** |
| timestamp | datetime64[ns, UTC] | Cierre de la vela |
| open | float64 | Precio de apertura |
| high | float64 | Máximo |
| low | float64 | Mínimo |
| close | float64 | Cierre |
| volume | float64 | Volumen (puede ser 0 o NaN si no aplica) |

**Reglas duras:**

* timestamp siempre en UTC.
* Indexado por timestamp.
* Sin forward‑fill, sin back‑fill, sin interpolación.

**🧩 Metadatos por fila**

|  |  |  |
| --- | --- | --- |
| **Columna** | **Tipo** | **Uso** |
| source | category / string | Proveedor real de esa vela |
| quality | category | normal, degraded, dirty |
| is\_gap | bool | True si esta vela fue esperada pero no observada |
| latency\_sec | float | Retraso estimado del dato (opcional) |

Esto permite:

* saber **qué proveedor** alimentó cada decisión,
* detectar **series incompletas** sin romper cálculos,
* degradar estrategias de forma consciente.

**🕳️ Representación de gaps (sin interpolar)**

Cuando falta una vela esperada:

* Se **crea la fila** con:
  + timestamp correcto,
  + OHLCV = NaN,
  + is\_gap = True,
  + quality = degraded.

Esto es crucial:

el sistema **ve el hueco**, no lo ignora ni lo inventa.

Ejemplo conceptual:

|  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **timestamp** | **open** | **high** | **low** | **close** | **volume** | **source** | **quality** | **is\_gap** |
| 2026‑02‑27 16:00 | NaN | NaN | NaN | NaN | NaN | tiingo | degraded | True |

**🧠 Por qué esto no rompe indicadores**

En pandas / numpy:

* los cálculos **no fallan** por NaN,
* los resultados se propagan como NaN,
* StrategyLogic puede decidir:
  + ignorar,
  + pausar,
  + reducir exposición.

**📦 Metadatos a nivel DataFrame**

Además del contenido tabular, MarketFeed debe devolver un objeto con metadata global:

metadata = {
 "symbol": "SPX",
 "timeframe": "1h",
 "source": "alpaca",
 "requested\_window": ("2026-02-01", "2026-02-28"),
 "coverage\_ratio": 0.97,
 "gap\_count": 3,
 "quality": "degraded"
}

Esto permite:

* logging,
* alertas,
* decisiones de alto nivel.

**🧪 Eventos temporales (separados)**

Earnings, macro, scraping de breadth, etc.:

* **No van en este DataFrame**.
* Se entregan como una estructura paralela:

events = [
 {"timestamp": "...", "type": "earnings", "symbol": "AAPL", "source": "tiingo"},
 {"timestamp": "...", "type": "breadth", "value": -1200, "source": "scraper"}
]

Esto evita contaminar series continuas con semántica puntual.