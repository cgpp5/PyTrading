from __future__ import annotations

from datetime import timedelta
import pandas as pd


def detect_intraday_gaps(
    df: pd.DataFrame,
    session_open: pd.Timestamp,
    session_close: pd.Timestamp,
    timeframe: str,
) -> pd.DataFrame:
    """
    Marca is_gap=True si faltan velas dentro de una sesión oficial.

    Requisitos:
    - df indexado por timestamp UTC
    - df ya normalizado
    - session_open / session_close oficiales del calendario
    """

    if df.empty:
        return df

    tf_map = {
        "15m": timedelta(minutes=15),
        "1h": timedelta(hours=1),
    }

    if timeframe not in tf_map:
        raise ValueError(f"Unsupported timeframe for gap detection: {timeframe}")

    step = tf_map[timeframe]

    expected_index = pd.date_range(
        start=session_open,
        end=session_close - step,
        freq=step,
        tz="UTC",
    )

    actual_index = df.index.intersection(expected_index)

    is_gap = len(actual_index) < len(expected_index)

    if is_gap:
        df = df.copy()
        df["is_gap"] = True

    return df
