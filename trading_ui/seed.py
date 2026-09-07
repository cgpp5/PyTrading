"""trading_ui.seed — Pobla data_store con datos reales para validación visual.

Delega en ``trading_ui.ingest`` (fuente de verdad única para la descarga y el
cálculo de features).

Uso:
    python -m trading_ui.seed
    python -m trading_ui.seed --symbols AAPL SPY MSFT --days 365
"""

from __future__ import annotations

import argparse
from datetime import datetime, timedelta, timezone

from data_store.core import DataStoreCore
from trading_ui import ingest


DB_PATH = "trading_data.sqlite"
DEFAULT_SYMBOLS = ["AAPL", "SPY"]
DEFAULT_DAYS = 365
TIMEFRAME = "1d"


def _seed_symbol(
    store: DataStoreCore,
    symbol: str,
    start: datetime,
    end: datetime,
) -> dict:
    """Descarga, calcula features y persiste datos para un símbolo."""
    print(f"  [{symbol}] Descargando OHLCV ({TIMEFRAME})...", flush=True)
    res = ingest.fetch_and_store_symbol(store, symbol, TIMEFRAME, start, end)
    print(
        f"  [{symbol}] {res['rows']} filas, "
        f"{res['features']} features ({res['action']})"
    )
    return {"symbol": symbol, "rows": res["rows"], "features": res["features"]}


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

    results = []
    for symbol in args.symbols:
        result = _seed_symbol(store, symbol, start, end)
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
