from __future__ import annotations

from datetime import datetime, timezone
import pandas as pd

from marketfeed.aggregate import aggregate_4h_aligned


def test_aggregate_4h_aligned_nyse_session():
    # Sesión NYSE: 09:30–16:00
    idx = pd.date_range(
        start=datetime(2026, 2, 2, 9, 30, tzinfo=timezone.utc),
        periods=6,
        freq="1h",
    )

    df = pd.DataFrame(
        {
            "open": [1, 2, 3, 4, 5, 6],
            "high": [2, 3, 4, 5, 6, 7],
            "low": [0.5, 1.5, 2.5, 3.5, 4.5, 5.5],
            "close": [1.5, 2.5, 3.5, 4.5, 5.5, 6.5],
            "volume": [100] * 6,
            "source": ["alpaca"] * 6,
            "quality": ["normal"] * 6,
            "is_gap": [False] * 6,
            "latency_sec": [0.1] * 6,
        },
        index=idx,
    )

    out = aggregate_4h_aligned(
        df,
        session_start_hour=9,
        session_start_minute=30,
        session_end_hour=16,
        session_end_minute=0,
    )

    assert len(out) == 2

    first = out.iloc[0]
    assert first["open"] == 1
    assert first["close"] == 4.5
    assert first["volume"] == 400
    assert not bool(first["is_gap"])

    second = out.iloc[1]
    assert bool(second["is_gap"])