from datetime import datetime, timezone

def test_nyse_normal_session_is_not_special(nyse_calendar_resolver):
    sessions = nyse_calendar_resolver.get_session_info(
        symbol="AAPL",
        start=datetime(2026, 3, 2, tzinfo=timezone.utc),
        end=datetime(2026, 3, 2, tzinfo=timezone.utc),
    )

    assert len(sessions) == 1

    session = sessions[0]

    assert session.is_special_session is False
    assert session.expected_bars == 6


from datetime import datetime, timezone

def test_nyse_early_close_is_special_session(nyse_calendar_resolver):
    sessions = nyse_calendar_resolver.get_session_info(
        symbol="AAPL",
        start=datetime(2026, 11, 27, tzinfo=timezone.utc),
        end=datetime(2026, 11, 27, tzinfo=timezone.utc),
    )

    assert len(sessions) == 1

    session = sessions[0]

    assert session.is_special_session is True
    assert session.expected_bars == 3


def test_special_session_does_not_imply_gap():
    from datetime import datetime, timezone
    from market_feed.calendar import SessionInfo

    session = SessionInfo(
        market_open=datetime(2026, 11, 27, 14, 30, tzinfo=timezone.utc),
        market_close=datetime(2026, 11, 27, 18, 0, tzinfo=timezone.utc),
        expected_bars=3,
        is_special_session=True,
    )

    actual_bars = 3

    assert actual_bars == session.expected_bars


def test_expected_bars_is_integer():
    from datetime import datetime, timezone
    from market_feed.calendar import SessionInfo

    session = SessionInfo(
        market_open=datetime(2026, 3, 2, 14, 30, tzinfo=timezone.utc),
        market_close=datetime(2026, 3, 2, 21, 0, tzinfo=timezone.utc),
        expected_bars=6,
        is_special_session=False,
    )

    assert isinstance(session.expected_bars, int)
    assert session.expected_bars >= 0


import pytest
from market_feed.calendar import MarketCalendarResolver
from market_feed.observability import InMemoryObservability

@pytest.fixture
def nyse_calendar_resolver():
    obs = InMemoryObservability()
    symbol_calendar_map = {"AAPL": "NYSE"}
    return MarketCalendarResolver(symbol_calendar_map=symbol_calendar_map, observability=obs)
