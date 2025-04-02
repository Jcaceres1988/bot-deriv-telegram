import pandas as pd

# Función para generar señales de entrada
def generar_senales(df, simbolo):
    df['Señal'] = ""
    
    for i in range(1, len(df)):
        rsi = df['RSI'].iloc[i]
        momentum = df['Momentum'].iloc[i]
        ema_21 = df['EMA_21'].iloc[i]
        ema_50 = df['EMA_50'].iloc[i]
        ema_21_prev = df['EMA_21'].iloc[i-1]
        ema_50_prev = df['EMA_50'].iloc[i-1]
        
        # Condición de compra para Boom 1000 Index
        if simbolo == "Boom 1000 Index" and rsi < 30 and momentum > df['Momentum'].iloc[i-1] and ema_21_prev < ema_50_prev and ema_21 > ema_50:
            df.at[i, 'Señal'] = "🟢 COMPRA"
        
        # Condición de venta para Crash 1000 Index
        elif simbolo == "Crash 1000 Index" and rsi > 70 and momentum < df['Momentum'].iloc[i-1] and ema_21_prev > ema_50_prev and ema_21 < ema_50:
            df.at[i, 'Señal'] = "🔴 VENTA"
    
    return df

# Cargar los datos calculados previamente
df_boom = pd.read_csv("indicadores_boom1000.csv")
df_crash = pd.read_csv("indicadores_crash1000.csv")

# Generar señales
df_boom = generar_senales(df_boom, "Boom 1000 Index")
df_crash = generar_senales(df_crash, "Crash 1000 Index")

# Mostrar las últimas señales
print("\n✅ Señales para Boom 1000 Index:")
print(df_boom[['time', 'Señal']].tail())

print("\n✅ Señales para Crash 1000 Index:")
print(df_crash[['time', 'Señal']].tail())

# Guardar resultados
df_boom.to_csv("senales_boom1000.csv", index=False)
df_crash.to_csv("senales_crash1000.csv", index=False)
