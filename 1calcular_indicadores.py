import pandas as pd
import ta  # Se reemplaza talib por ta

def calcular_indicadores(df):
    # RSI
    df["RSI"] = ta.momentum.RSIIndicator(df["close"], window=14).rsi()
    
    # Momentum (Williams %R como alternativa)
    df["Momentum"] = ta.momentum.WilliamsRIndicator(df["high"], df["low"], df["close"], lbp=614).williams_r()
    
    # Medias móviles exponenciales (EMA)
    df["EMA_21"] = ta.trend.EMAIndicator(df["close"], window=21).ema_indicator()
    df["EMA_50"] = ta.trend.EMAIndicator(df["close"], window=50).ema_indicator()
    df["EMA_200"] = ta.trend.EMAIndicator(df["close"], window=200).ema_indicator()
    
    return df

# Cargar datos de Boom 1000
df_boom = pd.read_csv("datos_boom1000.csv")
df_boom = calcular_indicadores(df_boom)
df_boom.to_csv("indicadores_boom1000.csv", index=False)

# Cargar datos de Crash 1000
df_crash = pd.read_csv("datos_crash1000.csv")
df_crash = calcular_indicadores(df_crash)
df_crash.to_csv("indicadores_crash1000.csv", index=False)

print("Indicadores calculados y guardados correctamente.")
