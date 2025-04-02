import MetaTrader5 as mt5

if not mt5.initialize():
    print("❌ Error al conectar con MetaTrader 5")
    mt5.shutdown()
else:
    cuenta = mt5.account_info()
    if cuenta:
        print(f"✅ Conectado a la cuenta: {cuenta.login}")
    else:
        print("⚠️ No se pudo obtener información de la cuenta.")
