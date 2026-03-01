import pytest

from feature_engine.feature_spec.spec import FeatureSpec
from feature_engine.feature_spec.enums import (
    FeatureCategory,
    AlignmentPolicy,
    InterpolationPolicy,
    WarmupPolicy,
)
from feature_engine.feature_spec.temporal import AvailabilityRule


def test_valid_external_series_spec():
    spec = FeatureSpec(
        name="mcclellan_oscillator",
        version="1.0",
        category=FeatureCategory.EXTERNAL_SERIES,
        timeframe="1d",
        availability=AvailabilityRule.NEXT_SESSION,
        alignment=AlignmentPolicy.LINEAR_INTERPOLATION,
        external_sources=("mcclellan_csv_v1",),
        interpolation=InterpolationPolicy.LINEAR,
        degrades_on_alignment=True,
    )
    assert spec.name == "mcclellan_oscillator"


def test_external_series_requires_external_source():
    with pytest.raises(ValueError):
        FeatureSpec(
            name="broken_external",
            version="1.0",
            category=FeatureCategory.EXTERNAL_SERIES,
            timeframe="1d",
            availability=AvailabilityRule.NEXT_SESSION,
            alignment=AlignmentPolicy.NONE,
        )


def test_interpolation_only_allowed_for_external_series():
    with pytest.raises(ValueError):
        FeatureSpec(
            name="bad_interpolation",
            version="1.0",
            category=FeatureCategory.TECHNICAL,
            timeframe="1d",
            availability=AvailabilityRule.AT_CLOSE,
            alignment=AlignmentPolicy.NONE,
            interpolation=InterpolationPolicy.LINEAR,
        )


def test_negative_lookback_is_invalid():
    with pytest.raises(ValueError):
        FeatureSpec(
            name="bad_lookback",
            version="1.0",
            category=FeatureCategory.TECHNICAL,
            timeframe="1d",
            availability=AvailabilityRule.AT_CLOSE,
            alignment=AlignmentPolicy.NONE,
            lookback_required=-1,
        )


def test_lookback_requires_warmup_policy():
    with pytest.raises(ValueError):
        FeatureSpec(
            name="missing_warmup",
            version="1.0",
            category=FeatureCategory.TECHNICAL,
            timeframe="1d",
            availability=AvailabilityRule.AT_CLOSE,
            alignment=AlignmentPolicy.NONE,
            lookback_required=14,
            warmup_policy=WarmupPolicy.NONE,
        )


def test_valid_technical_feature_with_lookback():
    spec = FeatureSpec(
        name="rsi_14",
        version="1.0",
        category=FeatureCategory.TECHNICAL,
        timeframe="1h",
        availability=AvailabilityRule.AT_CLOSE,
        alignment=AlignmentPolicy.NONE,
        lookback_required=14,
        warmup_policy=WarmupPolicy.FIXED_LOOKBACK,
    )
    assert spec.lookback_required == 14


def test_derived_requires_depends_on():
    with pytest.raises(ValueError):
        FeatureSpec(
            name="bad_derived",
            version="1.0",
            category=FeatureCategory.DERIVED,
            timeframe="1d",
            alignment=AlignmentPolicy.NONE,
        )


def test_valid_derived_with_depends_on():
    spec = FeatureSpec(
        name="spread",
        version="1.0",
        category=FeatureCategory.DERIVED,
        timeframe="1d",
        alignment=AlignmentPolicy.NONE,
        depends_on=("close", "sma_20"),
    )
    assert spec.depends_on == ("close", "sma_20")


def test_availability_defaults_to_none():
    spec = FeatureSpec(
        name="simple",
        version="1.0",
        category=FeatureCategory.TECHNICAL,
        timeframe="1d",
        alignment=AlignmentPolicy.NONE,
    )
    assert spec.availability is None


def test_invalid_timeframe_raises():
    with pytest.raises(ValueError):
        FeatureSpec(
            name="bad_tf",
            version="1.0",
            category=FeatureCategory.TECHNICAL,
            timeframe="2h",  # type: ignore
            alignment=AlignmentPolicy.NONE,
        )
