from dataclasses import dataclass, field
from typing import Tuple, Optional

from market_feed.timeframes import Timeframe, validate_timeframe

from .enums import (
    FeatureCategory,
    AlignmentPolicy,
    InterpolationPolicy,
    WarmupPolicy,
)
from .temporal import AvailabilityRule, validate_availability


@dataclass(frozen=True)
class FeatureSpec:
    # Identity
    name: str
    version: str
    category: FeatureCategory

    # Temporal semantics
    timeframe: Timeframe
    alignment: AlignmentPolicy

    # Dependencies
    depends_on: Tuple[str, ...] = field(default_factory=tuple)
    external_sources: Tuple[str, ...] = field(default_factory=tuple)

    # Temporal availability (Optional: only required when alignment != NONE)
    availability: Optional[AvailabilityRule] = None

    # Maturity
    lookback_required: int = 0
    warmup_policy: WarmupPolicy = WarmupPolicy.NONE

    # Quality & interpolation
    interpolation: Optional[InterpolationPolicy] = None
    degrades_on_alignment: bool = False

    def __post_init__(self):
        validate_timeframe(self.timeframe)
        self._validate_identity()
        self._validate_temporal_semantics()
        self._validate_dependencies()
        self._validate_maturity()
        self._validate_quality_rules()

    def _validate_identity(self):
        if not self.name:
            raise ValueError("FeatureSpec.name must be non-empty")
        if not self.version:
            raise ValueError("FeatureSpec.version must be non-empty")

    def _validate_temporal_semantics(self):
        validate_availability(self.availability, self.alignment)

    def _validate_dependencies(self):
        if self.category == FeatureCategory.EXTERNAL_SERIES:
            if not self.external_sources:
                raise ValueError(
                    "EXTERNAL_SERIES features must declare external_sources"
                )
        if self.category == FeatureCategory.DERIVED:
            if not self.depends_on:
                raise ValueError(
                    "DERIVED features must declare depends_on"
                )

    def _validate_maturity(self):
        if self.lookback_required < 0:
            raise ValueError("lookback_required cannot be negative")

        if self.lookback_required > 0 and self.warmup_policy == WarmupPolicy.NONE:
            raise ValueError(
                "Features with lookback_required must define a warmup_policy"
            )

    def _validate_quality_rules(self):
        if self.interpolation is not None:
            if self.category != FeatureCategory.EXTERNAL_SERIES:
                raise ValueError(
                    "InterpolationPolicy is only valid for EXTERNAL_SERIES features"
                )
