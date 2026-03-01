from __future__ import annotations

import logging
from datetime import datetime
import requests
import pandas as pd

from .base import MarketDataProvider
from ..errors import ProviderError

logger = logging.getLogger(__name__)

class AlpacaProvider(MarketDataProvider):
    """
    Proveedor Tier 1: Alpaca (Paper Trading / Free Tier).
    Utiliza el feed 'iex' para proporcionar datos gratuitos con latencia muy baja.
    """
    name = "alpaca"

    def __init__(self, api_key: str, api_secret: str):
        # El endpoint para la API de datos de mercado (Data API v2)
        self.base_url = "https://data.alpaca.markets/v2"
        self.api_key = api_key
        self.api_secret = api_secret
        
        # Mapeo del estándar del sistema al formato que espera Alpaca
        self._tf_map = {
            "15m": "15Min",
            "1h": "1Hour",
            "4h": None,
            "1d": "1Day"
        }

    def fetch_ohlcv(self, symbol: str, timeframe: str, start: datetime, end: datetime) -> pd.DataFrame:
        """
        Obtiene datos históricos de barras para un símbolo.
        """
        # Validación temprana del timeframe
        alpaca_tf = self._tf_map.get(timeframe)
        if alpaca_tf is None:
            raise ProviderError(f"[{self.name}] Timeframe no soportado: {timeframe}")

        # Configuración de los headers para la autenticación
        headers = {
            "APCA-API-KEY-ID": self.api_key,
            "APCA-API-SECRET-KEY": self.api_secret,
            "accept": "application/json"
        }

        # Formatear fechas a RFC3339 como requiere Alpaca
        start_str = start.strftime('%Y-%m-%dT%H:%M:%SZ')
        end_str = end.strftime('%Y-%m-%dT%H:%M:%SZ')

        # Endpoint de barras históricas para acciones
        url = f"{self.base_url}/stocks/bars"
        
        params = {
            "symbols": symbol,
            "timeframe": alpaca_tf,
            "start": start_str,
            "end": end_str,
            "limit": 10000,
            "feed": "iex"  # Feed gratuito obligatorio para cuentas sin fondear
        }

        try:
            logger.debug(f"[{self.name}] Solicitando datos para {symbol} ({alpaca_tf})")
            response = requests.get(url, headers=headers, params=params, timeout=10)
            
            # Alpaca puede devolver 429 si superamos el rate limit (200 requests/minuto)
            if response.status_code == 429:
                raise ProviderError(f"[{self.name}] Rate limit excedido (HTTP 429).")
                
            response.raise_for_status()
            data = response.json()

        except requests.exceptions.RequestException as e:
            raise ProviderError(f"[{self.name}] Error de conexión o HTTP: {e}")

        # Si el símbolo no devolvió barras o está vacío
        if "bars" not in data or symbol not in data["bars"] or not data["bars"][symbol]:
            # Lanzamos excepción para forzar el fallback explícito y registrar el motivo exacto
            raise ProviderError(f"[{self.name}] No se devolvieron datos para {symbol} en el rango solicitado.")

        # Convertir a DataFrame
        raw_bars = data["bars"][symbol]
        df = pd.DataFrame(raw_bars)

        # Mapear los nombres de las columnas que devuelve Alpaca al formato del sistema
        # t=timestamp, o=open, h=high, l=low, c=close, v=volume, n=trade_count, vw=vwap
        rename_map = {
            "t": "timestamp",
            "o": "open",
            "h": "high",
            "l": "low",
            "c": "close",
            "v": "volume"
        }
        df.rename(columns=rename_map, inplace=True)

        # Quedarnos estrictamente con las columnas requeridas para no arrastrar basura (ej. 'vw', 'n')
        required_cols = ["timestamp", "open", "high", "low", "close", "volume"]
        df = df[required_cols]

        return df