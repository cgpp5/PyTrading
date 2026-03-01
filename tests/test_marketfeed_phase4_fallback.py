from __future__ import annotations

from datetime import datetime, timezone
import unittest
import pandas as pd

from marketfeed.marketfeed import MarketFeed, ProviderTier
from marketfeed.calendar import MarketCalendarResolver
from marketfeed.observability import InMemoryObservability
from marketfeed.errors import ProviderError
from marketfeed.providers.base import MarketDataProvider


# --- Proveedores dummy para simular fallos y éxito ---

class FailingAlpaca(MarketDataProvider):

    @property
    def name(self) -> str:
        return "alpaca"

    def fetch_ohlcv(self, *args, **kwargs):
        raise ProviderError("alpaca down")


class FailingTiingo(MarketDataProvider):

    @property
    def name(self) -> str:
        return "tiingo"

    def fetch_ohlcv(self, *args, **kwargs):
        raise ProviderError("tiingo down")


class WorkingYFinance(MarketDataProvider):

    @property
    def name(self) -> str:
        return "yfinance"

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


class TestMarketFeedFallback(unittest.TestCase):
    def setUp(self):
        self.obs = InMemoryObservability()
        self.calendar = MarketCalendarResolver(
            symbol_calendar_map={"AAPL": "NYSE"},
            observability=self.obs,
        )

        self.feed = MarketFeed(
            tiers=[
                ProviderTier(FailingAlpaca(), quality="normal"),
                ProviderTier(FailingTiingo(), quality="normal"),
                ProviderTier(WorkingYFinance(), quality="degraded"),
            ],
            calendar_resolver=self.calendar,
            observability=self.obs,
        )

        self.start = datetime(2026, 2, 1, tzinfo=timezone.utc)
        self.end = datetime(2026, 2, 2, tzinfo=timezone.utc)

    def test_fallback_alpaca_fails_uses_tiingo(self):
        feed = MarketFeed(
            tiers=[
                ProviderTier(FailingAlpaca(), quality="normal"),
                ProviderTier(WorkingYFinance(), quality="normal"),
            ],
            calendar_resolver=self.calendar,
            observability=self.obs,
        )

        md = feed.get_ohlcv("AAPL", "1d", self.start, self.end)

        self.assertFalse(md.df.empty)
        self.assertEqual(md.meta.provider_used, "yfinance")
        self.assertTrue(md.meta.fallback_used)
        self.assertEqual(
            md.meta.extra["attempted_providers"],
            ["alpaca", "yfinance"],
        )

    def test_fallback_both_fail_uses_yfinance(self):
        md = self.feed.get_ohlcv("AAPL", "1d", self.start, self.end)

        self.assertFalse(md.df.empty)
        self.assertEqual(md.meta.provider_used, "yfinance")
        self.assertTrue(md.meta.fallback_used)
        self.assertEqual(
            md.meta.extra["attempted_providers"],
            ["alpaca", "tiingo", "yfinance"],
        )

        # Observability: dos warnings, ningún error crítico
        self.assertEqual(len(self.obs.warnings), 2)
        self.assertEqual(len(self.obs.errors), 0)
        self.assertEqual(len(self.obs.criticals), 0)
