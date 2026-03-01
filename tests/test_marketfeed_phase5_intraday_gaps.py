from __future__ import annotations

from datetime import datetime, timezone

import numpy as np
import pandas as pd

from marketfeed.gaps import fill_session_gaps


def test_inserts_nan_row_for_missing_bar():
    """Verifica que fill_session_gaps inserta filas NaN con is_gap=True
    para timestamps faltantes, según DataFrame.md."""

    session_open = datetime(2026, 2, 2, 9, 30, tzinfo=timezone.utc)
    session_close = datetime(2026, 2, 2, 16, 0, tzinfo=timezone.utc)

    # 5 barras presentes; falta la vela de 11:30
    idx = pd.to_datetime([
        datetime(2026, 2, 2, 9, 30, tzinfo=timezone.utc),
        datetime(2026, 2, 2, 10, 30, tzinfo=timezone.utc),
        # 11:30 falta
        datetime(2026, 2, 2, 12, 30, tzinfo=timezone.utc),
        datetime(2026, 2, 2, 13, 30, tzinfo=timezone.utc),
        datetime(2026, 2, 2, 14, 30, tzinfo=timezone.utc),
    ])

    df = pd.DataFrame(
        {
            "open": [1.0] * 5,
            "high": [2.0] * 5,
            "low": [0.5] * 5,
            "close": [1.5] * 5,
            "volume": [100.0] * 5,
            "source": ["alpaca"] * 5,
            "quality": ["normal"] * 5,
            "is_gap": [False] * 5,
            "latency_sec": [0.1] * 5,
        },
        index=idx,
    )
    df.index.name = "timestamp"

    out, inserted = fill_session_gaps(
        df,
        session_open=session_open,
        session_close=session_close,
        timeframe="1h",
        provider_name="alpaca",
    )

    # Debe haber insertado exactamente 1 fila (la de 11:30)
    assert inserted == 1
    assert len(out) == 6  # 5 originales + 1 gap

    # La fila insertada tiene OHLCV=NaN, is_gap=True, quality="degraded"
    gap_ts = datetime(2026, 2, 2, 11, 30, tzinfo=timezone.utc)
    gap_row = out.loc[pd.Timestamp(gap_ts)]

    assert gap_row["is_gap"] is True or gap_row["is_gap"] == True
    assert gap_row["quality"] == "degraded"
    assert gap_row["source"] == "alpaca"
    assert np.isnan(gap_row["open"])
    assert np.isnan(gap_row["close"])
    assert np.isnan(gap_row["volume"])

    # Las filas originales NO están marcadas como gap
    non_gap = out[~out["is_gap"]]
    assert len(non_gap) == 5
    assert all(non_gap["quality"] == "normal")


def test_no_gaps_returns_unchanged():
    """Si todas las barras esperadas están presentes, no inserta nada."""

    session_open = datetime(2026, 2, 2, 9, 30, tzinfo=timezone.utc)
    session_close = datetime(2026, 2, 2, 16, 0, tzinfo=timezone.utc)

    # 6 barras = sesión completa NYSE
    idx = pd.to_datetime([
        datetime(2026, 2, 2, h, 30, tzinfo=timezone.utc)
        for h in range(9, 15)
    ])

    df = pd.DataFrame(
        {
            "open": [1.0] * 6,
            "high": [2.0] * 6,
            "low": [0.5] * 6,
            "close": [1.5] * 6,
            "volume": [100.0] * 6,
            "source": ["alpaca"] * 6,
            "quality": ["normal"] * 6,
            "is_gap": [False] * 6,
            "latency_sec": [0.1] * 6,
        },
        index=idx,
    )
    df.index.name = "timestamp"

    out, inserted = fill_session_gaps(
        df,
        session_open=session_open,
        session_close=session_close,
        timeframe="1h",
        provider_name="alpaca",
    )

    assert inserted == 0
    assert len(out) == 6
