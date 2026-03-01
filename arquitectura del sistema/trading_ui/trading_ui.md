# trading_ui — Plan de desarrollo

## Visión general

4 pasos incrementales. Cada paso produce código funcional con tests o validación manual. El paso 0 establece la infraestructura de datos; los pasos 1-3 construyen el servidor y el frontend progresivamente.

**Prerequisito:** Los módulos market_feed, feature_engine y data_store deben estar completos y con todos los tests pasando (132 tests).

---

## Paso 0 — Seed script y dependencias (`seed.py`)

**Objetivo:** Poblar data_store con datos reales para que trading_ui tenga algo que mostrar. Instalar las dependencias nuevas (fastapi, uvicorn).

**Implementación:**

- Añadir `fastapi` y `uvicorn[standard]` a `pyproject.toml` como dependencias.
- `trading_ui/seed.py` — script ejecutable que:
  1. Instancia `DataStoreCore("trading_data.sqlite")`.
  2. Instancia `MarketFeed` con la cadena de fallback completa (Alpaca → Tiingo → yfinance).
  3. Para una lista configurable de símbolos (default: `["AAPL", "SPY"]`) y timeframe `"1d"`:
     - Llama a `get_ohlcv(symbol, "1d", start, end)`.
     - Guarda en data_store via `save_market_data()` y `save_request_meta()`.
  4. Calcula features con feature_engine:
     - `RollingMean(window=50, timeframe="1d")` → guarda via `save_features()` para cada fila.
  5. Imprime un resumen: símbolo, filas guardadas, features inyectados.

**Validación:**

1. Ejecutar `python -m trading_ui.seed`.
2. Verificar que `trading_data.sqlite` contiene filas en `market_data`.
3. Verificar que al menos algunas filas tienen la columna `features` con JSON no-NULL.

---

## Paso 1 — Backend FastAPI (`server.py`)

**Objetivo:** Servidor que expone los endpoints REST documentados en el Módulo TradingUI.md. Sirve archivos estáticos del frontend.

**Implementación:**

- `trading_ui/__init__.py` — vacío.
- `trading_ui/server.py`:
  - `app = FastAPI(title="TradingUI")`.
  - Montar archivos estáticos: `app.mount("/static", StaticFiles(directory="frontend"), name="static")`.
  - `GET /` → `FileResponse("frontend/index.html")`.
  - `DataStoreCore` instanciado a nivel de módulo con `db_path` configurable (default `"trading_data.sqlite"`).
  - Endpoints:
    - `GET /api/symbols` → query `SELECT DISTINCT symbol FROM market_data`.
    - `GET /api/timeframes` → devuelve `["15m", "1h", "4h", "1d"]` (constante de `market_feed.timeframes`).
    - `GET /api/ohlcv?symbol=X&timeframe=Y` → `load_market_data(conn, symbol, timeframe)`, transforma a formato LWC:
      ```python
      candles = [
          {"time": int(row.Index.timestamp()), "open": row.open, ...}
          for row in df.itertuples()
      ]
      volume = [
          {"time": int(row.Index.timestamp()), "value": row.volume}
          for row in df.itertuples()
      ]
      ```
    - `GET /api/available-features?symbol=X&timeframe=Y` → inspeccionar DataFrame cargado, extraer nombres de columnas que contengan `@`.
    - `GET /api/features?symbol=X&timeframe=Y&feature=Z` → extraer la columna del feature, filtrar NaN, devolver como `[{"time": ..., "value": ...}]`.

**Test (`tests/test_trading_ui_api.py`):**

1. Crear data_store en `:memory:`, insertar 5 velas de `TEST/1d` con `save_market_data()`.
2. Inyectar feature `sma_50@1.0` en 3 de las 5 velas con `save_features()`.
3. Usar `TestClient(app)` de FastAPI:
   - `GET /api/symbols` → `{"symbols": ["TEST"]}`.
   - `GET /api/timeframes` → `{"timeframes": [...]}` con 4 elementos.
   - `GET /api/ohlcv?symbol=TEST&timeframe=1d` → `candles` tiene 5 elementos, cada uno con `time` (int), `open`, `high`, `low`, `close`. `volume` tiene 5 elementos.
   - `GET /api/available-features?symbol=TEST&timeframe=1d` → `{"features": ["sma_50@1.0"]}`.
   - `GET /api/features?symbol=TEST&timeframe=1d&feature=sma_50@1.0` → `data` tiene 3 elementos (los que tienen feature, no NaN).
   - `GET /api/ohlcv?symbol=NONEXIST&timeframe=1d` → `candles: [], volume: []` (no error HTTP).

---

## Paso 2 — Frontend: Chart básico (`index.html`, `app.js`, `style.css`)

**Objetivo:** SPA mínimo que renderiza candlestick + volumen con datos del backend.

**Implementación:**

- `frontend/index.html`:
  - `<script>` tag para Lightweight Charts vía CDN (`unpkg.com/lightweight-charts@5.0.1/dist/lightweight-charts.standalone.production.mjs`).
  - Dropdowns: `<select id="symbol">`, `<select id="timeframe">`, botón `[Cargar]`.
  - Container: `<div id="chart-container">`.
  - `<script type="module" src="/static/app.js">`.

- `frontend/style.css`:
  - Dark theme base (fondo `#1e1e2e`, texto `#cdd6f4`).
  - Toolbar arriba, chart ocupa el resto de la ventana.
  - Responsive: chart se adapta al ancho de la ventana.

- `frontend/app.js`:
  - Al cargar: fetch `/api/symbols` y `/api/timeframes`, poblar dropdowns.
  - Al click `[Cargar]`:
    - fetch `/api/ohlcv?symbol=X&timeframe=Y`.
    - Crear chart con `createChart()` si no existe, o limpiar series previas.
    - `addSeries(CandlestickSeries)` → `setData(candles)`.
    - `addPane({height: 120})` → `addSeries(HistogramSeries)` → `setData(volume)`.
    - `chart.timeScale().fitContent()` para ajustar zoom.
  - Resize handler: `window.addEventListener('resize', () => chart.resize(...))`.

**Validación:**

1. Ejecutar `python -m trading_ui.seed` (o ya tener datos).
2. Ejecutar `uvicorn trading_ui.server:app --reload`.
3. Abrir `http://localhost:8000` en el navegador.
4. Seleccionar AAPL / 1d → click Cargar → ver candlestick + volumen.

---

## Paso 3 — Frontend: Overlay de features

**Objetivo:** Añadir selector de features y renderizar Rolling Mean como overlay sobre el candlestick.

**Implementación:**

- Tercer dropdown `<select id="feature">` en el toolbar.
- Al cargar OHLCV (después del fetch de candles):
  - fetch `/api/available-features?symbol=X&timeframe=Y`.
  - Poblar el dropdown de features con las opciones recibidas.
  - Añadir opción `"(ninguno)"` al inicio.
- Al seleccionar un feature:
  - fetch `/api/features?symbol=X&timeframe=Y&feature=Z`.
  - Si ya hay un featureSeries previo, removerlo (`chart.removeSeries(featureSeries)`).
  - `chart.addSeries(LineSeries, { color: '#fab387', lineWidth: 2 })` → `setData(data)`.
- Si selecciona `"(ninguno)"`, eliminar el overlay.

**Validación:**

1. Con datos seeded (AAPL + sma_50@1.0 en data_store).
2. Cargar AAPL / 1d → ver candlestick + volumen.
3. Seleccionar `sma_50@1.0` en dropdown → ver línea de media móvil superpuesta.
4. Cambiar a `(ninguno)` → la línea desaparece.
5. Cambiar de símbolo → el dropdown de features se actualiza automáticamente.

---

## Resumen de archivos a crear

| Paso | Archivo | Tipo |
|------|---------|------|
| 0 | `trading_ui/__init__.py` | Python (vacío) |
| 0 | `trading_ui/seed.py` | Python |
| 0 | `pyproject.toml` (editar) | Config |
| 1 | `trading_ui/server.py` | Python |
| 1 | `tests/test_trading_ui_api.py` | Python |
| 2 | `frontend/index.html` | HTML |
| 2 | `frontend/app.js` | JavaScript |
| 2 | `frontend/style.css` | CSS |
| 3 | `frontend/app.js` (extender) | JavaScript |
