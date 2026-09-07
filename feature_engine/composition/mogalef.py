"""Mogalef Bands (Eric Lefort) derived features.

Implements the MetaStock Express formula for the Mogalef Bands (see the
companion ``EL_MOGALEF_Bands`` formulas) as price-overlay feature series.

Core construction:
  1. A weighted "Mogalef" price ``(H + L + O + C + C) / 5`` (close double
     weighted).  The original script quantises this to integer ticks for
     numerical stability; here we work directly in price units (equivalent,
     modulo insignificant rounding).
  2. A rolling linear regression of that price on the bar index over ``n``
     bars yields the *middle* line (a causal, trailing regression line).
  3. A rolling standard deviation of the regression line over ``et`` bars
     sizes the band half-width.
  4. A **backward scan** (from the last bar to the first) builds the
     envelope: the band stays **flat** while the regression line lies inside
     it, and only "opens up" (re-anchors) when the regression line breaks out
     on either side.

Because step 4 runs backwards from the final bar the bands are
**retrospective / repainting by design** -- recomputing over a longer window
can change historical band values.  That is part of the indicator's intended
behaviour, not a bug.
"""

from __future__ import annotations

import numpy as np
import pandas as pd

from market_feed.timeframes import Timeframe

from feature_engine.feature_spec.enums import (
    AlignmentPolicy,
    FeatureCategory,
    WarmupPolicy,
)
from feature_engine.feature_spec.spec import FeatureSpec
from feature_engine.feature_spec.temporal import AvailabilityRule

from .base import DerivedFeature


def _format_param(value: float) -> str:
    return f"{value:g}".replace(".", "_")


def _band_names(n: int, et: int, coef: float) -> tuple[str, str, str]:
    coef_str = _format_param(coef)
    return (
        f"mogalef_middle_{n}_{et}_{coef_str}",
        f"mogalef_upper_{n}_{et}_{coef_str}",
        f"mogalef_lower_{n}_{et}_{coef_str}",
    )


def _rolling_regression_line(y: np.ndarray, n: int) -> np.ndarray:
    """Rolling linear regression of ``y`` on bar index over ``n`` bars.

    Returns the regression line value at each bar (the last observation of
    the window), padded with NaN until ``n`` bars are available.
    """
    if n < 2:
        raise ValueError("n must be >= 2 to fit a regression line")
    length = len(y)
    out = np.full(length, np.nan, dtype="float64")
    if length < n:
        return out

    from numpy.lib.stride_tricks import sliding_window_view

    # Each row is a window [oldest ... newest]; index x = 0 .. n-1.
    windows = sliding_window_view(y, n)
    x = np.arange(n, dtype="float64")
    xbar = (n - 1) / 2.0
    varx = n * (n**2 - 1) / 12.0
    weights = x - xbar

    # Slope b = sum((x - xbar)(y - ybar)) / varx; the ybar term sums to zero.
    slope = (windows @ weights) / varx
    ybar = windows.mean(axis=1)
    # Evaluate at the newest bar (x = n - 1): a + b*(n-1) = ybar + b*(n-1)/2
    pred = ybar + slope * ((n - 1) / 2.0)

    out[n - 1:] = pred
    return out


def _scan_bands(
    reg: np.ndarray,
    etyp: np.ndarray,
    coef: float,
) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    """Backward scan that builds the flat/breakout envelope.

    Returns ``(middle, upper, lower)`` arrays.  Walking from the last bar to
    the first, when the regression line is still inside the band already set
    at the *next* bar the band is carried forward flat; otherwise a fresh band
    (regression +/- coef * std) is anchored.
    """
    length = len(reg)
    middle = np.full(length, np.nan, dtype="float64")
    upper = np.full(length, np.nan, dtype="float64")
    lower = np.full(length, np.nan, dtype="float64")

    for j in range(length - 1, -1, -1):
        rj = reg[j]
        ej = etyp[j]
        if np.isnan(rj) or np.isnan(ej):
            continue

        if j < length - 1:
            pu = upper[j + 1]
            pl = lower[j + 1]
            if (not np.isnan(pu)) and (not np.isnan(pl)) and (rj < pu) and (rj > pl):
                # Regression line still inside the existing band -> flat.
                upper[j] = pu
                lower[j] = pl
                middle[j] = middle[j + 1]
                continue

        # Regression line has broken out (or this is the final bar) -> open a
        # fresh band anchored on the current regression line.
        upper[j] = rj + coef * ej
        lower[j] = rj - coef * ej
        middle[j] = rj

    return middle, upper, lower


def _compute_mogalef_bands(
    df: pd.DataFrame,
    n: int,
    et: int,
    coef: float,
) -> tuple[pd.Series, pd.Series, pd.Series]:
    """Return ``(middle, upper, lower)`` band series aligned to ``df.index``."""
    weighted = (df["high"] + df["low"] + df["open"] + df["close"] + df["close"]) / 5.0
    y = weighted.astype("float64").to_numpy()

    reg = _rolling_regression_line(y, n)
    reg_series = pd.Series(reg, index=df.index, dtype="float64")

    # Std dev of the regression line over `et` bars (population, ddof=0) --
    # matching MetaStock's StdDev.  Masked to NaN where the regression line is
    # not yet defined so the band scan stays NaN across gap/warm-up rows.
    etyp = reg_series.rolling(window=et, min_periods=et).std(ddof=0)
    etyp = etyp.where(reg_series.notna())

    middle, upper, lower = _scan_bands(reg, etyp.to_numpy(dtype="float64"), float(coef))

    return (
        pd.Series(middle, index=df.index, dtype="float64"),
        pd.Series(upper, index=df.index, dtype="float64"),
        pd.Series(lower, index=df.index, dtype="float64"),
    )


class _MogalefBandBase(DerivedFeature):
    """Shared plumbing for the three Mogalef band series."""

    _suffix = ""

    def __init__(
        self,
        n: int = 3,
        et: int = 7,
        coef: float = 2.0,
        timeframe: Timeframe = "1d",
    ) -> None:
        if n < 2:
            raise ValueError("n must be >= 2")
        if et < 2:
            raise ValueError("et must be >= 2")
        if coef <= 0:
            raise ValueError("coef must be > 0")
        self._n = n
        self._et = et
        self._coef = coef
        self._timeframe = timeframe

        middle_name, upper_name, lower_name = _band_names(n, et, coef)
        name = {
            "middle": middle_name,
            "upper": upper_name,
            "lower": lower_name,
        }[self._suffix]
        self._spec = FeatureSpec(
            name=name,
            version="1.0",
            category=FeatureCategory.TECHNICAL,
            timeframe=timeframe,
            alignment=AlignmentPolicy.NONE,
            availability=AvailabilityRule.AT_CLOSE,
            depends_on=(),
            # Regression makes the line defined after n bars; the et-bar std dev
            # of that line needs `et` more observations, hence n + et - 1 total.
            lookback_required=n + et - 1,
            warmup_policy=WarmupPolicy.FIXED_LOOKBACK,
        )

    @property
    def spec(self) -> FeatureSpec:
        return self._spec

    def compute(self, df: pd.DataFrame) -> pd.Series:
        self._validate_columns(df, {"open", "high", "low", "close"})
        middle, upper, lower = _compute_mogalef_bands(
            df, self._n, self._et, self._coef
        )
        return {"middle": middle, "upper": upper, "lower": lower}[self._suffix]


class MogalefMiddleBand(_MogalefBandBase):
    """Middle Mogalef band: the flat-carry regression line (MogM)."""

    _suffix = "middle"


class MogalefUpperBand(_MogalefBandBase):
    """Upper Mogalef band (MogH)."""

    _suffix = "upper"


class MogalefLowerBand(_MogalefBandBase):
    """Lower Mogalef band (MogB)."""

    _suffix = "lower"
