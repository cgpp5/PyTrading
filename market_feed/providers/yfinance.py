from __future__ import annotations

from datetime import datetime
import pandas as pd
import yfinance as yf

from .base import MarketDataProvider
from ..errors import ProviderError


_TIMEFRAME_MAP = {
    "15m": "15m",
    "1h": "60m",
    "1d": "1d",
}


class YFinanceProvider(MarketDataProvider):

    @property
    def name(self) -> str:
        return "yfinance"

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

        # yfinance >=0.2.31 puede devolver columnas MultiIndex
        # (e.g. ("Open", "AAPL")) al descargar un solo ticker.
        # Aplanar a nivel único antes de renombrar.
        if isinstance(df.columns, pd.MultiIndex):
            df.columns = df.columns.get_level_values(0)

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

        # yfinance usa "Date" para daily y "Datetime" para intradía
        df = df.reset_index()
        if "Datetime" in df.columns:
            df = df.rename(columns={"Datetime": "timestamp"})
        elif "Date" in df.columns:
            df = df.rename(columns={"Date": "timestamp"})

        return df
