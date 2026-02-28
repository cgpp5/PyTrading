from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
from typing import Sequence

import pandas as pd

from .calendar import MarketCalendarResolver
from .errors import ProviderError
from .normalize import empty_ohlcv_dataframe, normalize_ohlcv
from .observability import Observability
from .timeframes import validate_timeframe
from .types import MarketData, MarketDataMeta
from .providers.base import MarketDataProvider


@dataclass(frozen=True)
class ProviderTier:
    provider: MarketDataProvider
    quality: str  # "normal" | "degraded" | "dirty"


class MarketFeed:
    def __init__(
        self,
        tiers: Sequence[ProviderTier],
        calendar_resolver: MarketCalendarResolver,
        observability: Observability,
    ):
        if not tiers:
            raise ValueError("MarketFeed requires at least one provider tier.")
        self._tiers = list(tiers)
        self._cal = calendar_resolver
        self._obs = observability

    def get_ohlcv(
        self,
        symbol: str,
        timeframe: str,
        start: datetime,
        end: datetime,
        *,
        allow_fallback: bool = True,
    ) -> MarketData:
        tf = validate_timeframe(timeframe)

        calendar = self._cal.resolve(symbol)
        expected = calendar.expected_bars(timeframe=tf, start=start, end=end)  # stub en Fase 0

        attempted: list[str] = []
        last_provider_error: str | None = None

        for idx, tier in enumerate(self._tiers):
            if idx > 0 and not allow_fallback:
                break

            p = tier.provider
            attempted.append(p.name)

            try:
                raw = p.fetch_ohlcv(symbol=symbol, timeframe=tf, start=start, end=end)
            except ProviderError as e:
                last_provider_error = str(e)
                self._obs.log_warning(
                    "provider_failure",
                    provider=p.name,
                    symbol=symbol,
                    timeframe=tf,
                    error=str(e),
                )
                continue

            # Cualquier error aquí es interno (no se silencia)
            df = normalize_ohlcv(raw, provider_name=p.name, quality=tier.quality)

            meta = MarketDataMeta(
                symbol=symbol,
                timeframe=tf,
                provider_used=p.name,
                fallback_used=(idx > 0),
                start=start,
                end=end,
                coverage_ratio=0.0,  # Fase 5
                gap_count=0,         # Fase 5
                quality=tier.quality,
                notes=None,
                extra={"attempted_providers": attempted, "calendar": calendar.name, "expected_count": len(expected)},
            )
            return MarketData(df=df, meta=meta)

        self._obs.log_error(
            "all_providers_failed",
            symbol=symbol,
            timeframe=tf,
            attempted_providers=attempted,
            last_error=last_provider_error,
        )

        empty = empty_ohlcv_dataframe()
        meta = MarketDataMeta(
            symbol=symbol,
            timeframe=tf,
            provider_used="none",
            fallback_used=False,
            start=start,
            end=end,
            coverage_ratio=0.0,
            gap_count=len(expected),
            quality="degraded",
            notes="All providers failed",
            extra={"attempted_providers": attempted, "calendar": calendar.name, "expected_count": len(expected)},
        )
        return MarketData(df=empty, meta=meta)
