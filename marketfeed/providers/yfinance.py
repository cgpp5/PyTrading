from __future__ import annotations

from datetime import datetime
import pandas as pd
import yfinance as yf

from .base import MarketDataProvider
from marketfeed.errors import ProviderError


_TIMEFRAME_MAP = {
    "15m": "15m",
    "1h": "60m",
    "4h": "60m",  # yfinance no soporta 4h nativo; se degrada
    "1d": "1d",
}


class YFinanceProvider(MarketDataProvider):
    name = "yfinance"

    def fetch_ohlcv(
        self,
        symbol: str,
        timeframe: str,
        start: datetime,
        end: datetime,
    ) -> pd.DataFrame:
        interval = _TIMEFRAME_MAP.get(timeframe)
        if interval is None:
            raise ProviderError(f"Unsupported timeframe for yfinance: {timeframe}")

        try:
            df = yf.download(
                tickers=symbol,
                start=start,
                end=end,
                interval=interval,
                progress=False,
                auto_adjust=False,
            )
        except Exception as e:
            raise ProviderError(str(e)) from e

        if df is None or df.empty:
            raise ProviderError("No data returned from yfinance")

        # yfinance devuelve columnas con mayúsculas
        df = df.rename(
            columns={
                "Open": "open",
                "High": "high",
                "Low": "low",
                "Close": "close",
                "Volume": "volume",
            }
        )

        df = df.reset_index().rename(columns={"Date": "timestamp"})

        return df
