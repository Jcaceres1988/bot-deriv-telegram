import MetaTrader5 as mt5
import pandas as pd
import talib

# Inicializar MetaTrader 5
if not mt5.initialize():
    print("❌ Error al conectar con MetaTrader 5")
    mt5.shutdown()
    exit()

# Función para obtener datos históricos
def obtener_datos(simbolo):
    rates = mt5.copy_rates_from_pos(simbolo, mt5.TIMEFRAME_M1, 0, 1000)
    if rates is None:
        print(f"⚠️ No se pudieron obtener datos para {simbolo}")
        return None
    df = pd.DataFrame(rates)
    df['time'] = pd.to_datetime(df['time'], unit='s')
    return df

# Obtener datos para Boom 1000 y Crash 1000
boom_symbol = "Boom 1000 Index"
crash_symbol = "Crash 1000 Index"
df_boom = obtener_datos(boom_symbol)
df_crash = obtener_datos(crash_symbol)

if df_boom is not None and df_crash is not None:
    # Calcular indicadores técnicos
    def calcular_indicadores(df):
        df['RSI'] = talib.RSI(df['close'], timeperiod=14)
        df['Momentum'] = talib.MOM(df['close'], timeperiod=614)
        df['EMA_21'] = talib.EMA(df['close'], timeperiod=21)
        df['EMA_50'] = talib.EMA(df['close'], timeperiod=50)
        return df
    
    df_boom = calcular_indicadores(df_boom)
    df_crash = calcular_indicadores(df_crash)
    
    # Guardar en archivos CSV
    df_boom.to_csv("indicadores_boom1000.csv", index=False)
    df_crash.to_csv("indicadores_crash1000.csv", index=False)
    
    print("✅ Archivos indicadores guardados correctamente.")
else:
    print("⚠️ No se pudo calcular los indicadores debido a la falta de datos.")

# Cerrar la conexión con MT5
mt5.shutdown()
