from __future__ import annotations

from datetime import datetime, timezone

import pandas as pd
import pytest

from marketfeed.marketfeed import MarketFeed, ProviderTier
from marketfeed.calendar import MarketCalendarResolver
from marketfeed.observability import InMemoryObservability
from marketfeed.providers.base import MarketDataProvider
from marketfeed.errors import ProviderError


# ----------------------------------------------------------------
# Proveedores dummy que devuelven datos 1h controlados
# ----------------------------------------------------------------

class FullSessionProvider(MarketDataProvider):
    """Devuelve una sesión NYSE completa de 6 barras 1h (9:30–15:30 ET)."""

    @property
    def name(self) -> str:
        return "full_provider"

    def fetch_ohlcv(self, symbol, timeframe, start, end):
        # NYSE March 2, 2026 (EST, UTC-5): 14:30–21:00 UTC
        idx = pd.date_range(
            start=datetime(2026, 3, 2, 14, 30, tzinfo=timezone.utc),
            periods=6,
            freq="1h",
        )
        return pd.DataFrame(
            {
                "timestamp": idx,
                "open": [100.0, 101.0, 102.0, 103.0, 104.0, 105.0],
                "high": [101.0, 102.0, 103.0, 104.0, 105.0, 106.0],
                "low": [99.0, 100.0, 101.0, 102.0, 103.0, 104.0],
                "close": [101.0, 102.0, 103.0, 104.0, 105.0, 106.0],
                "volume": [1000.0] * 6,
            }
        )


class PartialSessionProvider(MarketDataProvider):
    """Devuelve una sesión con 1 barra faltante (15:30 no aparece)."""

    @property
    def name(self) -> str:
        return "partial_provider"

    def fetch_ohlcv(self, symbol, timeframe, start, end):
        # 5 de 6 barras — falta 15:30
        idx = pd.date_range(
            start=datetime(2026, 3, 2, 14, 30, tzinfo=timezone.utc),
            periods=5,
            freq="1h",
        )
        return pd.DataFrame(
            {
                "timestamp": idx,
                "open": [100.0, 101.0, 102.0, 103.0, 104.0],
                "high": [101.0, 102.0, 103.0, 104.0, 105.0],
                "low": [99.0, 100.0, 101.0, 102.0, 103.0],
                "close": [101.0, 102.0, 103.0, 104.0, 105.0],
                "volume": [1000.0] * 5,
            }
        )


# ----------------------------------------------------------------
# Helpers
# ----------------------------------------------------------------

def _make_feed(provider, quality="normal"):
    obs = InMemoryObservability()
    cal = MarketCalendarResolver(
        symbol_calendar_map={"AAPL": "NYSE"},
        observability=obs,
    )
    feed = MarketFeed(
        tiers=[ProviderTier(provider=provider, quality=quality)],
        calendar_resolver=cal,
        observability=obs,
    )
    return feed, obs


# ----------------------------------------------------------------
# Tests
# ----------------------------------------------------------------

def test_4h_e2e_full_session():
    """get_ohlcv('4h') con sesión completa produce 2 velas 4h correctas."""

    feed, obs = _make_feed(FullSessionProvider())

    start = datetime(2026, 3, 2, tzinfo=timezone.utc)
    end = datetime(2026, 3, 2, tzinfo=timezone.utc)

    md = feed.get_ohlcv("AAPL", "4h", start, end)

    # Metadata
    assert md.meta.timeframe == "4h"
    assert md.meta.provider_used == "full_provider"
    assert md.meta.gap_count == 0
    assert md.meta.quality == "normal"

    # 2 velas: ventana 14:30–18:30 (4 barras) + ventana 18:30–21:00 (2 barras)
    assert len(md.df) == 2

    first = md.df.iloc[0]
    assert first["open"] == 100.0
    assert first["close"] == 104.0
    assert first["volume"] == 4000.0
    assert not bool(first["is_gap"])

    second = md.df.iloc[1]
    assert second["open"] == 104.0   # barra 18:30 tiene open=104
    assert second["close"] == 106.0
    assert second["volume"] == 2000.0
    assert not bool(second["is_gap"])


def test_4h_e2e_with_gap_propagates_to_metadata():
    """get_ohlcv('4h') con barra faltante marca quality='degraded'."""

    feed, obs = _make_feed(PartialSessionProvider())

    start = datetime(2026, 3, 2, tzinfo=timezone.utc)
    end = datetime(2026, 3, 2, tzinfo=timezone.utc)

    md = feed.get_ohlcv("AAPL", "4h", start, end)

    # Metadata refleja la degradación
    assert md.meta.quality == "degraded"
    assert md.meta.gap_count == 1  # 1 barra NaN insertada
    assert md.meta.timeframe == "4h"

    # La segunda vela 4h (18:30–21:00) tiene is_gap=True
    # porque una de sus barras constituyentes (19:30) es un gap NaN
    second = md.df.iloc[1]
    assert bool(second["is_gap"])
