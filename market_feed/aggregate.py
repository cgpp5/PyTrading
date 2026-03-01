from __future__ import annotations

from datetime import datetime, timedelta
from typing import Sequence

import numpy as np
import pandas as pd


def aggregate_4h_aligned(
    df_1h: pd.DataFrame,
    sessions: Sequence[tuple[datetime, datetime]],
) -> pd.DataFrame:
    """
    Agrega velas 1h a 4h alineadas a la sesión de mercado.

    Parámetros:
    - df_1h: DataFrame indexado por timestamp UTC con columnas canónicas.
    - sessions: lista de (market_open, market_close) por día de sesión,
      obtenida directamente del calendario de mercado.
    """

    if df_1h.empty:
        return df_1h.copy()

    df = df_1h.copy().sort_index()

    aggregated_rows = []

    for session_start, session_end in sessions:
        session_df = df.loc[(df.index >= session_start) & (df.index < session_end)]
        if session_df.empty:
            continue

        # Ventanas 4h desde apertura oficial
        window_start = session_start
        while window_start < session_end:
            window_end = window_start + timedelta(hours=4)
            window_df = session_df.loc[
                (session_df.index >= window_start)
                & (session_df.index < window_end)
            ]

            if window_df.empty:
                window_start = window_end
                continue

            # Cap al cierre real de sesión para la última ventana
            effective_end = min(window_end, session_end)
            expected_bars = int(
                (effective_end - window_start) / timedelta(hours=1)
            )

            # Gap si alguna barra constituyente es gap o faltan barras
            has_gap = (
                bool(window_df["is_gap"].any())
                or len(window_df) < expected_bars
            )

            # Usar solo barras reales (no-gap) para OHLCV
            real_df = window_df[~window_df["is_gap"]]

            if real_df.empty:
                # Toda la ventana son gaps → vela 4h completamente NaN
                aggregated_rows.append(
                    {
                        "timestamp": window_start,
                        "open": np.nan,
                        "high": np.nan,
                        "low": np.nan,
                        "close": np.nan,
                        "volume": np.nan,
                        "source": window_df.iloc[0]["source"],
                        "quality": "degraded",
                        "is_gap": True,
                        "latency_sec": np.nan,
                    }
                )
            else:
                aggregated_rows.append(
                    {
                        "timestamp": window_start,
                        "open": real_df.iloc[0]["open"],
                        "high": real_df["high"].max(),
                        "low": real_df["low"].min(),
                        "close": real_df.iloc[-1]["close"],
                        "volume": real_df["volume"].sum(),
                        "source": real_df.iloc[0]["source"],
                        "quality": (
                            "degraded"
                            if has_gap
                            else real_df.iloc[0]["quality"]
                        ),
                        "is_gap": has_gap,
                        "latency_sec": real_df["latency_sec"].max(),
                    }
                )

            window_start = window_end

    out = pd.DataFrame(aggregated_rows)
    if out.empty:
        return out

    out["timestamp"] = pd.to_datetime(out["timestamp"], utc=True)
    out.set_index("timestamp", inplace=True)
    return out.sort_index()
