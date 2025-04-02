import MetaTrader5 as mt5

# Inicializar conexión con MetaTrader 5
if not mt5.initialize():
    print("❌ Error al conectar con MetaTrader 5")
    mt5.shutdown()
    exit()

# Nombres de los activos según aparecen en MT5
simbolos = ["Boom 1000 Index", "Crash 1000 Index"]

for simbolo in simbolos:
    info = mt5.symbol_info(simbolo)
    if info is None:
        print(f"⚠️ {simbolo} no está disponible en MetaTrader 5.")
    else:
        print(f"✅ {simbolo} está disponible en MetaTrader 5.")

# Cerrar conexión con MT5
mt5.shutdown()
