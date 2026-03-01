from enum import Enum


class FeatureCategory(Enum):
    TECHNICAL = "technical"
    DERIVED = "derived"
    EXTERNAL_SERIES = "external_series"
    META = "meta"


class AlignmentPolicy(Enum):
    NONE = "none"
    FORWARD_FILL = "forward_fill"
    LINEAR_INTERPOLATION = "linear_interpolation"
    STEPWISE = "stepwise"


class InterpolationPolicy(Enum):
    DISALLOW = "disallow"
    LINEAR = "linear"
    FORWARD_ONLY = "forward_only"


class WarmupPolicy(Enum):
    NONE = "none"
    FIXED_LOOKBACK = "fixed_lookback"
    DEPENDENCY_DRIVEN = "dependency_driven"
