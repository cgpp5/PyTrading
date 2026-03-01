from __future__ import annotations

import time
from dataclasses import dataclass
from datetime import datetime
from typing import Sequence

import pandas as pd

from .aggregate import aggregate_4h_aligned
from .calendar import MarketCalendarResolver, SessionInfo
from .errors import ProviderError
from .gaps import fill_session_gaps
from .normalize import empty_ohlcv_dataframe, normalize_ohlcv
from .observability import Observability
from .timeframes import validate_timeframe
from .types import Quality, MarketData, MarketDataMeta
from .providers.base import MarketDataProvider


@dataclass(frozen=True)
class ProviderTier:
    provider: MarketDataProvider
    quality: Quality


class MarketFeed:
    """Orquestador central de adquisición de datos de mercado."""

    MIN_COVERAGE = 0.85

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

    # =================================================================
    # API pública
    # =================================================================

    def get_ohlcv(
        self,
        symbol: str,
        timeframe: str,
        start: datetime,
        end: datetime,
        *,
        allow_fallback: bool = True,
    ) -> MarketData:
        start_total = time.perf_counter()

        tf = validate_timeframe(timeframe)
        base_tf = "1h" if tf in {"4h"} else tf

        attempted: list[str] = []
        last_provider_error: str | None = None

        for idx, tier in enumerate(self._tiers):
            if idx > 0 and not allow_fallback:
                break

            provider = tier.provider
            attempted.append(provider.name)

            raw = self._fetch_from_provider(
                provider, symbol, base_tf, start, end, idx,
            )

            if raw is None:
                last_provider_error = f"{provider.name} failed"
                continue

            df, gap_count, coverage_ratio, sessions = (
                self._process_raw_data(
                    raw, provider, tier, symbol, start, end, base_tf, tf,
                )
            )

            final_quality = self._determine_quality(
                df, coverage_ratio, tier.quality,
            )

            self._record_success_observability(
                idx, symbol, base_tf, tf, attempted,
                final_quality, coverage_ratio, gap_count,
                start_total,
            )

            meta = self._build_metadata(
                symbol, tf, provider.name, idx > 0,
                start, end, coverage_ratio, gap_count,
                final_quality, attempted,
            )

            return MarketData(df=df, meta=meta)

        # Todos los proveedores fallaron
        return self._build_failure_response(
            symbol, tf, attempted, last_provider_error, start_total,
        )

    # =================================================================
    # Pipeline interno
    # =================================================================

    def _fetch_from_provider(
        self,
        provider: MarketDataProvider,
        symbol: str,
        base_tf: str,
        start: datetime,
        end: datetime,
        tier_idx: int,
    ) -> pd.DataFrame | None:
        """Intenta obtener datos crudos de un proveedor. Devuelve None si falla."""

        self._obs.record_provider_attempt(
            provider=provider.name,
            symbol=symbol,
            timeframe=base_tf,
            tier=tier_idx,
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
            return None

        elapsed_ms = (time.perf_counter() - start_provider) * 1000
        self._obs.record_provider_latency(
            provider=provider.name,
            symbol=symbol,
            timeframe=base_tf,
            elapsed_ms=elapsed_ms,
        )
        self._obs.record_provider_success(
            provider=provider.name,
            symbol=symbol,
            timeframe=base_tf,
        )

        return raw

    def _process_raw_data(
        self,
        raw: pd.DataFrame,
        provider: MarketDataProvider,
        tier: ProviderTier,
        symbol: str,
        start: datetime,
        end: datetime,
        base_tf: str,
        tf: str,
    ) -> tuple[pd.DataFrame, int, float, list[SessionInfo]]:
        """Normaliza, detecta gaps, agrega si procede.

        Devuelve (df, gap_count, coverage_ratio, sessions).
        """

        df = normalize_ohlcv(
            raw,
            provider_name=provider.name,
            quality=tier.quality,
        )

        sessions = self._cal.get_session_info(
            symbol=symbol,
            start=start,
            end=end,
        )

        df, gap_count, total_expected = self._detect_and_fill_gaps(
            df, sessions, base_tf, provider.name,
        )

        actual_bars = int((~df["is_gap"]).sum()) if not df.empty else 0
        coverage_ratio = (
            actual_bars / total_expected
            if total_expected > 0
            else (1.0 if not df.empty else 0.0)
        )

        if tf == "4h":
            session_bounds = [
                (s.market_open, s.market_close) for s in sessions
            ]
            df = aggregate_4h_aligned(df_1h=df, sessions=session_bounds)

        return df, gap_count, coverage_ratio, sessions

    @staticmethod
    def _detect_and_fill_gaps(
        df: pd.DataFrame,
        sessions: list[SessionInfo],
        base_tf: str,
        provider_name: str,
    ) -> tuple[pd.DataFrame, int, int]:
        """Detecta gaps e inserta filas NaN. Devuelve (df, gap_count, total_expected)."""

        gap_count = 0
        total_expected = 0

        if base_tf in ("1h", "15m"):
            tf_multiplier = 4 if base_tf == "15m" else 1

            for session in sessions:
                total_expected += session.expected_bars * tf_multiplier

                df, inserted = fill_session_gaps(
                    df,
                    session.market_open,
                    session.market_close,
                    base_tf,
                    provider_name,
                )
                gap_count += inserted

        elif base_tf == "1d":
            total_expected = len(sessions)
            if len(df) < total_expected:
                gap_count = total_expected - len(df)

        return df, gap_count, total_expected

    def _determine_quality(
        self,
        df: pd.DataFrame,
        coverage_ratio: float,
        tier_quality: Quality,
    ) -> Quality:
        """Decide la calidad final según gaps y cobertura."""

        has_gap = bool(df["is_gap"].any())

        if has_gap or coverage_ratio < self.MIN_COVERAGE:
            return "degraded"
        return tier_quality

    # =================================================================
    # Observability helpers
    # =================================================================

    def _record_success_observability(
        self,
        tier_idx: int,
        symbol: str,
        base_tf: str,
        tf: str,
        attempted: list[str],
        quality: Quality,
        coverage_ratio: float,
        gap_count: int,
        start_total: float,
    ) -> None:
        if tier_idx > 0:
            self._obs.record_fallback_used(
                symbol=symbol,
                timeframe=base_tf,
                attempted_providers=attempted,
            )

        self._obs.record_data_quality(
            symbol=symbol,
            timeframe=tf,
            quality=quality,
            coverage_ratio=coverage_ratio,
            gap_count=gap_count,
        )

        total_elapsed_ms = (time.perf_counter() - start_total) * 1000
        self._obs.record_total_latency(
            symbol=symbol,
            timeframe=tf,
            elapsed_ms=total_elapsed_ms,
        )

    # =================================================================
    # Response builders
    # =================================================================

    def _build_metadata(
        self,
        symbol: str,
        tf: str,
        provider_used: str,
        fallback_used: bool,
        start: datetime,
        end: datetime,
        coverage_ratio: float,
        gap_count: int,
        quality: Quality,
        attempted: list[str],
        notes: str | None = None,
    ) -> MarketDataMeta:
        return MarketDataMeta(
            symbol=symbol,
            timeframe=tf,
            provider_used=provider_used,
            fallback_used=fallback_used,
            start=start,
            end=end,
            coverage_ratio=coverage_ratio,
            gap_count=gap_count,
            quality=quality,
            notes=notes,
            extra={
                "attempted_providers": attempted,
                "calendar": self._cal.resolve(symbol).name,
            },
        )

    def _build_failure_response(
        self,
        symbol: str,
        tf: str,
        attempted: list[str],
        last_error: str | None,
        start_total: float,
    ) -> MarketData:
        self._obs.log_error(
            "all_providers_failed",
            symbol=symbol,
            timeframe=tf,
            attempted_providers=attempted,
            last_error=last_error,
        )

        total_elapsed_ms = (time.perf_counter() - start_total) * 1000
        self._obs.record_total_latency(
            symbol=symbol,
            timeframe=tf,
            elapsed_ms=total_elapsed_ms,
        )

        meta = self._build_metadata(
            symbol, tf, "none", False,
            datetime.min, datetime.min,
            0.0, 0, "degraded", attempted,
            notes="All providers failed",
        )

        return MarketData(df=empty_ohlcv_dataframe(), meta=meta)
