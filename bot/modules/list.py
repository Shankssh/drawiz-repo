from telegram.ext import CommandHandler

from bot import LOGGER, RECURSIVE_SEARCH, dispatcher
from bot.helper.mirror_utils.upload_utils.gdriveTools import GoogleDriveHelper
from bot.helper.telegram_helper.bot_commands import BotCommands
from bot.helper.telegram_helper.filters import CustomFilters
from bot.helper.telegram_helper.message_utils import editMessage, sendMessage


def list_drive(update, context):
    try:
        search = update.message.text.split(" ", maxsplit=1)[1]
        LOGGER.info(f"Searching: {search}")
        reply = sendMessage("Searching From Drawiz Dynasty.. Wait a Minute 🤩", context.bot, update)
        gdrive = GoogleDriveHelper(None)
        if RECURSIVE_SEARCH:  
            msg, button = gdrive.uni_drive_list(search)
        else:
            msg, button = gdrive.drive_list(search) 

        if button:
            editMessage(msg, reply, button)
        else:
            editMessage("Opps, not Available 😔", reply, button)

    except IndexError:
        sendMessage("Send a Search Key Along with Command", context.bot, update)


list_handler = CommandHandler(
    BotCommands.ListCommand,
    list_drive,
    filters=CustomFilters.authorized_chat | CustomFilters.authorized_user,
    run_async=True,
)
dispatcher.add_handler(list_handler) 
