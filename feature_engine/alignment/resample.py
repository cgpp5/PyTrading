"""Resample alignment strategies: linear interpolation and stepwise.

Both strategies project a coarse-timeframe feature onto a finer target
index.  They differ only in how intermediate points are computed:

  - LINEAR_INTERPOLATION: linearly interpolates between consecutive
    available values.
  - STEPWISE: holds the value of the *previous* available point until
    the next one (identical to forward-fill in shape, but semantically
    distinct — stepwise is used when the feature declares interpolation
    explicitly via InterpolationPolicy).

Like forward_fill, both strategies apply the availability offset first
to guarantee point-in-time safety.
"""

from __future__ import annotations

import pandas as pd

from market_feed.timeframes import Timeframe
from feature_engine.feature_spec.temporal import AvailabilityRule

from .rules import make_available_index


def linear_interpolation(
    values: pd.Series,
    source_tf: Timeframe,
    target_index: pd.DatetimeIndex,
    availability: AvailabilityRule,
) -> pd.Series:
    """Align *values* onto *target_index* via linear interpolation.

    Steps:
      1. Shift source timestamps by availability offset.
      2. Reindex onto the union of shifted + target.
      3. Interpolate linearly between known points.
      4. Select only target timestamps.

    Leading/trailing bars outside known source range are NaN (no
    extrapolation).
    """
    available_index = make_available_index(values.index, availability, source_tf)
    shifted = pd.Series(values.values, index=available_index, name=values.name)

    combined_index = shifted.index.union(target_index).sort_values()
    combined = shifted.reindex(combined_index)
    combined = combined.interpolate(method="index")

    result = combined.reindex(target_index)

    # Null out leading positions before first available source value
    if len(available_index) > 0:
        first_available = available_index.min()
        result.loc[result.index < first_available] = float("nan")

    return result


def stepwise(
    values: pd.Series,
    source_tf: Timeframe,
    target_index: pd.DatetimeIndex,
    availability: AvailabilityRule,
) -> pd.Series:
    """Align *values* onto *target_index* via stepwise (staircase) method.

    Semantically distinct from forward_fill — stepwise is declared
    explicitly via alignment policy and signals that intermediate bars
    intentionally hold the prior value (not merely "filled because missing").
    The mechanical result is identical to forward_fill.
    """
    available_index = make_available_index(values.index, availability, source_tf)
    shifted = pd.Series(values.values, index=available_index, name=values.name)

    combined = shifted.reindex(shifted.index.union(target_index))
    combined = combined.sort_index()
    combined = combined.ffill()

    return combined.reindex(target_index)
