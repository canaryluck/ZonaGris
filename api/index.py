import os
import telebot
from http.server import BaseHTTPRequestHandler

bot = telebot.TeleBot(os.environ["BOT_TOKEN"])

class handler(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-Type", "text/plain")
        self.end_headers()
        self.wfile.write(b"Bot ZonaGris funcionando")

    def do_POST(self):
        content_length = int(self.headers.get("Content-Length", 0))
        body = self.rfile.read(content_length)

        update = telebot.types.Update.de_json(body.decode("utf-8"))
        bot.process_new_updates([update])

        self.send_response(200)
        self.send_header("Content-Type", "text/plain")
        self.end_headers()
        self.wfile.write(b"OK")
