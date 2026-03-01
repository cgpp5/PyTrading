"""trading_ui.server — FastAPI backend for TradingUI.

Exposes REST endpoints that read from data_store and serve data
formatted for Lightweight Charts.  Also serves the static frontend.

Usage:
    uvicorn trading_ui.server:app --reload
"""

from __future__ import annotations

import math
import os
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

    feature_cols = sorted(c for c in df.columns if "@" in c)
    return {"features": feature_cols}


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
