"""Temporal alignment rules and compatibility checks.

This module is the **single source of truth** for:
  - Which timeframe pairs allow alignment (source → target).
  - How to compute the availability offset that prevents look-ahead bias.
  - Whether a given alignment direction is valid.

Nothing outside alignment/ may decide timestamps.
"""

from __future__ import annotations

from datetime import timedelta

import pandas as pd

from market_feed.timeframes import Timeframe
from feature_engine.errors import InvalidAlignment
from feature_engine.feature_spec.enums import AlignmentPolicy
from feature_engine.feature_spec.temporal import AvailabilityRule


# ------------------------------------------------------------------
# Timeframe ordering (resolution in minutes)
# ------------------------------------------------------------------

_RESOLUTION_MINUTES: dict[Timeframe, int] = {
    "15m": 15,
    "1h": 60,
    "4h": 240,
    "1d": 1440,
}


def resolution_minutes(tf: Timeframe) -> int:
    """Return the resolution of a timeframe in minutes."""
    return _RESOLUTION_MINUTES[tf]


def is_upsampling(source_tf: Timeframe, target_tf: Timeframe) -> bool:
    """True when projecting a coarse timeframe into a finer one.

    Example: daily feature → hourly index  (upsampling).
    """
    return resolution_minutes(source_tf) > resolution_minutes(target_tf)


def is_downsampling(source_tf: Timeframe, target_tf: Timeframe) -> bool:
    """True when projecting a fine timeframe into a coarser one.

    Example: 15m feature → 1h index  (downsampling).
    """
    return resolution_minutes(source_tf) < resolution_minutes(target_tf)


def validate_alignment_pair(
    source_tf: Timeframe,
    target_tf: Timeframe,
    policy: AlignmentPolicy,
) -> None:
    """Raise InvalidAlignment if the source→target pair is not valid.

    Rules:
      - AlignmentPolicy.NONE: source and target must be the same timeframe.
      - Any other policy: upsampling is always valid (coarse→fine);
        downsampling is forbidden (fine→coarse would lose information).
    """
    if policy == AlignmentPolicy.NONE:
        if source_tf != target_tf:
            raise InvalidAlignment(
                f"AlignmentPolicy.NONE requires source==target, "
                f"got {source_tf!r}→{target_tf!r}"
            )
        return

    if is_downsampling(source_tf, target_tf):
        raise InvalidAlignment(
            f"Cannot downsample {source_tf!r}→{target_tf!r}: "
            f"alignment only supports upsampling (coarse→fine)"
        )

    if source_tf == target_tf:
        raise InvalidAlignment(
            f"Alignment with policy {policy.value!r} is redundant "
            f"when source==target ({source_tf!r})"
        )


# ------------------------------------------------------------------
# Availability offset (point-in-time safety)
# ------------------------------------------------------------------

def availability_offset(
    rule: AvailabilityRule,
    source_tf: Timeframe,
) -> timedelta:
    """Return the delay that must be applied before a value is usable.

    - AT_CLOSE: the value becomes available at the end of the source bar,
      so a bar at 14:00 (1h) is available at 15:00 → offset = 1 bar.
    - NEXT_SESSION: the value is available only on the *next trading day*.
      For daily features this means +1d; for intraday it means +1d as well
      (the value is not usable during the same session).
    - IMMEDIATE: zero offset — the caller must ensure this is safe.
    """
    if rule == AvailabilityRule.IMMEDIATE:
        return timedelta(0)

    if rule == AvailabilityRule.AT_CLOSE:
        return timedelta(minutes=resolution_minutes(source_tf))

    if rule == AvailabilityRule.NEXT_SESSION:
        return timedelta(days=1)

    raise InvalidAlignment(f"Unknown AvailabilityRule: {rule!r}")


def make_available_index(
    source_index: pd.DatetimeIndex,
    rule: AvailabilityRule,
    source_tf: Timeframe,
) -> pd.DatetimeIndex:
    """Shift *source_index* by the availability offset.

    The resulting index contains the timestamps **from which** each
    source value may legally be used.
    """
    offset = availability_offset(rule, source_tf)
    return source_index + offset
