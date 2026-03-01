class Observability:
    # ------------------------------------------------------------
    # Legacy logging / alerting (Fases 0–4)
    # ------------------------------------------------------------
    def log_warning(self, event: str, **context):
        pass

    def log_error(self, event: str, **context):
        pass

    def alert_critical(self, event: str, **context):
        pass

    # ------------------------------------------------------------
    # Provider lifecycle (Fase 7)
    # ------------------------------------------------------------
    def record_provider_attempt(self, provider, symbol, timeframe, tier):
        pass

    def record_provider_failure(self, provider, symbol, timeframe, error):
        pass

    def record_provider_success(self, provider, symbol, timeframe):
        pass

    # ------------------------------------------------------------
    # Fallback
    # ------------------------------------------------------------
    def record_fallback_used(self, symbol, timeframe, attempted_providers):
        pass

    # ------------------------------------------------------------
    # Latency
    # ------------------------------------------------------------
    def record_provider_latency(self, provider, symbol, timeframe, elapsed_ms):
        pass

    def record_total_latency(self, symbol, timeframe, elapsed_ms):
        pass

    # ------------------------------------------------------------
    # Data quality
    # ------------------------------------------------------------
    def record_data_quality(
        self,
        symbol,
        timeframe,
        quality,
        coverage_ratio,
        gap_count,
    ):
        pass


class InMemoryObservability(Observability):
    def __init__(self):
        # Legacy
        self.warnings: list[tuple[str, dict]] = []
        self.errors: list[tuple[str, dict]] = []
        self.criticals: list[tuple[str, dict]] = []

        # Fase 7
        self.events: list[dict] = []
        self.counters: dict[str, int] = {}
        self.latencies: dict[str, list[float]] = {}
        self.data_quality: list[dict] = []

    # ------------------------------------------------------------
    # Legacy logging / alerting
    # ------------------------------------------------------------
    def log_warning(self, event: str, **context):
        self.warnings.append((event, context))

    def log_error(self, event: str, **context):
        self.errors.append((event, context))

    def alert_critical(self, event: str, **context):
        self.criticals.append((event, context))

    # ------------------------------------------------------------
    # Provider lifecycle
    # ------------------------------------------------------------
    def record_provider_attempt(self, provider, symbol, timeframe, tier):
        self.events.append({
            "type": "provider_attempt",
            "provider": provider,
            "symbol": symbol,
            "timeframe": timeframe,
            "tier": tier,
        })

    def record_provider_failure(self, provider, symbol, timeframe, error):
        self.events.append({
            "type": "provider_failure",
            "provider": provider,
            "symbol": symbol,
            "timeframe": timeframe,
            "error": error,
        })
        self.counters["provider_failure"] = (
            self.counters.get("provider_failure", 0) + 1
        )

    def record_provider_success(self, provider, symbol, timeframe):
        self.events.append({
            "type": "provider_success",
            "provider": provider,
            "symbol": symbol,
            "timeframe": timeframe,
        })

    # ------------------------------------------------------------
    # Fallback
    # ------------------------------------------------------------
    def record_fallback_used(self, symbol, timeframe, attempted_providers):
        self.events.append({
            "type": "fallback_used",
            "symbol": symbol,
            "timeframe": timeframe,
            "attempted_providers": attempted_providers,
        })
        self.counters["fallback"] = self.counters.get("fallback", 0) + 1

    # ------------------------------------------------------------
    # Latency
    # ------------------------------------------------------------
    def record_provider_latency(self, provider, symbol, timeframe, elapsed_ms):
        key = f"provider:{provider}"
        self.latencies.setdefault(key, []).append(elapsed_ms)

    def record_total_latency(self, symbol, timeframe, elapsed_ms):
        self.latencies.setdefault("total", []).append(elapsed_ms)

    # ------------------------------------------------------------
    # Data quality
    # ------------------------------------------------------------
    def record_data_quality(
        self,
        symbol,
        timeframe,
        quality,
        coverage_ratio,
        gap_count,
    ):
        self.data_quality.append({
            "symbol": symbol,
            "timeframe": timeframe,
            "quality": quality,
            "coverage_ratio": coverage_ratio,
            "gap_count": gap_count,
        })
