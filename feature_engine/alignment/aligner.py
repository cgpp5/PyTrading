"""Temporal Aligner — public entry point for alignment operations.

The Aligner is the **only** component that external code should call.
It reads the FeatureSpec to decide:
  1. Is alignment needed / valid?
  2. Which strategy to apply (forward_fill, linear interpolation, stepwise).
  3. Whether quality degrades on alignment.

Nothing outside alignment/ may decide timestamps.
"""

from __future__ import annotations

from dataclasses import dataclass

import pandas as pd

from market_feed.timeframes import Timeframe

from feature_engine.errors import InvalidAlignment
from feature_engine.feature_spec.enums import AlignmentPolicy
from feature_engine.feature_spec.quality import FeatureQuality
from feature_engine.feature_spec.spec import FeatureSpec

from .forward_fill import forward_fill
from .resample import linear_interpolation, stepwise
from .rules import validate_alignment_pair


@dataclass(frozen=True)
class AlignedResult:
    """Outcome of a temporal alignment operation.

    Attributes:
        values: Series aligned to the target index.
        quality: Quality state after alignment.
        source_timeframe: Original timeframe of the feature.
        target_timeframe: Timeframe of the target index.
        policy_applied: The AlignmentPolicy that was applied.
    """
    values: pd.Series
    quality: FeatureQuality
    source_timeframe: Timeframe
    target_timeframe: Timeframe
    policy_applied: AlignmentPolicy


def align(
    values: pd.Series,
    spec: FeatureSpec,
    target_index: pd.DatetimeIndex,
    target_tf: Timeframe,
) -> AlignedResult:
    """Align a feature's computed values to a target timeframe index.

    This is the **single public entry point** for all alignment operations.

    Args:
        values: Computed feature values with DatetimeIndex in the
            feature's native timeframe.
        spec: The FeatureSpec that declares alignment policy, availability,
            and quality rules.
        target_index: The DatetimeIndex to project onto.
        target_tf: The timeframe of *target_index*.

    Returns:
        AlignedResult with the projected values and resulting quality.

    Raises:
        InvalidAlignment: If the source→target pair is invalid, or
            if alignment is requested but availability is not set.
    """
    policy = spec.alignment

    # -- NONE: no alignment, source must match target --
    if policy == AlignmentPolicy.NONE:
        validate_alignment_pair(spec.timeframe, target_tf, policy)
        return AlignedResult(
            values=values.reindex(target_index),
            quality=FeatureQuality.READY,
            source_timeframe=spec.timeframe,
            target_timeframe=target_tf,
            policy_applied=policy,
        )

    # -- Alignment requested: validate pair --
    validate_alignment_pair(spec.timeframe, target_tf, policy)

    if spec.availability is None:
        raise InvalidAlignment(
            f"Feature {spec.name!r} requires availability for "
            f"alignment policy {policy.value!r}"
        )

    # -- Dispatch to strategy --
    if policy == AlignmentPolicy.FORWARD_FILL:
        aligned = forward_fill(
            values, spec.timeframe, target_index, spec.availability,
        )
    elif policy == AlignmentPolicy.LINEAR_INTERPOLATION:
        aligned = linear_interpolation(
            values, spec.timeframe, target_index, spec.availability,
        )
    elif policy == AlignmentPolicy.STEPWISE:
        aligned = stepwise(
            values, spec.timeframe, target_index, spec.availability,
        )
    else:
        raise InvalidAlignment(f"Unsupported AlignmentPolicy: {policy!r}")

    # -- Quality degradation --
    quality = (
        FeatureQuality.DEGRADED if spec.degrades_on_alignment
        else FeatureQuality.READY
    )

    return AlignedResult(
        values=aligned,
        quality=quality,
        source_timeframe=spec.timeframe,
        target_timeframe=target_tf,
        policy_applied=policy,
    )
