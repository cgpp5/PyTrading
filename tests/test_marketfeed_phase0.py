from __future__ import annotations

from datetime import datetime, timezone

import pandas as pd
import pytest

from marketfeed.calendar import MarketCalendarResolver
from marketfeed.errors import ProviderError, ConfigurationError
from marketfeed.marketfeed import MarketFeed, ProviderTier
from marketfeed.observability import InMemoryObservability
from marketfeed.providers.base import MarketDataProvider


class AlwaysFailProvider(MarketDataProvider):

    @property
    def name(self) -> str:
        return "fail"

    def fetch_ohlcv(self, symbol: str, timeframe: str, start: datetime, end: datetime) -> pd.DataFrame:
        raise ProviderError("provider down")


class GoodProvider(MarketDataProvider):

    @property
    def name(self) -> str:
        return "good"

    def fetch_ohlcv(self, symbol: str, timeframe: str, start: datetime, end: datetime) -> pd.DataFrame:
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


class BuggyProvider(MarketDataProvider):

    @property
    def name(self) -> str:
        return "buggy"

    def fetch_ohlcv(self, symbol: str, timeframe: str, start: datetime, end: datetime) -> pd.DataFrame:
        # Missing required columns -> normalize_ohlcv will raise ValueError (internal)
        return pd.DataFrame({"timestamp": [start], "open": [1.0]})


def _mk_feed(tiers, symbol_calendar_map):
    obs = InMemoryObservability()
    cal = MarketCalendarResolver(symbol_calendar_map, obs)
    feed = MarketFeed(tiers=tiers, calendar_resolver=cal, observability=obs)
    return feed, obs


def test_missing_calendar_is_fatal():
    feed, obs = _mk_feed(
        tiers=[ProviderTier(provider=GoodProvider(), quality="normal")],
        symbol_calendar_map={},  # no mapping
    )
    with pytest.raises(ConfigurationError):
        feed.get_ohlcv("AAPL", "1h", datetime.now(timezone.utc), datetime.now(timezone.utc))

    assert len(obs.criticals) == 1
    assert obs.criticals[0][0] == "calendar_not_configured"


def test_fallback_on_provider_error():
    feed, obs = _mk_feed(
        tiers=[
            ProviderTier(provider=AlwaysFailProvider(), quality="normal"),
            ProviderTier(provider=GoodProvider(), quality="degraded"),
        ],
        symbol_calendar_map={"AAPL": "NYSE"},
    )

    start = datetime(2026, 2, 1, tzinfo=timezone.utc)
    end = datetime(2026, 2, 2, tzinfo=timezone.utc)

    md = feed.get_ohlcv("AAPL", "1h", start, end, allow_fallback=True)

    assert md.meta.provider_used == "good"
    assert md.meta.fallback_used is True
    assert md.meta.extra["attempted_providers"] == ["fail", "good"]
    assert len(obs.warnings) == 1
    assert obs.warnings[0][0] == "provider_failure"


def test_no_fallback_when_disabled():
    feed, obs = _mk_feed(
        tiers=[
            ProviderTier(provider=AlwaysFailProvider(), quality="normal"),
            ProviderTier(provider=GoodProvider(), quality="degraded"),
        ],
        symbol_calendar_map={"AAPL": "NYSE"},
    )

    start = datetime(2026, 2, 1, tzinfo=timezone.utc)
    end = datetime(2026, 2, 2, tzinfo=timezone.utc)

    md = feed.get_ohlcv("AAPL", "1h", start, end, allow_fallback=False)

    assert md.meta.provider_used == "none"
    assert md.df.empty
    assert len(obs.errors) == 1
    assert obs.errors[0][0] == "all_providers_failed"


def test_internal_error_is_not_silenced():
    feed, obs = _mk_feed(
        tiers=[
            ProviderTier(provider=BuggyProvider(), quality="normal"),
            ProviderTier(provider=GoodProvider(), quality="degraded"),
        ],
        symbol_calendar_map={"AAPL": "NYSE"},
    )

    start = datetime(2026, 2, 1, tzinfo=timezone.utc)
    end = datetime(2026, 2, 2, tzinfo=timezone.utc)

    with pytest.raises(ValueError):
        feed.get_ohlcv("AAPL", "1h", start, end, allow_fallback=True)

    # No warning of provider_failure because it wasn't ProviderError
    assert len(obs.warnings) == 0
    # No "all_providers_failed" because we aborted on internal error
    assert len(obs.errors) == 0
