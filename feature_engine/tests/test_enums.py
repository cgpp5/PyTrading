from feature_engine.feature_spec.enums import (
    FeatureCategory,
    AlignmentPolicy,
    InterpolationPolicy,
    WarmupPolicy,
)
from feature_engine.feature_spec.temporal import AvailabilityRule
from feature_engine.feature_spec.quality import FeatureQuality


def test_feature_category_values():
    assert FeatureCategory.TECHNICAL.value == "technical"
    assert FeatureCategory.EXTERNAL_SERIES.value == "external_series"


def test_alignment_policy_values():
    assert AlignmentPolicy.NONE.value == "none"
    assert AlignmentPolicy.LINEAR_INTERPOLATION.value == "linear_interpolation"


def test_interpolation_policy_values():
    assert InterpolationPolicy.LINEAR.value == "linear"
    assert InterpolationPolicy.DISALLOW.value == "disallow"


def test_warmup_policy_values():
    assert WarmupPolicy.NONE.value == "none"
    assert WarmupPolicy.FIXED_LOOKBACK.value == "fixed_lookback"


def test_availability_rule_values():
    assert AvailabilityRule.AT_CLOSE.value == "at_close"
    assert AvailabilityRule.NEXT_SESSION.value == "next_session"


def test_feature_quality_values():
    assert FeatureQuality.READY.value == "ready"
    assert FeatureQuality.DEGRADED.value == "degraded"
    assert FeatureQuality.WARMUP.value == "warmup"
    assert FeatureQuality.MISSING.value == "missing"


# --- B4: Quality transitions ---

from feature_engine.feature_spec.quality import can_transition, VALID_TRANSITIONS


def test_quality_self_transition_always_valid():
    for state in FeatureQuality:
        assert can_transition(state, state)


def test_quality_valid_transitions():
    assert can_transition(FeatureQuality.MISSING, FeatureQuality.WARMUP)
    assert can_transition(FeatureQuality.WARMUP, FeatureQuality.READY)
    assert can_transition(FeatureQuality.READY, FeatureQuality.DEGRADED)
    assert can_transition(FeatureQuality.DEGRADED, FeatureQuality.READY)


def test_quality_invalid_transitions():
    assert not can_transition(FeatureQuality.MISSING, FeatureQuality.READY)
    assert not can_transition(FeatureQuality.READY, FeatureQuality.WARMUP)


# --- B3: Temporal validation ---

from feature_engine.feature_spec.temporal import (
    validate_availability,
    is_point_in_time_safe,
)
from feature_engine.feature_spec.enums import AlignmentPolicy


def test_validate_availability_raises_when_alignment_needs_it():
    import pytest
    with pytest.raises(ValueError):
        validate_availability(None, AlignmentPolicy.FORWARD_FILL)


def test_validate_availability_ok_when_no_alignment():
    validate_availability(None, AlignmentPolicy.NONE)  # should not raise


def test_is_point_in_time_safe():
    assert is_point_in_time_safe(AvailabilityRule.AT_CLOSE)
    assert is_point_in_time_safe(AvailabilityRule.NEXT_SESSION)
    assert not is_point_in_time_safe(AvailabilityRule.IMMEDIATE)
