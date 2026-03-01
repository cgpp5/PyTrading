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
        import time

        start_total = time.perf_counter()

        tf = validate_timeframe(timeframe)

        # ------------------------------------------------------------
        # Fase 6: timeframe base siempre 1h para agregaciones
        # ------------------------------------------------------------
        base_tf = "1h" if tf in {"4h"} else tf

        calendar = self._cal

        attempted: list[str] = []
        last_provider_error: str | None = None

        for idx, tier in enumerate(self._tiers):
            if idx > 0 and not allow_fallback:
                break

            provider = tier.provider
            attempted.append(provider.name)

            # ------------------------------------------------------------
            # Observability: intento de provider
            # ------------------------------------------------------------
            self._obs.record_provider_attempt(
                provider=provider.name,
                symbol=symbol,
                timeframe=base_tf,
                tier=idx,
            )

            start_provider = time.perf_counter()

            try:
                raw = provider.fetch_ohlcv(
                    symbol=symbol,
                    timeframe=base_tf,
                    start=start,
                    end=end,
                )
            except ProviderError as e:
                last_provider_error = str(e)

                # --------------------------------------------------------
                # Observability: fallo de provider
                # --------------------------------------------------------
                self._obs.record_provider_failure(
                    provider=provider.name,
                    symbol=symbol,
                    timeframe=base_tf,
                    error=str(e),
                )

                self._obs.log_warning(
                    "provider_failure",
                    provider=provider.name,
                    symbol=symbol,
                    timeframe=base_tf,
                    error=str(e),
                )
                continue

            # ------------------------------------------------------------
            # Observability: latencia por provider
            # ------------------------------------------------------------
            elapsed_ms = (time.perf_counter() - start_provider) * 1000
            self._obs.record_provider_latency(
                provider=provider.name,
                symbol=symbol,
                timeframe=base_tf,
                elapsed_ms=elapsed_ms,
            )

            # ------------------------------------------------------------
            # Observability: éxito de provider
            # ------------------------------------------------------------
            self._obs.record_provider_success(
                provider=provider.name,
                symbol=symbol,
                timeframe=base_tf,
            )

            # ------------------------------------------------------------
            # Normalización canónica
            # ------------------------------------------------------------
            df = normalize_ohlcv(
                raw,
                provider_name=provider.name,
                quality=tier.quality,
            )

            # ------------------------------------------------------------
            # Fase 5: detección real de gaps intradía
            # ------------------------------------------------------------
            gap_count = 0
            total_expected = 0

            if base_tf == "1h":
                sessions = calendar.get_session_info(
                    symbol=symbol,
                    start=start,
                    end=end,
                )

                for session in sessions:
                    df_session = df.loc[
                        (df.index >= session.market_open) &
                        (df.index < session.market_close)
                    ]

                    total_expected += session.expected_bars

                    if len(df_session) < session.expected_bars:
                        gap_count += 1
                        df.loc[df_session.index, "is_gap"] = True

            coverage_ratio = (
                len(df) / total_expected
                if total_expected > 0
                else 0.0
            )

            # ------------------------------------------------------------
            # Fase 6: agregación automática si procede
            # ------------------------------------------------------------
            if tf == "4h":
                df = aggregate_4h_aligned(
                    df_1h=df,
                    session_start_hour=None,
                    session_start_minute=None,
                    session_end_hour=None,
                    session_end_minute=None,
                )

            # ------------------------------------------------------------
            # Política de quality (decisión explícita)
            # ------------------------------------------------------------
            MIN_COVERAGE = 0.85
            has_gap = bool(df["is_gap"].any())

            final_quality = (
                "degraded"
                if has_gap or coverage_ratio < MIN_COVERAGE
                else tier.quality
            )

            # ------------------------------------------------------------
            # Observability: fallback usado
            # ------------------------------------------------------------
            if idx > 0:
                self._obs.record_fallback_used(
                    symbol=symbol,
                    timeframe=base_tf,
                    attempted_providers=attempted,
                )

            # ------------------------------------------------------------
            # Observability: calidad de datos
            # ------------------------------------------------------------
            self._obs.record_data_quality(
                symbol=symbol,
                timeframe=tf,
                quality=final_quality,
                coverage_ratio=coverage_ratio,
                gap_count=gap_count,
            )

            # ------------------------------------------------------------
            # Observability: latencia total
            # ------------------------------------------------------------
            total_elapsed_ms = (time.perf_counter() - start_total) * 1000
            self._obs.record_total_latency(
                symbol=symbol,
                timeframe=tf,
                elapsed_ms=total_elapsed_ms,
            )

            meta = MarketDataMeta(
                symbol=symbol,
                timeframe=tf,
                provider_used=provider.name,
                fallback_used=(idx > 0),
                start=start,
                end=end,
                coverage_ratio=coverage_ratio,
                gap_count=gap_count,
                quality=final_quality,
                notes=None,
                extra={
                    "attempted_providers": attempted,
                    "calendar": self._cal.resolve(symbol).name,
                },
            )

            return MarketData(df=df, meta=meta)

        # ------------------------------------------------------------
        # Todos los proveedores fallaron
        # ------------------------------------------------------------
        self._obs.log_error(
            "all_providers_failed",
            symbol=symbol,
            timeframe=tf,
            attempted_providers=attempted,
            last_error=last_provider_error,
        )

        empty = empty_ohlcv_dataframe()

        total_elapsed_ms = (time.perf_counter() - start_total) * 1000
        self._obs.record_total_latency(
            symbol=symbol,
            timeframe=tf,
            elapsed_ms=total_elapsed_ms,
        )

        meta = MarketDataMeta(
            symbol=symbol,
            timeframe=tf,
            provider_used="none",
            fallback_used=False,
            start=start,
            end=end,
            coverage_ratio=0.0,
            gap_count=0,
            quality="degraded",
            notes="All providers failed",
            extra={
                "attempted_providers": attempted,
                "calendar": self._cal.resolve(symbol).name,
            },
        )

        return MarketData(df=empty, meta=meta)
