from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
from typing import Any, Literal, Optional

import pandas as pd

Quality = Literal["normal", "degraded", "dirty"]


@dataclass(frozen=True)
class MarketDataMeta:
    symbol: str
    timeframe: str
    provider_used: str
    fallback_used: bool
    start: datetime
    end: datetime
    coverage_ratio: float
    gap_count: int
    quality: Quality
    notes: Optional[str] = None
    extra: Optional[dict[str, Any]] = None


@dataclass(frozen=True)
class MarketData:
    df: pd.DataFrame
    meta: MarketDataMeta
