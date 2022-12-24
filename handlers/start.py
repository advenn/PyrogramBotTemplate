from pyrogram import filters, Client

from filters.filters import is_admin_filter
from utils.db_api import models


@Client.on_message(filters.private & filters.command(['start', 'help']) & is_admin_filter)
async def admin_start(app: Client, message):
    """
    This is a function that is called when an admin sends a message to the bot.

    :param app: Client - the client object
    :type app: Client
    :param message: The message object that triggered the command
    """
    user = await models.User.get_or_none(user_id=message.from_user.id)
    if user is None:
        await models.User.create(user_id=message.from_user.id,
                                 username=message.from_user.username,
                                 first_name=message.from_user.first_name,
                                 last_name=message.from_user.last_name if message.from_user.last_name else '',
                                 language_code=message.from_user.language_code)
    await message.reply(text='EN 🏴󠁧󠁢󠁥󠁮󠁧󠁿 : Welcome to the group, Admin!\nUZ 🇺🇿: Guruhga xush kelibsiz, Admin!')


@Client.on_message(filters.private & filters.command(['start', 'help']))
async def start(app: Client, message):
    """
    It sends a message to the user who sent the /start command

    :param app: Client - the client object
    :type app: Client
    :param message: The message object that triggered the command
    """
    await app.send_message(chat_id=message.from_user.id,
                           text='EN 🏴󠁧󠁢󠁥󠁮󠁧󠁿 : Welcome to bot\nUZ 🇺🇿 :Botga xush kelibsiz')
