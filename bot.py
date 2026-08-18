import os
import telebot

TOKEN = os.getenv("BOT_TOKEN")

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(func=lambda message: True)
def responder(message):
    bot.reply_to(message, "¡Hola! 👋 Tu bot ZonaGris ya está funcionando.")

print("Bot iniciado...")
bot.infinity_polling()
