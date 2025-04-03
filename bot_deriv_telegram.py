import pandas as pd
import numpy as np
import telebot
import schedule
import time
import requests
import json

# Configuración del bot de Telegram
TELEGRAM_BOT_TOKEN = "7976856792:AAEKwYzhKMGzB_ThnEMcER4eAYtWbPYL7u0"
CHAT_ID = "-1002646957870"
bot = telebot.TeleBot(TELEGRAM_BOT_TOKEN)

# URL de la API de Deriv
DERIV_API_URL = "https://api.deriv.com/v2/ticks/history"
ASSETS = {"boom_1000": "BOOM_1000", "crash_1000": "CRASH_1000"}

def obtener_datos(simbolo, num_velas=700):
    """Obtiene datos históricos desde la API de Deriv."""
    if simbolo not in ASSETS:
        print(f"⚠️ Activo {simbolo} no encontrado en la API de Deriv.")
        return pd.DataFrame()
    
    params = {
        "symbol": ASSETS[simbolo],
        "count": num_velas,
        "granularity": 60,  # Temporalidad M1
        "end": "latest"
    }
    response = requests.get(DERIV_API_URL, params=params)
    
    if response.status_code != 200:
        print(f"⚠️ Error al obtener datos de {simbolo}: {response.status_code}")
        return pd.DataFrame()
    
    data = response.json()
    if "candles" not in data:
        print(f"⚠️ No se encontraron datos para {simbolo}")
        return pd.DataFrame()
    
    df = pd.DataFrame(data["candles"])
    df.rename(columns={"epoch": "time", "close": "close"}, inplace=True)
    df['time'] = pd.to_datetime(df['time'], unit='s')
    return df

def calcular_indicadores(df):
    """Calcula RSI, Momentum y EMAs."""
    df['ema_21'] = df['close'].ewm(span=21, adjust=False).mean()
    df['ema_50'] = df['close'].ewm(span=50, adjust=False).mean()
    df['momentum'] = df['close'] - df['close'].shift(614)
    
    delta = df['close'].diff(1)
    gain = (delta.where(delta > 0, 0)).rolling(window=14).mean()
    loss = (-delta.where(delta < 0, 0)).rolling(window=14).mean()
    rs = gain / loss
    df['rsi'] = 100 - (100 / (1 + rs))
    
    return df

def analizar_mercado():
    """Analiza el mercado y envía señales a Telegram."""
    print("🔍 Analizando mercado...")
    for simbolo, direccion in [("boom_1000", "compra"), ("crash_1000", "venta")]:
        print(f"🔍 Ejecutando análisis para {simbolo}")
        
        df = obtener_datos(simbolo)
        if df.empty:
            print(f"⚠️ No se pudo obtener datos para {simbolo}")
            continue
        
        df = calcular_indicadores(df)
        
        print(f"Últimos datos de {simbolo}:")
        print(f"EMA 21: {df['ema_21'].iloc[-1]}, EMA 50: {df['ema_50'].iloc[-1]}")
        print(f"RSI: {df['rsi'].iloc[-1]:.2f}, Momentum: {df['momentum'].iloc[-1]:.2f}")
        
        if df['ema_21'].iloc[-1] > df['ema_50'].iloc[-1] and df['rsi'].iloc[-1] < 30 and df['momentum'].iloc[-1] > 0:
            mensaje = f"📈 Señal de {direccion.upper()} en {simbolo}\n\nPrecio: {df['close'].iloc[-1]}\nRSI: {df['rsi'].iloc[-1]:.2f}\nMomentum: {df['momentum'].iloc[-1]:.2f}"
            print(f"✅ Enviando señal: {mensaje}")
            bot.send_message(CHAT_ID, mensaje)

# Programar ejecución cada 10 minutos
schedule.every(10).minutes.do(analizar_mercado)
print("Bot en ejecución...")

while True:
    schedule.run_pending()
    print("Esperando 10 minutos antes del siguiente análisis...")
    time.sleep(600)
