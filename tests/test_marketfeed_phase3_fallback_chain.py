from __future__ import annotations

from datetime import datetime, timezone
import pandas as pd
import pytest

from marketfeed.marketfeed import MarketFeed, ProviderTier
from marketfeed.calendar import MarketCalendarResolver
from marketfeed.observability import InMemoryObservability
from marketfeed.errors import ProviderError
from marketfeed.providers.base import MarketDataProvider


# --- Proveedores dummy para simular la cadena real ---

class FailingAlpaca(MarketDataProvider):
    name = "alpaca"

    def fetch_ohlcv(self, *args, **kwargs):
        raise ProviderError("alpaca down")


class FailingTiingo(MarketDataProvider):
    name = "tiingo"

    def fetch_ohlcv(self, *args, **kwargs):
        raise ProviderError("tiingo down")


class WorkingYFinance(MarketDataProvider):
    name = "yfinance"

    def fetch_ohlcv(self, symbol, timeframe, start, end):
        return pd.DataFrame(
            {
                "timestamp": [start],
                "open": [1.0],
                "high": [2.0],
                "low": [0.5],
                "close": [1.5],
                "volume": [100.0],
            }
        )


def test_fallback_chain_alpaca_tiingo_yfinance():
    obs = InMemoryObservability()

    calendar = MarketCalendarResolver(
        symbol_calendar_map={"AAPL": "NYSE"},
        observability=obs,
    )

    feed = MarketFeed(
        tiers=[
            ProviderTier(provider=FailingAlpaca(), quality="normal"),
            ProviderTier(provider=FailingTiingo(), quality="normal"),
            ProviderTier(provider=WorkingYFinance(), quality="degraded"),
        ],
        calendar_resolver=calendar,
        observability=obs,
    )

    start = datetime(2026, 2, 1, tzinfo=timezone.utc)
    end = datetime(2026, 2, 2, tzinfo=timezone.utc)

    md = feed.get_ohlcv("AAPL", "1d", start, end)

    # --- Validaciones clave ---
    assert not md.df.empty
    assert md.meta.provider_used == "yfinance"
    assert md.meta.fallback_used is True
    assert md.meta.extra["attempted_providers"] == ["alpaca", "tiingo", "yfinance"]

    # Observability
    assert len(obs.warnings) == 2
    assert obs.warnings[0][1]["provider"] == "alpaca"
    assert obs.warnings[1][1]["provider"] == "tiingo"
    assert len(obs.errors) == 0
    assert len(obs.criticals) == 0
