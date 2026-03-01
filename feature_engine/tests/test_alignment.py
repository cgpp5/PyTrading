"""Tests for Phase 3 — Temporal alignment and synchronization.

Test categories:
  A. Rules: timeframe compatibility, availability offsets.
  B. Forward-fill: point-in-time safety, correct propagation.
  C. Linear interpolation: intermediate values, no extrapolation.
  D. Stepwise: same shape as ffill, declared explicitly.
  E. Aligner (orchestrator): dispatches correctly, quality degradation.
  F. Leakage prevention: no value visible before its availability time.
"""

from __future__ import annotations

from datetime import datetime, timedelta, timezone

import numpy as np
import pandas as pd
import pytest

from feature_engine.alignment.aligner import AlignedResult, align
from feature_engine.alignment.forward_fill import forward_fill
from feature_engine.alignment.resample import linear_interpolation, stepwise
from feature_engine.alignment.rules import (
    availability_offset,
    is_downsampling,
    is_upsampling,
    make_available_index,
    resolution_minutes,
    validate_alignment_pair,
)
from feature_engine.errors import InvalidAlignment
from feature_engine.feature_spec.enums import (
    AlignmentPolicy,
    FeatureCategory,
    WarmupPolicy,
)
from feature_engine.feature_spec.quality import FeatureQuality
from feature_engine.feature_spec.spec import FeatureSpec
from feature_engine.feature_spec.temporal import AvailabilityRule


# ------------------------------------------------------------------
# Helpers
# ------------------------------------------------------------------

def _daily_index(n: int, start: str = "2026-01-05") -> pd.DatetimeIndex:
    return pd.date_range(start, periods=n, freq="1D", tz="UTC")


def _hourly_index(n: int, start: str = "2026-01-05 09:30") -> pd.DatetimeIndex:
    return pd.date_range(start, periods=n, freq="1h", tz="UTC")


def _make_spec(
    timeframe: str = "1d",
    alignment: AlignmentPolicy = AlignmentPolicy.NONE,
    availability: AvailabilityRule | None = None,
    degrades: bool = False,
) -> FeatureSpec:
    return FeatureSpec(
        name="test_feature",
        version="1.0",
        category=FeatureCategory.TECHNICAL,
        timeframe=timeframe,
        alignment=alignment,
        availability=availability,
        degrades_on_alignment=degrades,
    )


# ==================================================================
# A. Rules
# ==================================================================

class TestRules:

    def test_resolution_minutes(self):
        assert resolution_minutes("15m") == 15
        assert resolution_minutes("1h") == 60
        assert resolution_minutes("4h") == 240
        assert resolution_minutes("1d") == 1440

    def test_is_upsampling(self):
        assert is_upsampling("1d", "1h")
        assert is_upsampling("4h", "1h")
        assert not is_upsampling("1h", "1d")
        assert not is_upsampling("1h", "1h")

    def test_is_downsampling(self):
        assert is_downsampling("1h", "1d")
        assert not is_downsampling("1d", "1h")

    def test_validate_none_same_tf_ok(self):
        validate_alignment_pair("1h", "1h", AlignmentPolicy.NONE)

    def test_validate_none_different_tf_raises(self):
        with pytest.raises(InvalidAlignment, match="NONE requires source==target"):
            validate_alignment_pair("1d", "1h", AlignmentPolicy.NONE)

    def test_validate_downsampling_raises(self):
        with pytest.raises(InvalidAlignment, match="Cannot downsample"):
            validate_alignment_pair("1h", "1d", AlignmentPolicy.FORWARD_FILL)

    def test_validate_same_tf_with_policy_raises(self):
        with pytest.raises(InvalidAlignment, match="redundant"):
            validate_alignment_pair("1h", "1h", AlignmentPolicy.FORWARD_FILL)

    def test_validate_upsampling_ok(self):
        validate_alignment_pair("1d", "1h", AlignmentPolicy.FORWARD_FILL)
        validate_alignment_pair("1d", "1h", AlignmentPolicy.LINEAR_INTERPOLATION)
        validate_alignment_pair("4h", "1h", AlignmentPolicy.STEPWISE)


# ==================================================================
# A2. Availability offsets
# ==================================================================

class TestAvailabilityOffset:

    def test_immediate_is_zero(self):
        assert availability_offset(AvailabilityRule.IMMEDIATE, "1h") == timedelta(0)

    def test_at_close_equals_one_bar(self):
        assert availability_offset(AvailabilityRule.AT_CLOSE, "1h") == timedelta(hours=1)
        assert availability_offset(AvailabilityRule.AT_CLOSE, "1d") == timedelta(days=1)
        assert availability_offset(AvailabilityRule.AT_CLOSE, "15m") == timedelta(minutes=15)

    def test_next_session_is_one_day(self):
        assert availability_offset(AvailabilityRule.NEXT_SESSION, "1d") == timedelta(days=1)
        assert availability_offset(AvailabilityRule.NEXT_SESSION, "1h") == timedelta(days=1)

    def test_make_available_index(self):
        idx = _daily_index(3)  # Jan 5, 6, 7
        shifted = make_available_index(idx, AvailabilityRule.AT_CLOSE, "1d")
        assert (shifted == idx + timedelta(days=1)).all()


# ==================================================================
# B. Forward-fill
# ==================================================================

class TestForwardFill:

    def test_daily_to_hourly_basic(self):
        """Daily feature available AT_CLOSE projected to hourly bars."""
        # Source: 3 daily values
        source_idx = _daily_index(3)  # Jan 5, 6, 7
        values = pd.Series([10.0, 20.0, 30.0], index=source_idx)

        # Target: hourly bars on Jan 6 (after AT_CLOSE of Jan 5 is available)
        target_idx = _hourly_index(6, start="2026-01-06 09:30")

        result = forward_fill(values, "1d", target_idx, AvailabilityRule.AT_CLOSE)

        assert len(result) == 6
        # AT_CLOSE offset for 1d = +1 day.
        # Value 10.0 (Jan 5) becomes available Jan 6 → visible in all Jan 6 bars.
        # Value 20.0 (Jan 6) becomes available Jan 7 → NOT visible on Jan 6.
        assert (result == 10.0).all()

    def test_leading_nan_before_first_available(self):
        """Bars before the first available value must be NaN."""
        source_idx = _daily_index(1, start="2026-01-06")
        values = pd.Series([42.0], index=source_idx)

        # Target starts before the first available (Jan 7 with AT_CLOSE+1d)
        target_idx = _hourly_index(3, start="2026-01-06 10:00")

        result = forward_fill(values, "1d", target_idx, AvailabilityRule.AT_CLOSE)
        assert result.isna().all()

    def test_immediate_availability(self):
        """IMMEDIATE availability means zero offset."""
        source_idx = _daily_index(2)  # Jan 5, 6
        values = pd.Series([100.0, 200.0], index=source_idx)

        # Target hourly on Jan 5 itself
        target_idx = _hourly_index(4, start="2026-01-05 00:00")

        result = forward_fill(values, "1d", target_idx, AvailabilityRule.IMMEDIATE)
        # Value 100.0 is available at Jan 5 00:00 (same time)
        assert (result == 100.0).all()


# ==================================================================
# C. Linear interpolation
# ==================================================================

class TestLinearInterpolation:

    def test_interpolates_between_points(self):
        """Values midway between two source points should be interpolated."""
        # Two daily points: 10 and 30
        source_idx = pd.to_datetime(
            ["2026-01-05", "2026-01-07"], utc=True
        )
        values = pd.Series([10.0, 30.0], index=source_idx)

        # Target: Jan 5, 6, 7 — daily with IMMEDIATE availability
        target_idx = _daily_index(3, start="2026-01-05")

        result = linear_interpolation(
            values, "1d", target_idx, AvailabilityRule.IMMEDIATE,
        )

        assert result.iloc[0] == pytest.approx(10.0)
        assert result.iloc[1] == pytest.approx(20.0)  # interpolated midpoint
        assert result.iloc[2] == pytest.approx(30.0)

    def test_no_extrapolation_before_first(self):
        """Values before the first source point must be NaN."""
        source_idx = _daily_index(2, start="2026-01-06")
        values = pd.Series([10.0, 20.0], index=source_idx)

        target_idx = _daily_index(4, start="2026-01-05")

        result = linear_interpolation(
            values, "1d", target_idx, AvailabilityRule.IMMEDIATE,
        )
        assert pd.isna(result.iloc[0])  # Jan 5 — before first source

    def test_at_close_offset_applied(self):
        """AT_CLOSE offset must shift availability before interpolating."""
        # Source: daily at Jan 5 (value=10) and Jan 7 (value=30)
        source_idx = pd.to_datetime(
            ["2026-01-05", "2026-01-07"], utc=True
        )
        values = pd.Series([10.0, 30.0], index=source_idx)

        # With AT_CLOSE+1d, available at Jan 6 and Jan 8
        # Target: Jan 6, 7 → should interpolate between the shifted times
        target_idx = _daily_index(2, start="2026-01-06")

        result = linear_interpolation(
            values, "1d", target_idx, AvailabilityRule.AT_CLOSE,
        )
        assert result.iloc[0] == pytest.approx(10.0)  # Jan 6 = first available
        assert result.iloc[1] == pytest.approx(20.0)  # Jan 7 = midpoint


# ==================================================================
# D. Stepwise
# ==================================================================

class TestStepwise:

    def test_stepwise_holds_value(self):
        """Stepwise should hold previous value like forward_fill."""
        source_idx = _daily_index(2)
        values = pd.Series([50.0, 100.0], index=source_idx)

        target_idx = _hourly_index(4, start="2026-01-06 10:00")

        result_step = stepwise(values, "1d", target_idx, AvailabilityRule.AT_CLOSE)
        result_ffill = forward_fill(values, "1d", target_idx, AvailabilityRule.AT_CLOSE)

        # Mechanically identical
        pd.testing.assert_series_equal(result_step, result_ffill)


# ==================================================================
# E. Aligner (orchestrator)
# ==================================================================

class TestAligner:

    def test_none_policy_same_tf(self):
        """NONE policy: values pass through on matching timeframe."""
        idx = _hourly_index(3)
        values = pd.Series([1.0, 2.0, 3.0], index=idx)
        spec = _make_spec(timeframe="1h", alignment=AlignmentPolicy.NONE)

        result = align(values, spec, idx, "1h")

        assert isinstance(result, AlignedResult)
        assert result.quality == FeatureQuality.READY
        assert result.policy_applied == AlignmentPolicy.NONE
        pd.testing.assert_series_equal(result.values, values)

    def test_none_policy_different_tf_raises(self):
        """NONE policy with mismatched timeframes must raise."""
        spec = _make_spec(timeframe="1d", alignment=AlignmentPolicy.NONE)
        with pytest.raises(InvalidAlignment):
            align(pd.Series(), spec, _hourly_index(1), "1h")

    def test_forward_fill_dispatch(self):
        """Aligner dispatches to forward_fill when policy says so."""
        source_idx = _daily_index(2)
        values = pd.Series([10.0, 20.0], index=source_idx)
        spec = _make_spec(
            timeframe="1d",
            alignment=AlignmentPolicy.FORWARD_FILL,
            availability=AvailabilityRule.AT_CLOSE,
        )
        target_idx = _hourly_index(3, start="2026-01-06 10:00")

        result = align(values, spec, target_idx, "1h")

        assert result.policy_applied == AlignmentPolicy.FORWARD_FILL
        assert result.quality == FeatureQuality.READY
        assert (result.values == 10.0).all()

    def test_linear_interpolation_dispatch(self):
        """Aligner dispatches to linear_interpolation."""
        source_idx = pd.to_datetime(
            ["2026-01-05", "2026-01-07"], utc=True
        )
        values = pd.Series([10.0, 30.0], index=source_idx)
        spec = _make_spec(
            timeframe="1d",
            alignment=AlignmentPolicy.LINEAR_INTERPOLATION,
            availability=AvailabilityRule.IMMEDIATE,
        )
        target_idx = _daily_index(3, start="2026-01-05")

        result = align(values, spec, target_idx, "1h")

        assert result.policy_applied == AlignmentPolicy.LINEAR_INTERPOLATION
        assert result.values.iloc[1] == pytest.approx(20.0)

    def test_stepwise_dispatch(self):
        """Aligner dispatches to stepwise."""
        source_idx = _daily_index(2)
        values = pd.Series([50.0, 100.0], index=source_idx)
        spec = _make_spec(
            timeframe="1d",
            alignment=AlignmentPolicy.STEPWISE,
            availability=AvailabilityRule.AT_CLOSE,
        )
        target_idx = _hourly_index(3, start="2026-01-06 10:00")

        result = align(values, spec, target_idx, "1h")
        assert result.policy_applied == AlignmentPolicy.STEPWISE

    def test_degrades_on_alignment(self):
        """If spec declares degrades_on_alignment, quality must be DEGRADED."""
        source_idx = _daily_index(2)
        values = pd.Series([10.0, 20.0], index=source_idx)
        spec = _make_spec(
            timeframe="1d",
            alignment=AlignmentPolicy.FORWARD_FILL,
            availability=AvailabilityRule.AT_CLOSE,
            degrades=True,
        )
        target_idx = _hourly_index(3, start="2026-01-06 10:00")

        result = align(values, spec, target_idx, "1h")
        assert result.quality == FeatureQuality.DEGRADED

    def test_alignment_without_availability_raises(self):
        """Alignment policy != NONE requires availability."""
        spec = FeatureSpec(
            name="no_avail",
            version="1.0",
            category=FeatureCategory.TECHNICAL,
            timeframe="1d",
            alignment=AlignmentPolicy.NONE,  # create with NONE to pass validation
        )
        # Force alignment by calling align with a different policy
        # We must make a spec with FORWARD_FILL + availability
        # Actually, the spec constructor already prevents this, so let's test
        # at the aligner level by manually creating a spec with NONE and calling
        # align with policy override — but spec is frozen. Instead test that
        # spec creation itself rejects it:
        with pytest.raises(ValueError, match="AvailabilityRule"):
            FeatureSpec(
                name="bad",
                version="1.0",
                category=FeatureCategory.TECHNICAL,
                timeframe="1d",
                alignment=AlignmentPolicy.FORWARD_FILL,
                # availability not set → should raise
            )


# ==================================================================
# F. Leakage prevention (critical)
# ==================================================================

class TestLeakagePrevention:

    def test_daily_feature_not_visible_same_day_at_close(self):
        """A daily feature (AT_CLOSE) must NOT be visible on the same day
        in an hourly index — only the next day."""
        # Daily source: Jan 5 = 100
        source_idx = _daily_index(1, start="2026-01-05")
        values = pd.Series([100.0], index=source_idx)

        # Hourly target: Jan 5 10:00 – 15:00 (same day)
        target_idx = _hourly_index(6, start="2026-01-05 10:00")

        result = forward_fill(values, "1d", target_idx, AvailabilityRule.AT_CLOSE)
        # AT_CLOSE + 1d means available Jan 6 → all Jan 5 bars must be NaN
        assert result.isna().all()

    def test_next_session_not_visible_same_session(self):
        """NEXT_SESSION availability must hide the value until the next day."""
        source_idx = _daily_index(1, start="2026-01-05")
        values = pd.Series([42.0], index=source_idx)

        # Target: same day hourly
        target_idx = _hourly_index(6, start="2026-01-05 09:30")

        result = forward_fill(
            values, "1d", target_idx, AvailabilityRule.NEXT_SESSION,
        )
        assert result.isna().all()

    def test_hourly_feature_not_visible_in_same_bar(self):
        """1h feature AT_CLOSE at 09:30 is available at 10:30, not 09:30-10:29."""
        source_idx = pd.DatetimeIndex(
            [datetime(2026, 1, 5, 9, 30, tzinfo=timezone.utc)]
        )
        values = pd.Series([77.0], index=source_idx)

        # 15m bars within the same hour
        target_idx = pd.date_range(
            "2026-01-05 09:30", periods=4, freq="15min", tz="UTC",
        )

        result = forward_fill(values, "1h", target_idx, AvailabilityRule.AT_CLOSE)
        # Available at 10:30, all 4 bars (09:30–10:15) are before that → NaN
        assert result.isna().all()

    def test_hourly_feature_visible_after_offset(self):
        """1h feature AT_CLOSE at 09:30 must be visible at 10:30."""
        source_idx = pd.DatetimeIndex(
            [datetime(2026, 1, 5, 9, 30, tzinfo=timezone.utc)]
        )
        values = pd.Series([77.0], index=source_idx)

        # 15m bars starting at 10:30 (after availability)
        target_idx = pd.date_range(
            "2026-01-05 10:30", periods=4, freq="15min", tz="UTC",
        )

        result = forward_fill(values, "1h", target_idx, AvailabilityRule.AT_CLOSE)
        assert (result == 77.0).all()

    def test_interpolation_no_leakage(self):
        """Linear interpolation must also respect availability offset."""
        # Source: daily Jan 5=10, Jan 7=30, AT_CLOSE → available Jan 6, Jan 8
        source_idx = pd.to_datetime(["2026-01-05", "2026-01-07"], utc=True)
        values = pd.Series([10.0, 30.0], index=source_idx)

        # Target: Jan 5 — before any availability
        target_on_jan5 = _daily_index(1, start="2026-01-05")

        result = linear_interpolation(
            values, "1d", target_on_jan5, AvailabilityRule.AT_CLOSE,
        )
        assert result.isna().all(), "Jan 5 must be NaN (first available is Jan 6)"
