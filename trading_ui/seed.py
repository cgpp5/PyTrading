"""trading_ui.seed — Pobla data_store con datos reales para validación visual.

Uso:
    python -m trading_ui.seed
    python -m trading_ui.seed --symbols AAPL SPY MSFT --days 365
"""

from __future__ import annotations

import argparse
import sys
from datetime import datetime, timedelta, timezone

from data_store.core import DataStoreCore
from data_store.market_repo import (
    save_features,
    save_market_data,
    save_request_meta,
)
from market_feed.calendar import MarketCalendarResolver
from market_feed.market_feed import MarketFeed, ProviderTier
from market_feed.observability import InMemoryObservability
from market_feed.providers.yfinance import YFinanceProvider
from feature_engine.primitives.rolling import RollingMean


DB_PATH = "trading_data.sqlite"
DEFAULT_SYMBOLS = ["AAPL", "SPY"]
DEFAULT_DAYS = 365
TIMEFRAME = "1d"


def _build_market_feed() -> MarketFeed:
    """Construct a MarketFeed with yfinance as the sole provider."""
    obs = InMemoryObservability()
    cal_map = {s: "NYSE" for s in DEFAULT_SYMBOLS + ["MSFT", "GOOG", "AMZN", "META", "TSLA"]}
    cal = MarketCalendarResolver(cal_map, obs)

    tiers = [
        ProviderTier(provider=YFinanceProvider(), quality="degraded"),
    ]
    return MarketFeed(tiers=tiers, calendar_resolver=cal, observability=obs)


def _seed_symbol(
    feed: MarketFeed,
    store: DataStoreCore,
    symbol: str,
    start: datetime,
    end: datetime,
) -> dict:
    """Download, compute features, and persist data for one symbol."""
    # --- 1. Descargar OHLCV ---
    print(f"  [{symbol}] Descargando OHLCV ({TIMEFRAME})...", end=" ", flush=True)
    md = feed.get_ohlcv(symbol, TIMEFRAME, start, end)

    if md.df.empty:
        print("SIN DATOS")
        return {"symbol": symbol, "rows": 0, "features": 0}

    print(f"{len(md.df)} velas")

    # --- 2. Persistir OHLCV ---
    conn = store.get_connection()
    rows = save_market_data(conn, symbol, TIMEFRAME, md.df)
    print(f"  [{symbol}] Guardadas {rows} filas en data_store")

    # --- 3. Persistir metadata ---
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
    save_request_meta(conn, symbol, TIMEFRAME, meta_dict)

    # --- 4. Calcular y persistir features ---
    sma = RollingMean(window=50, timeframe=TIMEFRAME)
    series = sma.compute(md.df)
    spec = sma.spec
    feature_key = f"{spec.name}@{spec.version}"  # "sma_50@1.0"

    features_saved = 0
    for ts, value in series.items():
        # Determinar quality según warmup
        if value is None or (hasattr(value, "__class__") and value != value):
            # NaN — periodo de warmup
            feat_dict = {
                feature_key: {"value": None, "quality": "warmup"}
            }
        else:
            feat_dict = {
                feature_key: {"value": float(value), "quality": "ready"}
            }

        ts_iso = ts.isoformat()
        save_features(conn, symbol, TIMEFRAME, ts_iso, feat_dict)
        features_saved += 1

    print(f"  [{symbol}] Inyectadas {features_saved} features ({feature_key})")
    conn.close()

    return {"symbol": symbol, "rows": rows, "features": features_saved}


def main(argv: list[str] | None = None) -> None:
    parser = argparse.ArgumentParser(description="Seed data_store for TradingUI")
    parser.add_argument(
        "--symbols",
        nargs="+",
        default=DEFAULT_SYMBOLS,
        help=f"Symbols to download (default: {DEFAULT_SYMBOLS})",
    )
    parser.add_argument(
        "--days",
        type=int,
        default=DEFAULT_DAYS,
        help=f"Number of days of history (default: {DEFAULT_DAYS})",
    )
    parser.add_argument(
        "--db",
        default=DB_PATH,
        help=f"SQLite database path (default: {DB_PATH})",
    )
    args = parser.parse_args(argv)

    end = datetime.now(timezone.utc)
    start = end - timedelta(days=args.days)

    print(f"=== Seed TradingUI ===")
    print(f"DB:     {args.db}")
    print(f"Rango:  {start.date()} → {end.date()} ({args.days} días)")
    print(f"Symbols: {args.symbols}")
    print()

    store = DataStoreCore(args.db)
    feed = _build_market_feed()

    # Asegurar que el calendar_resolver conoce todos los symbols
    for s in args.symbols:
        if s not in feed._cal._symbol_calendar_map:
            feed._cal._symbol_calendar_map[s] = "NYSE"

    results = []
    for symbol in args.symbols:
        result = _seed_symbol(feed, store, symbol, start, end)
        results.append(result)

    print()
    print("=== Resumen ===")
    for r in results:
        print(f"  {r['symbol']}: {r['rows']} filas, {r['features']} features")

    total_rows = sum(r["rows"] for r in results)
    total_feats = sum(r["features"] for r in results)
    print(f"  TOTAL: {total_rows} filas, {total_feats} features")
    print(f"  Base de datos: {args.db}")


if __name__ == "__main__":
    main()
