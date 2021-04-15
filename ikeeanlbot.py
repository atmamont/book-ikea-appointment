from secret import TOKEN
from telegram.ext import Updater, CommandHandler
import logging

def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="I can help you to book your appointment on Ikea.nl")

updater = Updater(token=TOKEN, use_context=True)
start_handler = CommandHandler('start', start)

dispatcher = updater.dispatcher
dispatcher.add_handler(start_handler)

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',level=logging.INFO)


updater.start_polling()