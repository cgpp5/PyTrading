from __future__ import annotations

from abc import ABC, abstractmethod
from datetime import datetime

import pandas as pd


class MarketDataProvider(ABC):
    @property
    @abstractmethod
    def name(self) -> str:
        """Unique identifier for this provider (e.g. 'alpaca', 'yfinance')."""
        ...

    @abstractmethod
    def fetch_ohlcv(self, symbol: str, timeframe: str, start: datetime, end: datetime) -> pd.DataFrame:
        raise NotImplementedError
