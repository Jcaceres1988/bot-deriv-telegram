import websocket
import json

# URL del WebSocket de Deriv
DERIV_WS_URL = "wss://ws.deriv.com/websockets/v3?app_id=1089"

def on_message(ws, message):
    data = json.loads(message)
    print("📩 Mensaje recibido:", data)

def on_error(ws, error):
    print("❌ Error al conectar con Deriv:", error)

def on_close(ws, close_status_code, close_msg):
    print("🔴 Conexión cerrada")

def on_open(ws):
    print("✅ Conectado a Deriv WebSocket")
    # Prueba de solicitud de datos
    request = {"ping": 1}
    ws.send(json.dumps(request))

if __name__ == "__main__":
    print("🔄 Ejecutando prueba de conexión con Deriv...")

    ws = websocket.WebSocketApp(
        DERIV_WS_URL,
        on_message=on_message,
        on_error=on_error,
        on_close=on_close
    )
    ws.on_open = on_open
    ws.run_forever()
