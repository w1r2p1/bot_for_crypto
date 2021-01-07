from flask import Flask, render_template, request
# 抓 config 當中的物件
from app.config import config
import logging
from telegram import bot, Update
from telegram.ext import Dispatcher, CommandHandler

# 關於 Flask 設定
app = Flask(__name__)

# Setting Config
if app.config["ENV"] == "production":
    app.config.from_object(config['pro'])
else:
    app.config.from_object(config['dev'])

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
logger = logging.getLogger(__name__)

# Init Bot
bot = bot.Bot(token=app.config['BOT_API_KEY'])


@app.route('/hook', methods=['POST'])
def webhook_handler():
    """Set route /hook with POST method will trigger this method."""
    if request.method == "POST":
        update = Update.de_json(request.get_json(force=True), bot)
        dispatcher.process_update(update)
    return 'ok'


# New a dispatcher for bot
dispatcher = Dispatcher(bot, None)


def start(update, context):
    # TODO 這邊很重要 Medium 那篇可能有誤，可能更新了。
    text = "Hi, Welcome"
    update.message.reply_text(text)


dispatcher.add_handler(CommandHandler('start', start))


@app.route("/", defaults={"path": ""})
@app.route("/<path:path>")
def catch_all(path):
    return render_template("index.html"), 404
