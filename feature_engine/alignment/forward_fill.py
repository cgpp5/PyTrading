"""Forward-fill alignment strategy.

Projects a coarse-timeframe feature onto a finer target index by
carrying forward the most recent *available* value.

Invariant: a value at source timestamp T with AvailabilityRule offset D
is only visible at target timestamps >= T + D.  Earlier target bars are NaN.
"""

from __future__ import annotations

import pandas as pd

from market_feed.timeframes import Timeframe
from feature_engine.feature_spec.temporal import AvailabilityRule

from .rules import make_available_index


def forward_fill(
    values: pd.Series,
    source_tf: Timeframe,
    target_index: pd.DatetimeIndex,
    availability: AvailabilityRule,
) -> pd.Series:
    """Align *values* onto *target_index* via forward-fill.

    Steps:
      1. Shift source timestamps by the availability offset
         (point-in-time safety — no leakage).
      2. Reindex onto the target, introducing NaN at unknown positions.
      3. Forward-fill: each target bar inherits the last available value.

    Returns:
        Series indexed by *target_index*.  Leading bars before the first
        available source value are NaN.
    """
    available_index = make_available_index(values.index, availability, source_tf)
    shifted = pd.Series(values.values, index=available_index, name=values.name)

    # Combine shifted source with target, forward-fill, then select target only
    combined = shifted.reindex(shifted.index.union(target_index))
    combined = combined.sort_index()
    combined = combined.ffill()

    return combined.reindex(target_index)
