import telebot

# Reemplaza con tu token de bot de Telegram
TOKEN = "7976856792:AAEKwYzhKMGzB_ThnEMcER4eAYtWbPYL7u0"
bot = telebot.TeleBot(TOKEN)

# Comando /start
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "¡Hola! Soy tu bot de Telegram 🤖")

# Responder a cualquier mensaje
@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, f"Me dijiste: {message.text}")

# Mantener el bot en ejecución
print("Bot iniciado...")
bot.infinity_polling()
