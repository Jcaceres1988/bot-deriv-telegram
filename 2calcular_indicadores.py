import pandas as pd
import ta

# Función para calcular indicadores técnicos
def calcular_indicadores(df):
    df["RSI"] = ta.momentum.RSIIndicator(df["close"], window=14).rsi()
    df["Momentum"] = ta.momentum.MomentumIndicator(df["close"], window=614).momentum()
    df["EMA_21"] = ta.trend.EMAIndicator(df["close"], window=21).ema_indicator()
    df["EMA_50"] = ta.trend.EMAIndicator(df["close"], window=50).ema_indicator()
    df["EMA_200"] = ta.trend.EMAIndicator(df["close"], window=200).ema_indicator()
    return df

if __name__ == "__main__":
    try:
        # Cargar datos
        df_boom = pd.read_csv("datos_boom_1000_index.csv")
        df_crash = pd.read_csv("datos_crash_1000_index.csv")

        # Calcular indicadores
        df_boom = calcular_indicadores(df_boom)
        df_crash = calcular_indicadores(df_crash)

        # Guardar los nuevos archivos con indicadores
        df_boom.to_csv("datos_boom_1000_index.csv", index=False)
        df_crash.to_csv("datos_crash_1000_index.csv", index=False)

        print("Indicadores calculados y guardados correctamente.")

    except Exception as e:
        print(f"Error al calcular indicadores: {e}")
