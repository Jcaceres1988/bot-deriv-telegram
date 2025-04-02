import MetaTrader5 as mt5
import pandas as pd
import time

# Conectar con MT5
if not mt5.initialize():
    print("Error al conectar con MetaTrader 5")
    quit()

# Definir los símbolos correctamente
symbols = ["Boom 1000 Index", "Crash 1000 Index"]

def obtener_datos(symbol, timeframe=mt5.TIMEFRAME_M1, n_candles=1000):
    """ Obtiene datos históricos de MT5 """
    rates = mt5.copy_rates_from_pos(symbol, timeframe, 0, n_candles)
    if rates is None:
        print(f"No se pudo obtener datos para {symbol}")
        return None
    df = pd.DataFrame(rates)
    df['time'] = pd.to_datetime(df['time'], unit='s')
    return df

while True:
    for symbol in symbols:
        df = obtener_datos(symbol)
        if df is not None:
            filename = f"datos_{symbol.lower().replace(' ', '_')}.csv"
            df.to_csv(filename, index=False)
            print(f"Datos guardados en {filename}")
    
    print("Esperando 10 minutos para la siguiente actualización...")
    time.sleep(600)  # Esperar 10 minutos
