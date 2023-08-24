import logging
import sys

import telegram.error
from telegram import Bot
from telegram.ext import (CommandHandler, ConversationHandler, Dispatcher,
                          filters, MessageHandler, Updater,
                          CallbackQueryHandler, ShippingQueryHandler)


from flowershop.settings import DEBUG, TELEGRAM_TOKEN
from flowershop_bot.handlers.clients import handlers as clients_handlers
#common import handlers as common_handlers

from flowershop_bot.handlers.delivery_man import handlers as delivery_man_handlers
#meetup import handlers as meetup_handlers

from flowershop_bot.handlers.florist import handlers as florist_handlers
#admin import handlers as admin_handlers


def setup_dispatcher(dp):
    dp.add_error_handler(delivery_man_handlers)

    dp.add_handler(CommandHandler("start", clients_handlers.command_start))
    # dp.add_handler(CommandHandler("cancel", clients_handlers.command_cancel))
    # dp.add_handler(CommandHandler("admin", admin_handlers.command_admin))
    return dp


def run_pooling():
    """ Run bot in pooling mode """
    updater = Updater(TELEGRAM_TOKEN, use_context=True)

    dp = updater.dispatcher
    dp = setup_dispatcher(dp)

    bot_info = Bot(TELEGRAM_TOKEN).get_me()
    bot_link = f'https://t.me/{bot_info["username"]}'

    print(f"Pooling of '{bot_link}' started")

    updater.start_polling()
    updater.idle()


bot = Bot(TELEGRAM_TOKEN)
try:
    TELEGRAM_BOT_USERNAME = bot.get_me()["username"]
except telegram.error.Unauthorized:
    logging.error(f"Invalid TELEGRAM_TOKEN.")  # remove f string
    sys.exit(1)

n_workers = 1 if DEBUG else 4
dispatcher = setup_dispatcher(
    Dispatcher(bot, update_queue=None, workers=n_workers, use_context=True)
)
