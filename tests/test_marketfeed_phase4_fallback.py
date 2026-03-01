import unittest
from unittest.mock import patch
from datetime import datetime, timedelta, timezone

from marketfeed.marketfeed import MarketFeed
from marketfeed.errors import ProviderError

class TestMarketFeedFallback(unittest.TestCase):
    
    def setUp(self):
        from marketfeed.providers.alpaca import AlpacaProvider
        from marketfeed.providers.tiingo import TiingoProvider
        from marketfeed.providers.yfinance import YFinanceProvider
        
        # Instanciamos el orquestador inyectando la lista de proveedores directamente
        self.feed = MarketFeed(
            providers=[
                AlpacaProvider(api_key="fake", api_secret="fake"),
                TiingoProvider(api_key="fake"),
                YFinanceProvider()
            ]
        )
        self.start = datetime.now(timezone.utc) - timedelta(days=5)
        self.end = datetime.now(timezone.utc)
        self.symbol = "SPY"
        self.tf = "1d"

    @patch('marketfeed.providers.alpaca.AlpacaProvider.fetch_ohlcv')
    @patch('marketfeed.providers.tiingo.TiingoProvider.fetch_ohlcv')
    def test_fallback_alpaca_fails_uses_tiingo(self, mock_tiingo, mock_alpaca):
        """Prueba: Caída de Alpaca → Uso de Tiingo"""
        
        # 1. Forzamos a Alpaca a fallar con un Error de Conexión
        mock_alpaca.side_effect = ProviderError("Alpaca connection lost")
        
        # 2. Hacemos que Tiingo devuelva un DataFrame válido
        import pandas as pd
        df_tiingo = pd.DataFrame({
            "open": [10], "high": [12], "low": [9], "close": [11], "volume": [100]
        }, index=pd.to_datetime(["2026-01-01"], utc=True))
        df_tiingo.index.name = "timestamp"
        mock_tiingo.return_value = df_tiingo

        # Ejecutamos
        market_data = self.feed.get_ohlcv(self.symbol, self.tf, self.start, self.end)

        # Verificaciones
        mock_alpaca.assert_called_once()  # Se intentó Alpaca
        mock_tiingo.assert_called_once()  # Se intentó Tiingo
        
        self.assertEqual(market_data.meta.provider_used, "tiingo")
        self.assertTrue(market_data.meta.fallback_used)
        self.assertEqual(market_data.meta.quality, "degraded")
        self.assertEqual(market_data.df.iloc[0]["source"], "tiingo")

    @patch('marketfeed.providers.alpaca.AlpacaProvider.fetch_ohlcv')
    @patch('marketfeed.providers.tiingo.TiingoProvider.fetch_ohlcv')
    @patch('marketfeed.providers.yfinance.YFinanceProvider.fetch_ohlcv')
    def test_fallback_both_fail_uses_yfinance(self, mock_yf, mock_tiingo, mock_alpaca):
        """Prueba: Caída de Alpaca y Tiingo → Uso de yfinance"""
        
        # 1. Forzamos a Alpaca y Tiingo a fallar (ej. Rate Limit y Caída Servidor)
        mock_alpaca.side_effect = ProviderError("Alpaca rate limit")
        mock_tiingo.side_effect = ProviderError("Tiingo server down")
        
        # 2. Hacemos que yfinance salve la situación
        import pandas as pd
        df_yf = pd.DataFrame({
            "open": [10], "high": [12], "low": [9], "close": [11], "volume": [100]
        }, index=pd.to_datetime(["2026-01-01"], utc=True))
        df_yf.index.name = "timestamp"
        mock_yf.return_value = df_yf

        # Ejecutamos
        market_data = self.feed.get_ohlcv(self.symbol, self.tf, self.start, self.end)

        # Verificaciones
        mock_alpaca.assert_called_once()
        mock_tiingo.assert_called_once()
        mock_yf.assert_called_once()
        
        self.assertEqual(market_data.meta.provider_used, "yfinance")
        self.assertTrue(market_data.meta.fallback_used)
        self.assertEqual(market_data.meta.quality, "degraded")

if __name__ == '__main__':
    unittest.main()