# Main bot script goes here.
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from BasicCommands import *
import SoundFinder
import logging


# Enable logging (for now it can be DEBUG or INFO)
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

logger = logging.getLogger(__name__)


def main():
    # Create the EventHandler and pass it your bot's token.
    updater = Updater("383778403:AAE_zdIpponH9K8CcgBCC1Txq8DwmdSoNQc")

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # on different commands - answer in Telegram
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))
    dp.add_handler(CommandHandler("sound" or "", SoundFinder.reply_sound, pass_args=True))

    # on noncommand i.e message - echo the message on Telegram
    dp.add_handler(MessageHandler(Filters.text, echo))

    # log all errors
    dp.add_error_handler(error)

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    main()