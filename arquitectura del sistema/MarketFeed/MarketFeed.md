MarketFeed

sábado, 28 de febrero de 2026

20:09

**Objetivo operativo de MarketFeed**

MarketFeed debe convertirse en un **servicio de datos determinista y tolerante a fallos** que:

* entregue OHLCV armonizado bajo un contrato estable,
* gestione múltiples proveedores con fallback controlado,
* exponga explícitamente la calidad y cobertura de los datos,
* nunca colapse el sistema por datos incompletos.

**Estructura de carpetas**

marketfeed/
 \_\_init\_\_.py
 types.py
 timeframes.py
 normalize.py
 providers/
 \_\_init\_\_.py
 base.py
 alpaca.py
 tiingo.py
 yfinance.py
 marketfeed.py