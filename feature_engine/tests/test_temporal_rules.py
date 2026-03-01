import pytest

from feature_engine.feature_spec.spec import FeatureSpec
from feature_engine.feature_spec.enums import (
    FeatureCategory,
    AlignmentPolicy,
)
from feature_engine.feature_spec.temporal import AvailabilityRule


def test_alignment_requires_availability():
    with pytest.raises(ValueError):
        FeatureSpec(
            name="bad_feature",
            version="1.0",
            category=FeatureCategory.TECHNICAL,
            timeframe="1d",
            availability=None,  # type: ignore
            alignment=AlignmentPolicy.FORWARD_FILL,
        )


def test_no_alignment_allows_availability():
    spec = FeatureSpec(
        name="simple_feature",
        version="1.0",
        category=FeatureCategory.TECHNICAL,
        timeframe="1d",
        availability=AvailabilityRule.AT_CLOSE,
        alignment=AlignmentPolicy.NONE,
    )
    assert spec.alignment == AlignmentPolicy.NONE
