import os
import telebot

bot = telebot.TeleBot(os.environ["BOT_TOKEN"])

def handler(request):
    if request.method == "POST":
        bot.process_new_updates(
            [telebot.types.Update.de_json(request.body.decode("utf-8"))]
        )
        return "OK"

    return "Bot ZonaGris funcionando 👋"
