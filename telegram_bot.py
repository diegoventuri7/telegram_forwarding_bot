import logging
import configparser
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext, MessageHandler, Filters

config = configparser.ConfigParser()
config.read('config.ini')

API_TOKEN = config.get('DEFAULT', 'API_TOKEN')
SOURCE_CHANNEL_ID = config.get('DEFAULT', 'SOURCE_CHANNEL_ID')
DESTINATION_CHANNEL_ID = config.get('DEFAULT', 'DESTINATION_CHANNEL_ID')
SUBSTITUTIONS_FILE = config.get('DEFAULT', 'SUBSTITUTIONS_FILE')

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)

logger = logging.getLogger(__name__)

def load_substitutions(filename):
    substitutions = []
    with open(filename, 'r') as file:
        for line in file.readlines():
            if '>' in line:
                source, target = line.strip().split('>', 1)
                substitutions.append((source, target))
    return substitutions

def apply_substitutions(text, substitutions):
    for source, target in substitutions:
        text = text.replace(source, target)
    return text

substitutions = load_substitutions(SUBSTITUTIONS_FILE)

def forward_message(update: Update, context: CallbackContext):
    if update.channel_post:
        message = update.channel_post
    else:
        message = update.message

    if message.chat_id == int(SOURCE_CHANNEL_ID):
        text = apply_substitutions(message.text, substitutions)
        context.bot.send_message(chat_id=DESTINATION_CHANNEL_ID, text=text)

def main():
    updater = Updater(API_TOKEN)

    dispatcher = updater.dispatcher
    dispatcher.add_handler(MessageHandler(Filters.text & (~Filters.command), forward_message))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()

