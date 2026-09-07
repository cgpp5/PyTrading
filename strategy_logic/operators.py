"""Operadores lógicos de StrategyLogic.

Dos familias:

- **Comparación** (``<``, ``>``, ``<=``, ``>=``, ``==``, ``!=``): comparan dos
  valores escalares ya resueltos en la barra actual.
- **Serie** (``pct_change``, ``slope``): derivan un escalar de la serie de una
  feature sobre una ventana terminada en la barra actual, y lo comparan contra
  un umbral.

Todas las funciones son puras: no mutan estado ni producen efectos secundarios.
"""

from __future__ import annotations

import math
from enum import Enum

import numpy as np
import pandas as pd


class Operator(Enum):
    LT = "<"
    GT = ">"
    LE = "<="
    GE = ">="
    EQ = "=="
    NE = "!="
    PCT_CHANGE = "pct_change"
    SLOPE = "slope"

    @property
    def is_comparison(self) -> bool:
        return self in (
            Operator.LT, Operator.GT, Operator.LE,
            Operator.GE, Operator.EQ, Operator.NE,
        )

    @property
    def is_series(self) -> bool:
        return self in (Operator.PCT_CHANGE, Operator.SLOPE)


def compare(op: Operator, left: float, right: float) -> bool:
    """Evalúa un operador de comparación entre dos escalares.

    :raises ValueError: si *op* no es un operador de comparación.
    """
    if not op.is_comparison:
        raise ValueError(f"Operator {op.value!r} is not a comparison operator")

    if op is Operator.LT:
        return left < right
    if op is Operator.GT:
        return left > right
    if op is Operator.LE:
        return left <= right
    if op is Operator.GE:
        return left >= right
    if op is Operator.EQ:
        return left == right
    if op is Operator.NE:
        return left != right
    raise ValueError(f"Unknown comparison operator {op.value!r}")  # pragma: no cover


def pct_change(series: pd.Series, lookback: int, at: int) -> float | None:
    """Cambio porcentual de *series* entre la barra ``at - lookback`` y ``at``.

    Fórmula: ``((cur - base) / max(|base|, eps)) * 100``.

    Devuelve ``None`` si no hay suficiente histórico (``at < lookback``) o si
    los valores implicados son NaN.
    """
    if lookback <= 0:
        raise ValueError("lookback must be positive")
    if at < lookback or at >= len(series):
        return None

    base = series.iloc[at - lookback]
    cur = series.iloc[at]
    if pd.isna(base) or pd.isna(cur):
        return None

    denom = max(abs(float(base)), 1e-9)
    return ((float(cur) - float(base)) / denom) * 100.0


def slope(series: pd.Series, window: int, at: int) -> float | None:
    """Pendiente (regresión lineal) de *series* en la ventana terminada en ``at``.

    Usa ``np.polyfit`` de grado 1 sobre los ``window`` últimos valores
    (inclusive). Devuelve ``None`` si no hay suficiente histórico o si hay NaN
    en la ventana.
    """
    if window < 2:
        raise ValueError("slope window must be at least 2")
    if at < window - 1 or at >= len(series):
        return None

    values = series.iloc[at - window + 1 : at + 1].to_numpy(dtype=float)
    if np.isnan(values).any():
        return None

    x = np.arange(window, dtype=float)
    coeffs = np.polyfit(x, values, 1)
    return float(coeffs[0])


def is_finite(value: float | None) -> bool:
    """True si *value* es un número finito (no None/NaN/inf)."""
    if value is None:
        return False
    return math.isfinite(value)
