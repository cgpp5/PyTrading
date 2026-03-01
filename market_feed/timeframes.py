from typing import Literal

Timeframe = Literal["15m", "1h", "4h", "1d"]

_ALLOWED = {"15m", "1h", "4h", "1d"}


def validate_timeframe(tf: str) -> Timeframe:
    if tf not in _ALLOWED:
        raise ValueError(f"Unsupported timeframe: {tf}. Allowed: {sorted(_ALLOWED)}")
    return tf  # type: ignore[return-value]
