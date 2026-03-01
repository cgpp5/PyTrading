from __future__ import annotations

from datetime import datetime, timezone
import pandas as pd

from marketfeed.gaps import detect_intraday_gaps


def test_detects_intraday_gap():
    session_open = datetime(2026, 2, 2, 9, 30, tzinfo=timezone.utc)
    session_close = datetime(2026, 2, 2, 16, 0, tzinfo=timezone.utc)

    # Falta la vela de 11:30
    idx = [
        datetime(2026, 2, 2, 9, 30, tzinfo=timezone.utc),
        datetime(2026, 2, 2, 10, 30, tzinfo=timezone.utc),
        datetime(2026, 2, 2, 12, 30, tzinfo=timezone.utc),
        datetime(2026, 2, 2, 13, 30, tzinfo=timezone.utc),
        datetime(2026, 2, 2, 14, 30, tzinfo=timezone.utc),
        datetime(2026, 2, 2, 15, 30, tzinfo=timezone.utc),
    ]

    df = pd.DataFrame(
        {
            "open": [1] * 6,
            "high": [2] * 6,
            "low": [0.5] * 6,
            "close": [1.5] * 6,
            "volume": [100] * 6,
            "source": ["alpaca"] * 6,
            "quality": ["normal"] * 6,
            "is_gap": [False] * 6,
            "latency_sec": [0.1] * 6,
        },
        index=idx,
    )

    out = detect_intraday_gaps(
        df,
        session_open=session_open,
        session_close=session_close,
        timeframe="1h",
    )

    assert bool(out["is_gap"].iloc[0]) is True
