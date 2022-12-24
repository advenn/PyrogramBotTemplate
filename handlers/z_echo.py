from pyrogram import filters, Client


@Client.on_message(filters.private)
async def z_echo(app: Client, message):
    """
    It takes a message, and replies to it with the same text

    :param app: Client - The client object that is running the bot
    :type app: Client
    :param message: The message object that triggered the command
    """
    await message.reply(text=message.text)
