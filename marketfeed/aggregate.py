from __future__ import annotations

from datetime import timedelta
import pandas as pd


def aggregate_4h_aligned(
    df_1h: pd.DataFrame,
    session_start_hour: int,
    session_start_minute: int,
    session_end_hour: int,
    session_end_minute: int,
) -> pd.DataFrame:
    """
    Agrega velas 1h a 4h alineadas a la sesión de mercado.

    Requisitos:
    - df_1h indexado por timestamp UTC
    - columnas canónicas OHLCV + control
    """

    if df_1h.empty:
        return df_1h.copy()

    df = df_1h.copy().sort_index()

    # Construimos los límites de sesión por día
    sessions = []
    for day in df.index.normalize().unique():
        start = day + timedelta(
            hours=session_start_hour,
            minutes=session_start_minute,
        )
        end = day + timedelta(
            hours=session_end_hour,
            minutes=session_end_minute,
        )
        sessions.append((start, end))

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

            expected_bars = int((window_end - window_start) / timedelta(hours=1))
            is_gap = len(window_df) < expected_bars

            aggregated_rows.append(
                {
                    "timestamp": window_start,
                    "open": window_df.iloc[0]["open"],
                    "high": window_df["high"].max(),
                    "low": window_df["low"].min(),
                    "close": window_df.iloc[-1]["close"],
                    "volume": window_df["volume"].sum(),
                    "source": window_df.iloc[0]["source"],
                    "quality": (
                        "degraded" if is_gap else window_df.iloc[0]["quality"]
                    ),
                    "is_gap": is_gap,
                    "latency_sec": window_df["latency_sec"].max(),
                }
            )

            window_start = window_end

    out = pd.DataFrame(aggregated_rows)
    if out.empty:
        return out

    out["timestamp"] = pd.to_datetime(out["timestamp"], utc=True)
    out.set_index("timestamp", inplace=True)
    return out.sort_index()
