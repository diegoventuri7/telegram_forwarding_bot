import logging
import configparser

from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext, MessageHandler, Filters

config = configparser.ConfigParser()
config.read('config.ini')

API_TOKEN = config.get('DEFAULT', 'API_TOKEN')

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)

logger = logging.getLogger(__name__)

def get_chat_id(update: Update, context: CallbackContext):
    if update.channel_post:
        message = update.channel_post
    else:
        message = update.message

    chat_id = message.chat_id
    chat_title = message.chat.title
    context.bot.send_message(chat_id, f'The channel "{chat_title}" has the ID: {chat_id}')

def channel_post_handler(update: Update, context: CallbackContext):
    if update.channel_post.text.startswith("/get_chat_id"):
        get_chat_id(update, context)

def main():
    updater = Updater(API_TOKEN)

    dispatcher = updater.dispatcher
    dispatcher.add_handler(CommandHandler('get_chat_id', get_chat_id))
    dispatcher.add_handler(MessageHandler(Filters.update.channel_post, channel_post_handler))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
