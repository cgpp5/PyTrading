"""Unified visual test: seed AAPL/1d with ALL primitives, launch server, open browser.

Usage:
    python -m trading_ui.visual_test
"""

from __future__ import annotations

import math
import os
import tempfile
import threading
import webbrowser
from datetime import datetime, timedelta, timezone

from data_store.core import DataStoreCore
from data_store.market_repo import save_features, save_market_data, save_request_meta
from market_feed.calendar import MarketCalendarResolver
from market_feed.market_feed import MarketFeed, ProviderTier
from market_feed.observability import InMemoryObservability
from market_feed.providers.yfinance import YFinanceProvider

from feature_engine.composition.adx import (
    AverageDirectionalIndex,
    MinusDirectionalIndex,
    PlusDirectionalIndex,
)
from feature_engine.composition.atr import AverageTrueRange
from feature_engine.composition.bollinger import (
    BollingerBandWidth,
    BollingerLowerBand,
    BollingerMiddleBand,
    BollingerUpperBand,
)
from feature_engine.composition.macd import MACDHistogram, MACDLine, MACDSignal
from feature_engine.composition.sma_osc import SMAOscillator
from feature_engine.errors import ComputationError
from feature_engine.primitives.external import McClellanOscillator, McClellanSummation
from feature_engine.primitives.returns import SimpleReturns, LogReturns
from feature_engine.primitives.rolling import RollingMean, RollingStd
from feature_engine.primitives.volatility import TrueRange
from feature_engine.primitives.volume import VolumeZScore
from feature_engine.primitives.rsi import RSI

SYMBOL = "AAPL"
TIMEFRAME = "1d"
DAYS = 365


def _build_primitives():
    """Return all implemented primitives with sensible defaults."""
    return [
        SimpleReturns(timeframe=TIMEFRAME),
        LogReturns(timeframe=TIMEFRAME),
        RollingMean(window=20, timeframe=TIMEFRAME),
        RollingMean(window=50, timeframe=TIMEFRAME),
        RollingStd(window=20, timeframe=TIMEFRAME),
        BollingerMiddleBand(period=20, timeframe=TIMEFRAME),
        BollingerUpperBand(period=20, timeframe=TIMEFRAME),
        BollingerLowerBand(period=20, timeframe=TIMEFRAME),
        BollingerBandWidth(period=20, timeframe=TIMEFRAME),
        AverageTrueRange(period=14, timeframe=TIMEFRAME),
        PlusDirectionalIndex(period=14, timeframe=TIMEFRAME),
        MinusDirectionalIndex(period=14, timeframe=TIMEFRAME),
        AverageDirectionalIndex(period=14, timeframe=TIMEFRAME),
        MACDLine(timeframe=TIMEFRAME),
        MACDSignal(timeframe=TIMEFRAME),
        MACDHistogram(timeframe=TIMEFRAME),
        SMAOscillator(period=20, timeframe=TIMEFRAME),
        TrueRange(timeframe=TIMEFRAME),
        VolumeZScore(window=20, timeframe=TIMEFRAME),
        RSI(period=14, timeframe=TIMEFRAME),
        McClellanOscillator(timeframe=TIMEFRAME),
        McClellanSummation(timeframe=TIMEFRAME),
    ]


def _feature_storage_key(feature) -> str:
    storage_key = getattr(feature, "storage_key", None)
    if isinstance(storage_key, str):
        return storage_key
    spec = feature.spec
    return f"{spec.name}@{spec.version}"


def _seed(db_path: str) -> None:
    """Download AAPL, compute all primitives, persist to db_path."""
    obs = InMemoryObservability()
    cal = MarketCalendarResolver({SYMBOL: "NYSE"}, obs)
    tiers = [ProviderTier(provider=YFinanceProvider(), quality="degraded")]
    feed = MarketFeed(tiers=tiers, calendar_resolver=cal, observability=obs)

    end = datetime.now(timezone.utc)
    start = end - timedelta(days=DAYS)

    print(f"[1/3] Descargando {SYMBOL} {TIMEFRAME} ({DAYS} días)...")
    md = feed.get_ohlcv(SYMBOL, TIMEFRAME, start, end)
    if md.df.empty:
        print("ERROR: No se obtuvieron datos. Abortando.")
        return

    print(f"      {len(md.df)} velas descargadas")

    store = DataStoreCore(db_path)
    conn = store.get_connection()

    rows = save_market_data(conn, SYMBOL, TIMEFRAME, md.df)
    print(f"      {rows} filas guardadas en data_store")

    meta_dict = {
        "provider_used": md.meta.provider_used,
        "fallback_used": md.meta.fallback_used,
        "start": md.meta.start.isoformat(),
        "end": md.meta.end.isoformat(),
        "coverage_ratio": md.meta.coverage_ratio,
        "gap_count": md.meta.gap_count,
        "quality": md.meta.quality,
        "notes": md.meta.notes,
    }
    save_request_meta(conn, SYMBOL, TIMEFRAME, meta_dict)

    # --- Compute and persist ALL primitives ---
    print(f"[2/3] Calculando features...")
    primitives = _build_primitives()

    # Accumulate all features per timestamp, then write once to avoid
    # save_features overwriting the JSON on each call.
    features_by_ts: dict[str, dict] = {}

    for prim in primitives:
        spec = prim.spec
        feature_key = _feature_storage_key(prim)
        try:
            series = prim.compute(md.df)
        except ComputationError as exc:
            print(f"      {spec.name}: omitida ({exc})")
            continue

        count_valid = 0
        for ts, value in series.items():
            ts_iso = ts.isoformat()
            is_nan = value is None or (isinstance(value, float) and math.isnan(value))
            if is_nan:
                quality = "warmup" if "@" in feature_key else "missing"
                entry = {"value": None, "quality": quality}
            else:
                entry = {"value": float(value), "quality": "ready"}
                count_valid += 1

            features_by_ts.setdefault(ts_iso, {})[feature_key] = entry

        print(f"      {feature_key}: {count_valid} valores válidos / {len(series)} total")

    # Write all features in a single pass
    for ts_iso, feat_dict in features_by_ts.items():
        save_features(conn, SYMBOL, TIMEFRAME, ts_iso, feat_dict)

    conn.close()
    print()


def main() -> None:
    # Use a temp file so we don't pollute the workspace
    db_fd, db_path = tempfile.mkstemp(suffix=".sqlite", prefix="visual_test_")
    os.close(db_fd)

    print(f"=== Visual Test: {SYMBOL}/{TIMEFRAME} con todas las primitivas ===")
    print(f"DB temporal: {db_path}")
    print()

    _seed(db_path)

    # Point the server at our temp DB
    os.environ["TRADING_UI_DB"] = db_path

    # Reset the server's lazy singleton so it picks up our DB
    import trading_ui.server as srv
    srv._store = None

    print(f"[3/3] Lanzando servidor en http://localhost:8000 ...")
    print(f"      Ctrl+C para detener")
    print()

    # Open browser after a short delay
    def _open_browser():
        import time
        time.sleep(1.5)
        webbrowser.open("http://localhost:8000")

    threading.Thread(target=_open_browser, daemon=True).start()

    import uvicorn
    uvicorn.run(srv.app, host="127.0.0.1", port=8000, log_level="warning")


if __name__ == "__main__":
    main()
