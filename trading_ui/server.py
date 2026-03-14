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
from pathlib import Path
from typing import Any

from fastapi import FastAPI, Query
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles

from data_store.core import DataStoreCore
from data_store.market_repo import load_market_data
from market_feed.timeframes import _ALLOWED as _VALID_TIMEFRAMES

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


def _format_display_param(value: str) -> str:
    return value.replace("_", ".")


def _build_indicator_catalog(feature_cols: list[str]) -> list[dict[str, Any]]:
    indicators: list[dict[str, Any]] = []
    consumed: set[str] = set()
    middle_by_period: dict[tuple[str, str], str] = {}
    bands: dict[tuple[str, str, str], dict[str, str]] = {}
    macd_parts: dict[tuple[str, str, str, str, str], dict[str, str]] = {}
    adx_parts: dict[tuple[str, str], dict[str, str]] = {}

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
):
    """Load OHLCV + volume from data_store, formatted for LWC."""
    conn = _get_store().get_connection()
    try:
        df = load_market_data(conn, symbol, timeframe)
    finally:
        conn.close()

    if df.empty:
        return {"symbol": symbol, "timeframe": timeframe, "candles": [], "volume": []}

    candles = []
    volume = []

    for ts in df.index:
        row = df.loc[ts]
        t = _ts_to_unix(ts)

        candles.append({
            "time": t,
            "open": float(row["open"]),
            "high": float(row["high"]),
            "low": float(row["low"]),
            "close": float(row["close"]),
        })
        volume.append({
            "time": t,
            "value": float(row["volume"]),
        })

    return {
        "symbol": symbol,
        "timeframe": timeframe,
        "candles": candles,
        "volume": volume,
    }


@app.get("/api/available-features")
async def get_available_features(
    symbol: str = Query(..., description="Ticker symbol"),
    timeframe: str = Query(..., description="Timeframe"),
):
    """List feature keys available for a symbol/timeframe pair."""
    conn = _get_store().get_connection()
    try:
        df = load_market_data(conn, symbol, timeframe)
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
):
    """List renderable indicators for a symbol/timeframe pair."""
    conn = _get_store().get_connection()
    try:
        df = load_market_data(conn, symbol, timeframe)
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
):
    """Load a specific feature series, omitting NaN values."""
    conn = _get_store().get_connection()
    try:
        df = load_market_data(conn, symbol, timeframe)
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
):
    """Load a grouped indicator definition with one or more renderable series."""
    conn = _get_store().get_connection()
    try:
        df = load_market_data(conn, symbol, timeframe)
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
