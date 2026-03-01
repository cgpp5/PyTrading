from __future__ import annotations

import logging
from datetime import datetime
import requests
import pandas as pd

from .base import MarketDataProvider
from ..errors import ProviderError

logger = logging.getLogger(__name__)

class TiingoProvider(MarketDataProvider):
    """
    Proveedor Tier 2: Tiingo.
    Actúa como fallback de alta calidad. 
    Usa el endpoint IEX para intradía (15m, 1h) y el endpoint Daily (EOD) para 1d.
    No soporta 4h nativamente para evitar resampleos inconsistentes de IEX.
    """

    @property
    def name(self) -> str:
        return "tiingo"

    def __init__(self, api_key: str):
        self.api_key = api_key
        self.base_url_iex = "https://api.tiingo.com/iex"
        self.base_url_eod = "https://api.tiingo.com/tiingo/daily"
        
        # Eliminamos '4h' por seguridad matemática en sesiones de 6.5h
        self._tf_map_iex = {
            "15m": "15min",
            "1h": "1hour"
        }

    def fetch_ohlcv(self, symbol: str, timeframe: str, start: datetime, end: datetime) -> pd.DataFrame:
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Token {self.api_key}"
        }
        
        start_str = start.strftime('%Y-%m-%d')
        end_str = end.strftime('%Y-%m-%d')

        if timeframe == "1d":
            # Endpoint oficial de fin de día (EOD)
            url = f"{self.base_url_eod}/{symbol}/prices"
            params = {
                "startDate": start_str,
                "endDate": end_str
            }
        elif timeframe in self._tf_map_iex:
            # Endpoint IEX para intradía
            url = f"{self.base_url_iex}/{symbol}/prices"
            params = {
                "startDate": start_str,
                "endDate": end_str,
                "resampleFreq": self._tf_map_iex[timeframe]
            }
        else:
            raise ProviderError(f"[{self.name}] Timeframe no soportado de forma segura: {timeframe}")

        try:
            logger.debug(f"[{self.name}] Solicitando datos para {symbol} ({timeframe})")
            response = requests.get(url, headers=headers, params=params, timeout=10)
            
            # Control estricto de Rate Limits (sin retries)
            if response.status_code == 429:
                raise ProviderError(f"[{self.name}] Rate limit excedido (HTTP 429). Iniciando fallback.")
                
            response.raise_for_status()
            data = response.json()

        except requests.exceptions.RequestException as e:
            raise ProviderError(f"[{self.name}] Error HTTP o de red: {e}")

        # Validación de datos vacíos = forzar fallback
        if not data:
            raise ProviderError(f"[{self.name}] No se devolvieron datos para {symbol} en el rango solicitado.")

        df = pd.DataFrame(data)

        # Renombramos la fecha para cumplir el contrato básico
        df.rename(columns={"date": "timestamp"}, inplace=True)
        
        # Validación defensiva de columnas
        required_cols = ["timestamp", "open", "high", "low", "close", "volume"]
        missing = [c for c in required_cols if c not in df.columns]
        
        if missing:
            raise ProviderError(f"[{self.name}] La respuesta omite columnas vitales: {missing}")
            
        # Filtramos estrictamente las columnas y no forzamos tipos/índices (se hace en normalize)
        df = df[required_cols]
        df["timestamp"] = pd.to_datetime(df["timestamp"])

        return df