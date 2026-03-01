class ProviderError(RuntimeError):
    """External/provider-level failure (auth, rate limit, outage, etc.)."""
    pass


class ConfigurationError(RuntimeError):
    """Misconfiguration (missing calendar mapping, unsupported symbol class, etc.)."""
    pass


class InternalMarketFeedError(RuntimeError):
    """Internal bug or invariant violation inside MarketFeed."""
    pass
