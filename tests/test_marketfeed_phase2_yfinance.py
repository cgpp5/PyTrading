from __future__ import annotations

from datetime import datetime, timezone
import pandas as pd
import pytest

from marketfeed.marketfeed import MarketFeed, ProviderTier
from marketfeed.providers.yfinance import YFinanceProvider
from marketfeed.calendar import MarketCalendarResolver
from marketfeed.observability import InMemoryObservability
from marketfeed.errors import ProviderError


class DummyYF:
    @staticmethod
    def download(*args, **kwargs):
        return pd.DataFrame(
            {
                "Date": [datetime(2026, 2, 1, tzinfo=timezone.utc)],
                "Open": [1.0],
                "High": [2.0],
                "Low": [0.5],
                "Close": [1.5],
                "Volume": [100.0],
            }
        )


def test_yfinance_provider_success(monkeypatch):
    import marketfeed.providers.yfinance as yfmod

    monkeypatch.setattr(yfmod, "yf", DummyYF)

    obs = InMemoryObservability()
    cal = MarketCalendarResolver({"AAPL": "NYSE"}, obs)

    feed = MarketFeed(
        tiers=[ProviderTier(provider=YFinanceProvider(), quality="degraded")],
        calendar_resolver=cal,
        observability=obs,
    )

    start = datetime(2026, 2, 1, tzinfo=timezone.utc)
    end = datetime(2026, 2, 2, tzinfo=timezone.utc)

    md = feed.get_ohlcv("AAPL", "1d", start, end)

    assert not md.df.empty
    assert md.meta.provider_used == "yfinance"
    assert md.meta.quality == "degraded"
    assert md.df.index.tz is not None


def test_yfinance_no_data_raises_provider_error(monkeypatch):
    import marketfeed.providers.yfinance as yfmod

    class EmptyYF:
        @staticmethod
        def download(*args, **kwargs):
            return pd.DataFrame()

    monkeypatch.setattr(yfmod, "yf", EmptyYF)

    provider = YFinanceProvider()

    with pytest.raises(ProviderError):
        provider.fetch_ohlcv(
            "AAPL",
            "1d",
            datetime(2026, 2, 1, tzinfo=timezone.utc),
            datetime(2026, 2, 2, tzinfo=timezone.utc),
        )
