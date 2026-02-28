from __future__ import annotations

import numpy as np
import pandas as pd

REQUIRED_PRICE_COLS = ["open", "high", "low", "close", "volume"]
CONTROL_COLS = ["source", "quality", "is_gap", "latency_sec"]
CANONICAL_COLS = REQUIRED_PRICE_COLS + CONTROL_COLS


def empty_ohlcv_dataframe() -> pd.DataFrame:
    df = pd.DataFrame(columns=CANONICAL_COLS)
    df.index.name = "timestamp"
    return df


def _ensure_utc_index(df: pd.DataFrame) -> pd.DataFrame:
    out = df.copy()

    if "timestamp" in out.columns:
        out["timestamp"] = pd.to_datetime(out["timestamp"], utc=True, errors="raise")
        out = out.set_index("timestamp")
    else:
        out.index = pd.to_datetime(out.index, utc=True, errors="raise")

    out.index.name = "timestamp"
    return out.sort_index()


def _dedupe_index_keep_last(df: pd.DataFrame) -> pd.DataFrame:
    # determinista: si hay duplicados, nos quedamos con el último
    return df[~df.index.duplicated(keep="last")]


def normalize_ohlcv(raw: pd.DataFrame, *, provider_name: str, quality: str) -> pd.DataFrame:
    if raw is None:
        raise ValueError("raw cannot be None")

    df = _ensure_utc_index(raw)
    df = _dedupe_index_keep_last(df)

    missing = [c for c in REQUIRED_PRICE_COLS if c not in df.columns]
    if missing:
        raise ValueError(f"Missing columns: {missing}")

    # Solo nos quedamos con OHLCV; ignoramos extras del proveedor
    df = df[REQUIRED_PRICE_COLS].copy()

    # Tipos estrictos
    df = df.astype("float64")

    # Columnas de control (siempre presentes)
    df["source"] = provider_name
    df["quality"] = quality
    df["is_gap"] = False
    df["latency_sec"] = np.nan

    # Orden canónico fijo
    df = df[CANONICAL_COLS]

    return df
