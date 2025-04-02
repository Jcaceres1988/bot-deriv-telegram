import telebot

TELEGRAM_BOT_TOKEN = "7976856792:AAEKwYzhKMGzB_ThnEMcER4eAYtWbPYL7u0"  # Reemplázalo con tu token real
bot = telebot.TeleBot(TELEGRAM_BOT_TOKEN)

@bot.message_handler(func=lambda message: True)
def recibir_mensaje(message):
    print(f"📩 Mensaje recibido: {message.text} | De: {message.chat.id}")

bot.polling()
