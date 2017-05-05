# -*- coding: utf-8 -*-
import config
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
#вынести в конфиг

logger = logging.getLogger(__name__)


def start(bot, update):
	bot.sendMessage(chat_id=update.message.chat_id, text="I'm a poor little bot, please say hello or send a stiker or just talk to me!")

def hello(bot, update):
	bot.sendMessage(chat_id=update.message.chat_id, text= "Hello, %s!" % update.message["from"].get("first_name"))

def sticker(bot, update):
	bot.sendSticker(chat_id=update.message.chat_id, sticker=update.message.file_id)

def echo(bot, update):
	update.message.reply_text(update.message.text)


def main():
	updater = Updater(token=config.token)
	dp = updater.dispatcher

	dp.add_handler(CommandHandler("start", start))
	dp.add_handler(CommandHandler("hello", hello))
	dp.add_handler(CommandHandler("sticker", sticker))
	dp.add_handler(MessageHandler(Filters.text, echo))

	updater.start_polling()
	updater.idle()

if __name__ == '__main__':
    main()

