"""trading_ui.server — FastAPI backend for TradingUI.

Exposes REST endpoints that read from data_store and serve data
formatted for Lightweight Charts.  Also serves the static frontend.

Usage:
    uvicorn trading_ui.server:app --reload
"""

from __future__ import annotations

import math
import os
import re
from datetime import datetime, timedelta, timezone
from pathlib import Path
from typing import Any

from fastapi import FastAPI, Query
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles

from starlette.concurrency import run_in_threadpool

from data_store.core import DataStoreCore
from data_store.market_repo import load_market_data
from data_store.state_repo import load_state, save_state
from market_feed.timeframes import _ALLOWED as _VALID_TIMEFRAMES
from trading_ui import ingest

# ---------------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------------

_DB_PATH = os.environ.get("TRADING_UI_DB", "trading_data.sqlite")
_FRONTEND_DIR = Path(__file__).resolve().parent.parent / "frontend"
_BASE_COLUMNS = {
    "open",
    "high",
    "low",
    "close",
    "volume",
    "source",
    "quality",
    "is_gap",
    "latency_sec",
}
_BOLLINGER_MIDDLE_RE = re.compile(
    r"^bollinger_middle_(?P<period>\d+)@(?P<version>[A-Za-z0-9._-]+)$"
)
_BOLLINGER_UPPER_RE = re.compile(
    r"^bollinger_upper_(?P<period>\d+)_(?P<deviation>[0-9_]+)@(?P<version>[A-Za-z0-9._-]+)$"
)
_BOLLINGER_LOWER_RE = re.compile(
    r"^bollinger_lower_(?P<period>\d+)_(?P<deviation>[0-9_]+)@(?P<version>[A-Za-z0-9._-]+)$"
)
_MACD_LINE_RE = re.compile(
    r"^macd_line_(?P<fast>\d+)_(?P<slow>\d+)_(?P<signal>\d+)_(?P<column>[A-Za-z0-9_]+)@(?P<version>[A-Za-z0-9._-]+)$"
)
_MACD_SIGNAL_RE = re.compile(
    r"^macd_signal_(?P<fast>\d+)_(?P<slow>\d+)_(?P<signal>\d+)_(?P<column>[A-Za-z0-9_]+)@(?P<version>[A-Za-z0-9._-]+)$"
)
_MACD_HISTOGRAM_RE = re.compile(
    r"^macd_histogram_(?P<fast>\d+)_(?P<slow>\d+)_(?P<signal>\d+)_(?P<column>[A-Za-z0-9_]+)@(?P<version>[A-Za-z0-9._-]+)$"
)
_ATR_RE = re.compile(
    r"^atr_(?P<period>\d+)@(?P<version>[A-Za-z0-9._-]+)$"
)
_SMA_OSC_RE = re.compile(
    r"^sma_osc_(?P<period>\d+)@(?P<version>[A-Za-z0-9._-]+)$"
)
_ADX_RE = re.compile(
    r"^adx_(?P<period>\d+)@(?P<version>[A-Za-z0-9._-]+)$"
)
_PLUS_DI_RE = re.compile(
    r"^plus_di_(?P<period>\d+)@(?P<version>[A-Za-z0-9._-]+)$"
)
_MINUS_DI_RE = re.compile(
    r"^minus_di_(?P<period>\d+)@(?P<version>[A-Za-z0-9._-]+)$"
)
_MOGALEF_MIDDLE_RE = re.compile(
    r"^mogalef_middle_(?P<n>\d+)_(?P<et>\d+)_(?P<coef>[0-9_]+)@(?P<version>[A-Za-z0-9._-]+)$"
)
_MOGALEF_UPPER_RE = re.compile(
    r"^mogalef_upper_(?P<n>\d+)_(?P<et>\d+)_(?P<coef>[0-9_]+)@(?P<version>[A-Za-z0-9._-]+)$"
)
_MOGALEF_LOWER_RE = re.compile(
    r"^mogalef_lower_(?P<n>\d+)_(?P<et>\d+)_(?P<coef>[0-9_]+)@(?P<version>[A-Za-z0-9._-]+)$"
)

# Scalar features that are NOT price overlays. They carry their own scale
# (oscillator / summation values) and must render in a dedicated sub-pane
# instead of being drawn on top of the price chart.
_SEPARATE_SCALAR_FEATURES: dict[str, str] = {
    "mcclellan_oscillator": "McClellan Oscillator",
    "mcclellan_summation": "McClellan Summation",
}

# ---------------------------------------------------------------------------
# Application
# ---------------------------------------------------------------------------

app = FastAPI(title="TradingUI")

# DataStoreCore — lazy singleton (overridable for testing)
_store: DataStoreCore | None = None


def _get_store() -> DataStoreCore:
    global _store
    if _store is None:
        _store = DataStoreCore(_DB_PATH)
    return _store


def set_store(store: DataStoreCore) -> None:
    """Override the DataStoreCore instance (used by tests)."""
    global _store
    _store = store


async def _ensure_data(
    symbol: str, timeframe: str, days: int | None = None
) -> dict[str, Any]:
    """Asegura datos frescos para ``(symbol, timeframe)``.

    Si el par aún no está en ``data_store`` (o su cobertura es menor que
    ``days`` días), lo descarga del proveedor, calcula las features y lo
    persiste — en un hilo para no bloquear el event loop.  Devuelve un dict
    de estado de la ingesta para que los endpoints puedan informar al cliente
    si el ticker no existe (``no_data``) o si la descarga falló (``error``).
    """
    store = _get_store()
    try:
        return await run_in_threadpool(
            ingest.ensure_symbol_data, store, symbol, timeframe, days=days
        )
    except Exception as exc:  # noqa: BLE001
        # Fallo de descarga → servimos lo cacheado (o vacío) e informamos.
        return {"action": "error", "error": str(exc)}


def _ingest_status(result: dict[str, Any] | None, symbol: str, has_data: bool) -> dict[str, Any]:
    """Traduce el resultado de la ingesta a un ``status``/``message`` de API.

    - Si hay velas → ``ok``.
    - Si no hay velas y la ingesta reportó ``no_data`` → ``no_data``.
    - Si la ingesta falló (``error``) → ``error`` (red / símbolo no válido).
    - Si no hay velas pero la ingesta no lo aclaró → ``empty``.
    """
    action = (result or {}).get("action")

    if has_data:
        return {"status": "ok", "message": None}

    if action == "no_data":
        return {
            "status": "no_data",
            "message": f"No data for {symbol}. The ticker may not exist or the provider has no data for the requested range.",
        }
    if action == "error":
        return {
            "status": "error",
            "message": f"Could not load {symbol}: {result.get('error')}",
        }
    return {
        "status": "empty",
        "message": f"No cached data for {symbol} and it could not be downloaded.",
    }


# Mount static files only if the frontend directory exists (won't exist
# during unit tests that don't create it).
if _FRONTEND_DIR.is_dir():
    app.mount("/static", StaticFiles(directory=str(_FRONTEND_DIR)), name="static")


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def _ts_to_unix(idx_val) -> int:
    """Convert a pandas Timestamp to UNIX seconds (int)."""
    return int(idx_val.timestamp())


def _safe_float(val: Any) -> float | None:
    """Return a plain float, or None for NaN/None."""
    if val is None:
        return None
    try:
        if math.isnan(val):
            return None
    except (TypeError, ValueError):
        pass
    return float(val)


def _feature_columns(df) -> list[str]:
    return sorted(c for c in df.columns if c not in _BASE_COLUMNS)


def _load_window(conn, symbol: str, timeframe: str, days: int | None = None):
    """Carga OHLCV acotado a los últimos ``days`` días (si se indica)."""
    start = None
    if days is not None:
        start = (datetime.now(timezone.utc) - timedelta(days=days)).isoformat()
    return load_market_data(conn, symbol, timeframe, start=start)


def _format_display_param(value: str) -> str:
    return value.replace("_", ".")


def _build_indicator_catalog(feature_cols: list[str]) -> list[dict[str, Any]]:
    indicators: list[dict[str, Any]] = []
    consumed: set[str] = set()
    middle_by_period: dict[tuple[str, str], str] = {}
    bands: dict[tuple[str, str, str], dict[str, str]] = {}
    macd_parts: dict[tuple[str, str, str, str, str], dict[str, str]] = {}
    adx_parts: dict[tuple[str, str], dict[str, str]] = {}
    mogalef_bands: dict[tuple[str, str, str, str], dict[str, str]] = {}

    for col in feature_cols:
        middle_match = _BOLLINGER_MIDDLE_RE.fullmatch(col)
        if middle_match:
            middle_by_period[(middle_match.group("period"), middle_match.group("version"))] = col
            continue

        upper_match = _BOLLINGER_UPPER_RE.fullmatch(col)
        if upper_match:
            key = (
                upper_match.group("period"),
                upper_match.group("deviation"),
                upper_match.group("version"),
            )
            bands.setdefault(key, {})["upper"] = col
            continue

        lower_match = _BOLLINGER_LOWER_RE.fullmatch(col)
        if lower_match:
            key = (
                lower_match.group("period"),
                lower_match.group("deviation"),
                lower_match.group("version"),
            )
            bands.setdefault(key, {})["lower"] = col
            continue

        macd_line_match = _MACD_LINE_RE.fullmatch(col)
        if macd_line_match:
            key = (
                macd_line_match.group("fast"),
                macd_line_match.group("slow"),
                macd_line_match.group("signal"),
                macd_line_match.group("column"),
                macd_line_match.group("version"),
            )
            macd_parts.setdefault(key, {})["line"] = col
            continue

        macd_signal_match = _MACD_SIGNAL_RE.fullmatch(col)
        if macd_signal_match:
            key = (
                macd_signal_match.group("fast"),
                macd_signal_match.group("slow"),
                macd_signal_match.group("signal"),
                macd_signal_match.group("column"),
                macd_signal_match.group("version"),
            )
            macd_parts.setdefault(key, {})["signal"] = col
            continue

        macd_histogram_match = _MACD_HISTOGRAM_RE.fullmatch(col)
        if macd_histogram_match:
            key = (
                macd_histogram_match.group("fast"),
                macd_histogram_match.group("slow"),
                macd_histogram_match.group("signal"),
                macd_histogram_match.group("column"),
                macd_histogram_match.group("version"),
            )
            macd_parts.setdefault(key, {})["histogram"] = col
            continue

        atr_match = _ATR_RE.fullmatch(col)
        if atr_match:
            consumed.add(col)
            indicators.append({
                "key": col,
                "name": f"ATR ({atr_match.group('period')})",
                "kind": "atr",
                "overlay": False,
                "pane": "separate",
                "series": [
                    {
                        "key": col,
                        "label": "ATR",
                        "color": "#fab387",
                        "lineWidth": 2,
                        "seriesType": "line",
                    }
                ],
            })
            continue

        sma_osc_match = _SMA_OSC_RE.fullmatch(col)
        if sma_osc_match:
            consumed.add(col)
            indicators.append({
                "key": col,
                "name": f"SMA Osc ({sma_osc_match.group('period')})",
                "kind": "sma_osc",
                "overlay": False,
                "pane": "separate",
                "series": [
                    {
                        "key": col,
                        "label": "SMA Osc",
                        "color": "#cba6f7",
                        "lineWidth": 2,
                        "seriesType": "line",
                        "valueFormat": "percent",
                    }
                ],
            })
            continue

        adx_match = _ADX_RE.fullmatch(col)
        if adx_match:
            key = (adx_match.group("period"), adx_match.group("version"))
            adx_parts.setdefault(key, {})["adx"] = col
            continue

        plus_di_match = _PLUS_DI_RE.fullmatch(col)
        if plus_di_match:
            key = (plus_di_match.group("period"), plus_di_match.group("version"))
            adx_parts.setdefault(key, {})["plus_di"] = col
            continue

        minus_di_match = _MINUS_DI_RE.fullmatch(col)
        if minus_di_match:
            key = (minus_di_match.group("period"), minus_di_match.group("version"))
            adx_parts.setdefault(key, {})["minus_di"] = col
            continue

        mogalef_middle_match = _MOGALEF_MIDDLE_RE.fullmatch(col)
        if mogalef_middle_match:
            key = (
                mogalef_middle_match.group("n"),
                mogalef_middle_match.group("et"),
                mogalef_middle_match.group("coef"),
                mogalef_middle_match.group("version"),
            )
            mogalef_bands.setdefault(key, {})["middle"] = col
            continue

        mogalef_upper_match = _MOGALEF_UPPER_RE.fullmatch(col)
        if mogalef_upper_match:
            key = (
                mogalef_upper_match.group("n"),
                mogalef_upper_match.group("et"),
                mogalef_upper_match.group("coef"),
                mogalef_upper_match.group("version"),
            )
            mogalef_bands.setdefault(key, {})["upper"] = col
            continue

        mogalef_lower_match = _MOGALEF_LOWER_RE.fullmatch(col)
        if mogalef_lower_match:
            key = (
                mogalef_lower_match.group("n"),
                mogalef_lower_match.group("et"),
                mogalef_lower_match.group("coef"),
                mogalef_lower_match.group("version"),
            )
            mogalef_bands.setdefault(key, {})["lower"] = col
            continue

        if col in _SEPARATE_SCALAR_FEATURES:
            consumed.add(col)
            indicators.append({
                "key": col,
                "name": _SEPARATE_SCALAR_FEATURES[col],
                "kind": "scalar",
                "overlay": False,
                "pane": "separate",
                "series": [
                    {
                        "key": col,
                        "label": _SEPARATE_SCALAR_FEATURES[col],
                        "color": "#94e2d5",
                        "lineWidth": 2,
                        "seriesType": "line",
                    }
                ],
            })
            continue
    for (period, deviation, version), parts in sorted(bands.items()):
        middle = middle_by_period.get((period, version))
        upper = parts.get("upper")
        lower = parts.get("lower")
        if not (middle and upper and lower):
            continue

        consumed.update({middle, upper, lower})
        indicators.append({
            "key": f"bollinger_bands_{period}_{deviation}@{version}",
            "name": f"Bollinger Bands ({period}, {_format_display_param(deviation)})",
            "kind": "bollinger_bands",
            "overlay": True,
            "pane": "overlay",
            "series": [
                {
                    "key": middle,
                    "label": "Middle",
                    "color": "#f9e2af",
                    "lineWidth": 2,
                    "seriesType": "line",
                },
                {
                    "key": upper,
                    "label": "Upper",
                    "color": "#f38ba8",
                    "lineWidth": 2,
                    "seriesType": "line",
                },
                {
                    "key": lower,
                    "label": "Lower",
                    "color": "#89b4fa",
                    "lineWidth": 2,
                    "seriesType": "line",
                },
            ],
        })

    for (n, et, coef, version), parts in sorted(mogalef_bands.items()):
        middle = parts.get("middle")
        upper = parts.get("upper")
        lower = parts.get("lower")
        if not (middle and upper and lower):
            continue

        consumed.update({middle, upper, lower})
        indicators.append({
            "key": f"mogalef_bands_{n}_{et}_{coef}@{version}",
            "name": (
                f"Mogalef Bands ({n}, {et}, {_format_display_param(coef)})"
            ),
            "kind": "mogalef_bands",
            "overlay": True,
            "pane": "overlay",
            "series": [
                {
                    "key": middle,
                    "label": "Middle",
                    "color": "#f9e2af",
                    "lineWidth": 1,
                    "lineStyle": "dotted",
                    "seriesType": "line",
                },
                {
                    "key": upper,
                    "label": "Upper",
                    "color": "#f38ba8",
                    "lineWidth": 1,
                    "seriesType": "line",
                },
                {
                    "key": lower,
                    "label": "Lower",
                    "color": "#89b4fa",
                    "lineWidth": 1,
                    "seriesType": "line",
                },
            ],
        })

    for (fast, slow, signal, column, version), parts in sorted(macd_parts.items()):
        line = parts.get("line")
        signal_col = parts.get("signal")
        histogram = parts.get("histogram")
        if not (line and signal_col and histogram):
            continue

        consumed.update({line, signal_col, histogram})
        indicators.append({
            "key": f"macd_{fast}_{slow}_{signal}_{column}@{version}",
            "name": f"MACD ({fast}, {slow}, {signal})",
            "kind": "macd",
            "overlay": False,
            "pane": "separate",
            "series": [
                {
                    "key": line,
                    "label": "MACD",
                    "color": "#f9e2af",
                    "lineWidth": 2,
                    "seriesType": "line",
                },
                {
                    "key": signal_col,
                    "label": "Signal",
                    "color": "#89b4fa",
                    "lineWidth": 2,
                    "seriesType": "line",
                },
                {
                    "key": histogram,
                    "label": "Histogram",
                    "color": "#94e2d5",
                    "negativeColor": "#f38ba8",
                    "lineWidth": 1,
                    "seriesType": "histogram",
                },
            ],
        })

    for (period, version), parts in sorted(adx_parts.items()):
        adx = parts.get("adx")
        plus_di = parts.get("plus_di")
        minus_di = parts.get("minus_di")
        if not (adx and plus_di and minus_di):
            continue

        consumed.update({adx, plus_di, minus_di})
        indicators.append({
            "key": f"adx_family_{period}@{version}",
            "name": f"ADX ({period})",
            "kind": "adx",
            "overlay": False,
            "pane": "separate",
            "series": [
                {
                    "key": adx,
                    "label": "ADX",
                    "color": "#f9e2af",
                    "lineWidth": 2,
                    "seriesType": "line",
                },
                {
                    "key": plus_di,
                    "label": "+DI",
                    "color": "#a6e3a1",
                    "lineWidth": 2,
                    "seriesType": "line",
                },
                {
                    "key": minus_di,
                    "label": "-DI",
                    "color": "#f38ba8",
                    "lineWidth": 2,
                    "seriesType": "line",
                },
            ],
        })

    for col in feature_cols:
        if col in consumed:
            continue
        indicators.append({
            "key": col,
            "name": col,
            "kind": "scalar",
            "overlay": True,
            "pane": "overlay",
            "series": [
                {
                    "key": col,
                    "label": col,
                    "color": "#fab387",
                    "lineWidth": 2,
                    "seriesType": "line",
                }
            ],
        })

    indicators.sort(key=lambda item: item["name"].lower())
    return indicators


def _find_indicator(indicators: list[dict[str, Any]], key: str) -> dict[str, Any] | None:
    for indicator in indicators:
        if indicator["key"] == key:
            return indicator
    return None


# ---------------------------------------------------------------------------
# Routes
# ---------------------------------------------------------------------------

@app.get("/")
async def index():
    """Serve the frontend SPA."""
    html_path = _FRONTEND_DIR / "index.html"
    return FileResponse(str(html_path))


@app.get("/api/symbols")
async def get_symbols():
    """List distinct symbols available in data_store."""
    conn = _get_store().get_connection()
    try:
        rows = conn.execute(
            "SELECT DISTINCT symbol FROM market_data ORDER BY symbol"
        ).fetchall()
        symbols = [r["symbol"] for r in rows]
    finally:
        conn.close()
    return {"symbols": symbols}


@app.get("/api/timeframes")
async def get_timeframes():
    """List valid timeframes."""
    return {"timeframes": sorted(_VALID_TIMEFRAMES)}


@app.get("/api/ohlcv")
async def get_ohlcv(
    symbol: str = Query(..., description="Ticker symbol"),
    timeframe: str = Query(..., description="Timeframe (e.g. 1d)"),
    days: int | None = Query(None, description="History lookback in days"),
    start: str | None = Query(
        None, description="ISO date: fetch/serve history back to this day"
    ),
):
    """Load OHLCV + volume from data_store, formatted for LWC.

    ``days`` pide los últimos N días.  ``start`` (fecha ISO) pide historia
    hasta esa fecha hacia atrás — si hace falta se descarga — y devuelve
    todas las velas desde ``start`` (útil para cargar más histórico al
    hacer pan/scroll a la izquierda).
    """
    start_dt: datetime | None = None
    if start is not None:
        try:
            start_dt = datetime.fromisoformat(start)
        except ValueError:
            start_dt = None
        if start_dt is not None and start_dt.tzinfo is None:
            start_dt = start_dt.replace(tzinfo=timezone.utc)

    store = _get_store()
    if start_dt is not None:
        try:
            ingest_result = await run_in_threadpool(
                ingest.ensure_history_back_to,
                store, symbol, timeframe, start_dt,
            )
        except Exception as exc:  # noqa: BLE001
            ingest_result = {"action": "error", "error": str(exc)}
    else:
        ingest_result = await _ensure_data(symbol, timeframe, days)

    conn = store.get_connection()
    try:
        if start_dt is not None:
            df = load_market_data(
                conn, symbol, timeframe, start=start_dt.isoformat()
            )
        else:
            df = _load_window(conn, symbol, timeframe, days)
    finally:
        conn.close()

    if df.empty:
        return {
            "symbol": symbol,
            "timeframe": timeframe,
            "candles": [],
            "volume": [],
            **_ingest_status(ingest_result, symbol, has_data=False),
        }

    candles = []
    volume = []

    for ts in df.index:
        row = df.loc[ts]
        t = _ts_to_unix(ts)

        open_v = _safe_float(row.get("open"))
        high_v = _safe_float(row.get("high"))
        low_v = _safe_float(row.get("low"))
        close_v = _safe_float(row.get("close"))
        vol_v = _safe_float(row.get("volume"))

        # Las filas de hueco (NaN en OHLC) son marcadores de gap, no velas
        # reales: se omiten para que LWC no reciba NaN (que JSON no serializa
        # y provocaba un error 500 al cambiar a 15m/1h).
        if open_v is None or high_v is None or low_v is None or close_v is None:
            continue

        candles.append({
            "time": t,
            "open": open_v,
            "high": high_v,
            "low": low_v,
            "close": close_v,
        })
        if vol_v is not None:
            volume.append({"time": t, "value": vol_v})

    return {
        "symbol": symbol,
        "timeframe": timeframe,
        "candles": candles,
        "volume": volume,
        **_ingest_status(ingest_result, symbol, has_data=True),
    }


@app.get("/api/available-features")
async def get_available_features(
    symbol: str = Query(..., description="Ticker symbol"),
    timeframe: str = Query(..., description="Timeframe"),
    days: int | None = Query(None, description="History lookback in days"),
):
    """List feature keys available for a symbol/timeframe pair."""
    await _ensure_data(symbol, timeframe, days)
    conn = _get_store().get_connection()
    try:
        df = _load_window(conn, symbol, timeframe, days)
    finally:
        conn.close()

    if df.empty:
        return {"features": []}

    feature_cols = _feature_columns(df)
    return {"features": feature_cols}


@app.get("/api/available-indicators")
async def get_available_indicators(
    symbol: str = Query(..., description="Ticker symbol"),
    timeframe: str = Query(..., description="Timeframe"),
    days: int | None = Query(None, description="History lookback in days"),
):
    """List renderable indicators for a symbol/timeframe pair."""
    await _ensure_data(symbol, timeframe, days)
    conn = _get_store().get_connection()
    try:
        df = _load_window(conn, symbol, timeframe, days)
    finally:
        conn.close()

    if df.empty:
        return {"indicators": []}

    return {"indicators": _build_indicator_catalog(_feature_columns(df))}


@app.get("/api/features")
async def get_features(
    symbol: str = Query(..., description="Ticker symbol"),
    timeframe: str = Query(..., description="Timeframe"),
    feature: str = Query(..., description="Feature key (e.g. sma_50@1.0)"),
    days: int | None = Query(None, description="History lookback in days"),
):
    """Load a specific feature series, omitting NaN values."""
    await _ensure_data(symbol, timeframe, days)
    conn = _get_store().get_connection()
    try:
        df = _load_window(conn, symbol, timeframe, days)
    finally:
        conn.close()

    if df.empty or feature not in df.columns:
        return {
            "symbol": symbol,
            "timeframe": timeframe,
            "feature": feature,
            "data": [],
        }

    data = []
    for ts in df.index:
        val = _safe_float(df.loc[ts, feature])
        if val is not None:
            data.append({"time": _ts_to_unix(ts), "value": val})

    return {
        "symbol": symbol,
        "timeframe": timeframe,
        "feature": feature,
        "data": data,
    }


@app.get("/api/indicator")
async def get_indicator(
    symbol: str = Query(..., description="Ticker symbol"),
    timeframe: str = Query(..., description="Timeframe"),
    indicator: str = Query(..., description="Indicator key"),
    days: int | None = Query(None, description="History lookback in days"),
):
    """Load a grouped indicator definition with one or more renderable series."""
    await _ensure_data(symbol, timeframe, days)
    conn = _get_store().get_connection()
    try:
        df = _load_window(conn, symbol, timeframe, days)
    finally:
        conn.close()

    if df.empty:
        return {
            "symbol": symbol,
            "timeframe": timeframe,
            "indicator": indicator,
            "series": [],
        }

    descriptor = _find_indicator(_build_indicator_catalog(_feature_columns(df)), indicator)
    if descriptor is None:
        return {
            "symbol": symbol,
            "timeframe": timeframe,
            "indicator": indicator,
            "series": [],
        }

    payload_series = []
    for item in descriptor["series"]:
        if item["key"] not in df.columns:
            continue

        data = []
        for ts in df.index:
            val = _safe_float(df.loc[ts, item["key"]])
            if val is not None:
                data.append({"time": _ts_to_unix(ts), "value": val})

        payload_series.append({
            "key": item["key"],
            "label": item["label"],
            "color": item["color"],
            "negativeColor": item.get("negativeColor"),
            "lineWidth": item["lineWidth"],
            "lineStyle": item.get("lineStyle"),
            "seriesType": item.get("seriesType", "line"),
            "valueFormat": item.get("valueFormat"),
            "data": data,
        })

    return {
        "symbol": symbol,
        "timeframe": timeframe,
        "indicator": descriptor["key"],
        "name": descriptor["name"],
        "kind": descriptor["kind"],
        "overlay": descriptor["overlay"],
        "pane": descriptor.get("pane", "overlay"),
        "series": payload_series,
    }


# ---------------------------------------------------------------------------
# Paso 5 — Historial de trading, posiciones y métricas operativas
# ---------------------------------------------------------------------------
#
# El estado se persiste en el KV store de DataStore (``system_state``) bajo
# claves por símbolo:
#   - ``trading_log_{symbol}``  → lista de eventos (señales / ejecuciones).
#   - ``positions_{symbol}``    → lista de posiciones abiertas.
#
# Las métricas operativas (TOTAL P/L, Open Positions) se derivan de las
# posiciones abiertas y del último cierre disponible en ``market_data``.

from pydantic import BaseModel, Field  # noqa: E402


def _log_key(symbol: str) -> str:
    return f"trading_log_{symbol}"


def _positions_key(symbol: str) -> str:
    return f"positions_{symbol}"


def _latest_close(symbol: str) -> float | None:
    """Último cierre disponible para el símbolo (cualquier timeframe)."""
    conn = _get_store().get_connection()
    try:
        timeframes = [
            r["timeframe"]
            for r in conn.execute(
                "SELECT DISTINCT timeframe FROM market_data WHERE symbol = ?",
                (symbol,),
            ).fetchall()
        ]
        best: float | None = None
        best_ts = None
        for tf in timeframes:
            df = load_market_data(conn, symbol, tf)
            if df.empty:
                continue
            ts = df.index[-1]
            close = _safe_float(df["close"].iloc[-1])
            if close is None:
                continue
            if best_ts is None or ts > best_ts:
                best_ts = ts
                best = close
        return best
    finally:
        conn.close()


class LogEvent(BaseModel):
    """Evento del log de trading (señal o ejecución)."""

    symbol: str
    type: str = Field(description="signal | execution")
    strategy: str | None = None
    action: str | None = None
    timestamp: str | None = None
    detail: dict[str, Any] = Field(default_factory=dict)


class Position(BaseModel):
    """Posición abierta."""

    id: str
    symbol: str
    side: str = Field(description="long | short")
    qty: float
    entry_price: float
    opened_at: str | None = None
    strategy: str | None = None


def _compute_total_pl(positions: list[dict[str, Any]], last_close: float | None) -> float:
    """P/L no realizado de las posiciones abiertas contra el último cierre."""
    if last_close is None:
        return 0.0
    total = 0.0
    for pos in positions:
        qty = float(pos.get("qty", 0.0))
        entry = float(pos.get("entry_price", 0.0))
        side = pos.get("side", "long")
        if side == "short":
            total += (entry - last_close) * qty
        else:
            total += (last_close - entry) * qty
    return total


@app.get("/api/trading-log")
async def get_trading_log(symbol: str = Query(..., description="Ticker symbol")):
    """Devuelve el log de trading (señales y ejecuciones) de un símbolo."""
    conn = _get_store().get_connection()
    try:
        events = load_state(conn, _log_key(symbol)) or []
    finally:
        conn.close()
    return {"symbol": symbol, "events": events}


@app.post("/api/trading-log")
async def append_trading_log(event: LogEvent):
    """Añade un evento al log de trading de un símbolo."""
    conn = _get_store().get_connection()
    try:
        events = load_state(conn, _log_key(event.symbol)) or []
        events.append(event.model_dump())
        save_state(conn, _log_key(event.symbol), events)
    finally:
        conn.close()
    return {"symbol": event.symbol, "count": len(events)}


@app.get("/api/positions")
async def get_positions(symbol: str = Query(..., description="Ticker symbol")):
    """Devuelve las posiciones abiertas y las métricas operativas."""
    conn = _get_store().get_connection()
    try:
        positions = load_state(conn, _positions_key(symbol)) or []
    finally:
        conn.close()

    last_close = _latest_close(symbol)
    total_pl = _compute_total_pl(positions, last_close)

    return {
        "symbol": symbol,
        "positions": positions,
        "open_positions": len(positions),
        "total_pl": total_pl,
        "last_close": last_close,
    }


@app.post("/api/positions")
async def upsert_position(position: Position):
    """Crea o actualiza una posición abierta (por ``id``)."""
    conn = _get_store().get_connection()
    try:
        positions = load_state(conn, _positions_key(position.symbol)) or []
        payload = position.model_dump()
        existing_ids = {p.get("id") for p in positions}
        if position.id in existing_ids:
            positions = [
                payload if p.get("id") == position.id else p for p in positions
            ]
        else:
            positions.append(payload)
        save_state(conn, _positions_key(position.symbol), positions)
    finally:
        conn.close()
    return {"symbol": position.symbol, "count": len(positions)}


@app.delete("/api/positions/{position_id}")
async def close_position(
    position_id: str,
    symbol: str = Query(..., description="Ticker symbol"),
):
    """Cierra (elimina) una posición abierta por ``id``."""
    conn = _get_store().get_connection()
    try:
        positions = load_state(conn, _positions_key(symbol)) or []
        remaining = [p for p in positions if p.get("id") != position_id]
        save_state(conn, _positions_key(symbol), remaining)
    finally:
        conn.close()
    return {"symbol": symbol, "count": len(remaining)}
