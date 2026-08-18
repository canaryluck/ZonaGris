import os
import telebot

bot = telebot.TeleBot(os.environ["BOT_TOKEN"])

def handler(request):
    if request.method == "POST":
        update = telebot.types.Update.de_json(request.body.decode("utf-8"))
        bot.process_new_updates([update])
        return "OK"

    return "Bot ZonaGris funcionando 👋"
