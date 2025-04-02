import requests

TOKEN = "7976856792:AAEKwYzhKMGzB_ThnEMcER4eAYtWbPYL7u0"
CHAT_ID = "-1002646957870"

mensaje = "🚀 Prueba de mensaje desde el bot de Telegram!"

url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
params = {"chat_id": CHAT_ID, "text": mensaje}

response = requests.get(url, params=params)

if response.status_code == 200:
    print("✅ Mensaje enviado con éxito!")
else:
    print(f"❌ Error al enviar mensaje: {response.text}")
