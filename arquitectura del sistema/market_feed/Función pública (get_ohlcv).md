Función pública (get\_ohlcv)

sábado, 28 de febrero de 2026

20:04

**🎯 Qué debe hacer la función pública**

**Dado un símbolo, un timeframe y una ventana temporal, devolver una serie OHLCV armonizada y autocontenida, con información suficiente para evaluar su fiabilidad.**

**🧩 Firma conceptual de la función**

def get\_ohlcv(

symbol: str,

timeframe: str,

start: datetime,

end: datetime,

\*,

allow\_fallback: bool = True

) -> MarketData:

validate\_timeframe(timeframe)

calendar = calendar\_resolver.resolve(symbol)

expected\_timestamps = calendar.expected\_bars(

timeframe=timeframe,

start=start,

end=end

)

attempted\_providers = []

last\_provider\_error = None

for tier\_index, tier in enumerate(provider\_tiers):

if tier\_index > 0 and not allow\_fallback:

break

provider = tier.provider

attempted\_providers.append(provider.name)

try:

raw\_df = provider.fetch\_ohlcv(

symbol=symbol,

timeframe=timeframe,

start=start,

end=end

)

except ProviderError as e:

# Error externo → fallback permitido

last\_provider\_error = e

observability.log\_warning(

"provider\_failure",

provider=provider.name,

symbol=symbol,

timeframe=timeframe,

error=str(e)

)

continue

try:

df = normalize\_ohlcv(

raw\_df,

provider\_name=provider.name,

quality=tier.quality

)

df = align\_to\_calendar(

df=df,

expected\_timestamps=expected\_timestamps,

provider\_name=provider.name,

quality=tier.quality

)

coverage\_ratio, gap\_count = compute\_coverage(

df=df,

expected\_timestamps=expected\_timestamps

)

except Exception as e:

# Error interno → NO fallback silencioso

observability.alert\_critical(

"marketfeed\_internal\_error",

provider=provider.name,

symbol=symbol,

timeframe=timeframe,

error=str(e),

stacktrace=traceback.format\_exc()

)

raise # o abortar según entorno

metadata = MarketDataMeta(

symbol=symbol,

timeframe=timeframe,

provider\_used=provider.name,

fallback\_used=(tier\_index > 0),

start=start,

end=end,

coverage\_ratio=coverage\_ratio,

gap\_count=gap\_count,

quality=tier.quality,

extra={

"attempted\_providers": attempted\_providers,

"calendar": calendar.name

}

)

return MarketData(df=df, meta=metadata)

# Ningún proveedor funcionó

observability.log\_error(

"all\_providers\_failed",

symbol=symbol,

timeframe=timeframe,

attempted\_providers=attempted\_providers,

last\_error=str(last\_provider\_error)

)

empty\_df = empty\_ohlcv\_dataframe()

metadata = MarketDataMeta(

symbol=symbol,

timeframe=timeframe,

provider\_used="none",

fallback\_used=False,

start=start,

end=end,

coverage\_ratio=0.0,

gap\_count=len(expected\_timestamps),

quality="degraded",

notes="All providers failed",

extra={

"attempted\_providers": attempted\_providers,

"calendar": calendar.name

}

)

return MarketData(df=empty\_df, meta=metadata)

Donde MarketData es un **objeto compuesto**, no solo un DataFrame.

**📦 Qué devuelve**

**1️⃣ DataFrame OHLCV**

* Indexado por timestamp (UTC).
* Columnas:
  + open, high, low, close, volume
  + source
  + quality
  + is\_gap
  + latency\_sec

Este DataFrame **siempre existe**, incluso si está parcialmente vacío o degradado.

**2️⃣ Metadata estructurada**

Separada del DataFrame, para decisiones de alto nivel:

metadata = {
 "symbol": "SPX",
 "timeframe": "1h",
 "provider\_used": "alpaca",
 "fallback\_used": False,
 "requested\_window": (start, end),
 "coverage\_ratio": 0.98,
 "gap\_count": 2,
 "quality": "degraded"
}

**🔁 Comportamiento esperado (reglas duras)**

* Si el proveedor primario falla:
  + se intenta fallback si allow\_fallback=True.
* Nunca se mezclan proveedores dentro de una misma serie.
* Si no hay datos:
  + se devuelve DataFrame vacío **con metadata explicativa**.
* Nunca se lanza una excepción por “datos incompletos”.
* La degradación **se comunica**, no se oculta.

**🧠 Por qué esta firma es suficiente**

Con esta función:

* FeatureEngine puede calcular indicadores sin preocuparse del origen.
* StrategyLogic puede decidir si confía o no en los datos.
* Observability puede alertar de degradaciones.
* ExecutionController nunca se entera de cómo se obtuvieron los precios.

Es el punto exacto donde se corta la complejidad.