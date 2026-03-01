from __future__ import annotations

from datetime import datetime, timedelta

import numpy as np
import pandas as pd


def fill_session_gaps(
    df: pd.DataFrame,
    session_open: datetime,
    session_close: datetime,
    timeframe: str,
    provider_name: str,
) -> tuple[pd.DataFrame, int]:
    """
    Inserta filas NaN para timestamps esperados que falten dentro de una sesión.

    Per DataFrame.md:
      - timestamp correcto
      - OHLCV = NaN
      - is_gap = True
      - quality = "degraded"
      - source = provider_name

    Devuelve (df_con_gaps_insertados, número_de_filas_insertadas).
    """

    tf_map = {
        "15m": timedelta(minutes=15),
        "1h": timedelta(hours=1),
    }

    if timeframe not in tf_map:
        raise ValueError(
            f"Unsupported timeframe for gap detection: {timeframe}"
        )

    step = tf_map[timeframe]

    expected_index = pd.date_range(
        start=session_open,
        end=session_close - step,
        freq=step,
        tz="UTC",
    )

    missing = expected_index.difference(df.index)

    if len(missing) == 0:
        return df, 0

    gap_rows = pd.DataFrame(
        {
            "open": np.nan,
            "high": np.nan,
            "low": np.nan,
            "close": np.nan,
            "volume": np.nan,
            "source": provider_name,
            "quality": "degraded",
            "is_gap": True,
            "latency_sec": np.nan,
        },
        index=missing,
    )
    gap_rows.index.name = "timestamp"

    result = pd.concat([df, gap_rows]).sort_index()
    # Si hay duplicados accidentales, conservar el dato real
    result = result[~result.index.duplicated(keep="first")]

    return result, len(missing)
