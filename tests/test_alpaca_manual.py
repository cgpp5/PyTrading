import os
import logging
from datetime import datetime, timedelta, timezone
from dotenv import load_dotenv

# Importamos el proveedor y la clase de error de tu estructura
from marketfeed.providers.alpaca import AlpacaProvider
from marketfeed.errors import ProviderError

# Configuramos el logging en nivel DEBUG para ver exactamente la URL que se llama
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(name)s - %(message)s')

def run_test():
    print("--- Iniciando prueba manual de AlpacaProvider (Fase 3) ---")
    
    # 1. Cargar las credenciales del archivo .env
    load_dotenv()
    api_key = os.getenv("ALPACA_API_KEY")
    api_secret = os.getenv("ALPACA_API_SECRET")
    
    if not api_key or not api_secret:
        print("❌ ERROR: No se encontraron ALPACA_API_KEY o ALPACA_API_SECRET en el archivo .env")
        print("Asegúrate de haber creado el archivo .env en la raíz del proyecto.")
        return

    # 2. Instanciar el proveedor
    try:
        provider = AlpacaProvider(api_key=api_key, api_secret=api_secret)
        print("✅ Proveedor de Alpaca instanciado correctamente.")
    except Exception as e:
        print(f"❌ ERROR al instanciar el proveedor: {e}")
        return

    # 3. Configurar los parámetros de la petición
    symbol = "SPY"
    timeframe = "1h"
    
    # Pedimos datos de los últimos 5 días hasta el momento actual (en UTC)
    end_date = datetime.now(timezone.utc)
    start_date = end_date - timedelta(days=5)

    print(f"\nSolicitando datos para {symbol} en {timeframe}")
    print(f"Desde: {start_date.strftime('%Y-%m-%d %H:%M:%S UTC')}")
    print(f"Hasta: {end_date.strftime('%Y-%m-%d %H:%M:%S UTC')}\n")

    # 4. Ejecutar la llamada a la API
    try:
        df = provider.fetch_ohlcv(symbol, timeframe, start_date, end_date)
        
        if df.empty:
            print("⚠️ Petición exitosa, pero el DataFrame está vacío.")
            print("Esto es normal si el mercado estuvo cerrado todo el rango solicitado (ej. fin de semana).")
        else:
            print("✅ ¡Datos obtenidos y formateados con éxito!\n")
            print("Primeras 3 filas:")
            print(df.head(3))
            print("\nÚltimas 3 filas:")
            print(df.tail(3))
            print("-" * 60)
            print(f"Total de velas: {len(df)}")
            print(f"Índice: '{df.index.name}' (Tipo: {df.index.dtype})")
            print(f"Columnas: {list(df.columns)}")
            
    except ProviderError as pe:
        print(f"❌ Fallo controlado en el proveedor: {pe}")
    except Exception as e:
        print(f"❌ Fallo crítico inesperado: {e}")

if __name__ == "__main__":
    run_test()