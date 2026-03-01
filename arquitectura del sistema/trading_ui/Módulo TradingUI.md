# Módulo: trading_ui (Visualización de Validación)

## Posición en la arquitectura

trading_ui es un módulo **consumidor de solo lectura** que lee datos de data_store y los presenta como charts interactivos en el navegador. No modifica datos, no calcula features y no ejecuta estrategias. Su única dependencia ascendente es data_store.

```
market_feed ──► data_store ◄── feature_engine
                    │
                    ▼
               trading_ui
              (FastAPI + LWC)
                    │
                    ▼
                Navegador
```

## Objetivo operativo

Proporcionar validación visual del pipeline completo: datos OHLCV de market_feed, features calculados por feature_engine, y persistencia de data_store — todo renderizado como charts interactivos con Lightweight Charts v5.x. No reemplaza tests automatizados; los complementa con feedback visual inmediato.

---

## Decisiones arquitecturales

| # | Decisión | Opción elegida | Alternativas descartadas |
|---|----------|---------------|------------------------|
| D1 | Servidor | FastAPI (ASGI) | Flask, http.server stdlib, HTML offline |
| D2 | Flujo de datos | API REST intermedia | Directo DataStore, directo MarketFeed |
| D3 | Layout | Candlestick + Volumen + Indicador | Solo candlestick, candles+volumen |
| D4 | Alcance v1 | Selector en la UI (dropdowns) | Hardcoded, CLI params |
| D5 | Indicador | Rolling Mean (overlay sobre candlestick) | Rolling Std, Simple Returns, selector dinámico |
| D6 | Origen features | Leer de DataStore | Calcular on-the-fly, fallback mixto |
| D7 | Estructura proyecto | Separar `trading_ui/` y `frontend/` | Todo en `trading_ui/` |

---

## Principios de diseño

### 1. Solo lectura (Read-Only Consumer)

trading_ui **jamás escribe** en data_store. Solo lee vía `load_market_data()`. Si no hay datos persistidos, muestra un mensaje informativo — nunca intenta descargar ni calcular.

### 2. Separación estricta backend/frontend

Python (FastAPI) sirve datos como JSON y archivos estáticos. JavaScript (Lightweight Charts) renderiza charts. No hay templates Jinja, no hay HTML generado desde Python. El frontend es un SPA estático puro.

### 3. Cero procesamiento en el frontend

Todas las transformaciones (DatetimeIndex → UNIX seconds, feature unpacking, filtrado por rango) ocurren en el backend. El frontend recibe arrays de objetos listos para `setData()`.

### 4. Desacoplamiento por contratos REST

El frontend no sabe que el backend usa SQLite ni pandas. El backend no sabe que el frontend usa Lightweight Charts. El contrato es: endpoints JSON con shapes documentados.

---

## Stack tecnológico

| Capa | Tecnología | Versión | Rol |
|------|-----------|---------|-----|
| Backend | FastAPI | 0.115+ | Servidor ASGI, routing, serialización JSON |
| ASGI runner | uvicorn | 0.34+ | Proceso HTTP |
| Frontend | Lightweight Charts | 5.0 | Renderizado de charts financieros (~30 kB) |
| Persistencia | SQLite (via data_store) | — | SSOT ya implementada |

**Dependencias nuevas:** `fastapi`, `uvicorn`. Se añaden a `pyproject.toml` bajo extras o dependencies.

---

## Estructura de directorios

```
trading_ui/
    __init__.py
    server.py          ← FastAPI app + endpoints
    seed.py             ← Script para poblar data_store con datos de prueba

frontend/
    index.html          ← SPA: dropdowns + contenedor del chart
    app.js              ← Lógica: fetch → LWC → render
    style.css           ← Estilos mínimos

tests/
    test_trading_ui_api.py  ← Tests de endpoints con TestClient
```

---

## Contratos REST (API)

### `GET /api/symbols`

Lista los símbolos disponibles en data_store (DISTINCT de `market_data`).

**Response:**
```json
{
  "symbols": ["AAPL", "SPY", "MSFT"]
}
```

### `GET /api/timeframes`

Lista los timeframes válidos.

**Response:**
```json
{
  "timeframes": ["15m", "1h", "4h", "1d"]
}
```

### `GET /api/ohlcv?symbol=AAPL&timeframe=1d`

Carga OHLCV + volumen desde data_store. Convierte timestamps a UNIX seconds (UTC).

**Response:**
```json
{
  "symbol": "AAPL",
  "timeframe": "1d",
  "candles": [
    {"time": 1706745600, "open": 185.2, "high": 186.1, "low": 184.5, "close": 185.8},
    {"time": 1706832000, "open": 185.9, "high": 187.3, "low": 185.0, "close": 186.5}
  ],
  "volume": [
    {"time": 1706745600, "value": 52340000},
    {"time": 1706832000, "value": 48210000}
  ]
}
```

**Formato de `time`:** UNIX timestamp en **segundos** (no milisegundos). Lightweight Charts requiere `UTCTimestamp` como `number` para datos intradiarios.

**Transformación en el backend:**
- `DatetimeIndex[ns, UTC]` → `int(ts.timestamp())` por fila.
- OHLCV como `float`, volumen como `float`.
- Filas con `is_gap=True` se incluyen con valores normales (LWC no requiere `WhitespaceData` explícito si hay OHLCV).

### `GET /api/features?symbol=AAPL&timeframe=1d&feature=sma_50@1.0`

Carga un feature específico desde la columna `features` de data_store.

**Response:**
```json
{
  "symbol": "AAPL",
  "timeframe": "1d",
  "feature": "sma_50@1.0",
  "data": [
    {"time": 1706745600, "value": 183.4},
    {"time": 1706832000, "value": 183.9}
  ]
}
```

**Notas:**
- Si el feature no existe para ninguna fila, devuelve `"data": []`.
- Filas donde el feature tiene `quality: "missing"` o valor `NaN` se omiten del array (producen gaps naturales en LWC).
- El endpoint lee via `load_market_data()` que ya deserializa el JSON de features en columnas del DataFrame.

### `GET /api/available-features?symbol=AAPL&timeframe=1d`

Lista los features disponibles en data_store para esa combinación symbol+timeframe.

**Response:**
```json
{
  "features": ["returns@1.0", "sma_50@1.0", "rolling_std_20@1.0"]
}
```

**Implementación:** Lee una muestra de filas, inspecciona el JSON de features, y devuelve las claves únicas encontradas.

---

## Arquitectura del frontend

### Layout HTML

```
┌─────────────────────────────────────────────┐
│  [Symbol ▼] [Timeframe ▼] [Feature ▼] [Go] │  ← Barra de controles
├─────────────────────────────────────────────┤
│                                             │
│           Candlestick + Overlay             │  ← Panel principal (LWC)
│         (Rolling Mean como línea)           │
│                                             │
├─────────────────────────────────────────────┤
│           Volume Histogram                  │  ← Panel secundario (LWC pane)
└─────────────────────────────────────────────┘
```

### Flujo JavaScript

```
1. Al cargar la página:
   fetch("/api/symbols")       → poblar dropdown de símbolos
   fetch("/api/timeframes")    → poblar dropdown de timeframes

2. Al hacer click en [Go] (o al seleccionar):
   fetch("/api/ohlcv?symbol=X&timeframe=Y")
     → chart.addSeries(CandlestickSeries) → series.setData(candles)
     → volumePane.addSeries(HistogramSeries) → volumeSeries.setData(volume)

   fetch("/api/available-features?symbol=X&timeframe=Y")
     → poblar dropdown de features

3. Al seleccionar un feature:
   fetch("/api/features?symbol=X&timeframe=Y&feature=Z")
     → chart.addSeries(LineSeries) → featureSeries.setData(data)
```

### Lightweight Charts: Setup

```javascript
const chart = createChart(container, {
    width: container.clientWidth,
    height: 500,
    layout: { background: { color: '#1e1e2e' }, textColor: '#cdd6f4' },
    grid: { vertLines: { color: '#313244' }, horzLines: { color: '#313244' } },
    timeScale: { timeVisible: true, secondsVisible: false },
});

// Panel principal: Candlestick
const candleSeries = chart.addSeries(CandlestickSeries, {
    upColor: '#a6e3a1', downColor: '#f38ba8',
    borderUpColor: '#a6e3a1', borderDownColor: '#f38ba8',
    wickUpColor: '#a6e3a1', wickDownColor: '#f38ba8',
});

// Panel secundario: Volumen (en pane separado)
const volumePane = chart.addPane({ height: 120 });
const volumeSeries = volumePane.addSeries(HistogramSeries, {
    color: '#89b4fa',
    priceFormat: { type: 'volume' },
});

// Overlay: Feature como línea sobre el candlestick
const featureSeries = chart.addSeries(LineSeries, {
    color: '#fab387',
    lineWidth: 2,
});
```

---

## Consideraciones

### Datos pre-cargados (requisito)

trading_ui asume que data_store ya contiene datos. Se proporciona un script `seed.py` que:
1. Llama a `MarketFeed.get_ohlcv()` para descargar OHLCV.
2. Calcula features con feature_engine (ej: `RollingMean(window=50)`).
3. Persiste ambos en data_store vía `save_market_data()` + `save_features()`.

### Timestamps UTC

Lightweight Charts opera exclusivamente en UTC. Los timestamps se convierten en el backend:
```python
int(pd.Timestamp("2024-02-01", tz="UTC").timestamp())  # → 1706745600
```
No se aplica ningún offset de timezone en el frontend.

### Volumen en pane separado

LWC v5 soporta múltiples panes via `chart.addPane()`. El volumen se renderiza como `HistogramSeries` en un pane inferior con altura fija (120px). El pane principal ocupa el resto del espacio.

### Rolling Mean como overlay

La Rolling Mean se renderiza como `LineSeries` en el mismo pane que el candlestick. Comparte el price scale del candlestick. Se puede ocultar/mostrar vía `featureSeries.applyOptions({ visible: false })`.

### Error handling

- Si el backend no tiene datos para un symbol/timeframe, el endpoint devuelve arrays vacíos (no errores HTTP).
- Si FastAPI no puede conectar a SQLite, devuelve HTTP 500 con mensaje descriptivo.
- El frontend muestra un aviso en el DOM si los arrays de datos están vacíos.
