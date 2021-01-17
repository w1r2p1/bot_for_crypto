import app as app
from flask import Flask, render_template, request
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
# 抓 config 當中的物件
from app.config import config
import logging
import telebot

# init Package
logger = telebot.logger
telebot.logger.setLevel(logging.INFO)
app = Flask(__name__)

# Setting Config
if app.config["ENV"] == "production":
    app.config.from_object(config['pro'])
else:
    app.config.from_object(config['dev'])

# Models 關於資料庫
db = SQLAlchemy(app)
Migrate = Migrate(app, db)
ma = Marshmallow(app)

# init bot
bot = telebot.TeleBot(token=app.config['BOT_API_KEY'])

@app.route('/' + app.config['BOT_API_KEY'], methods=['POST'])
def getMessage():
    bot.process_new_updates([telebot.types.Update.de_json(request.stream.read().decode("utf-8"))])
    return "!", 200


# Connect Telegram bot Webhooks
@app.route("/")
def webhook():
    bot.remove_webhook()
    bot.set_webhook(url=app.config['BOT_WEBHOOKS_URL'] + app.config['BOT_API_KEY'])
    return "!", 200

from . import commands
