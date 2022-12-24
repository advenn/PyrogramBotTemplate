from pyrogram import filters, Client


@Client.on_message(filters.channel)
async def channel_start(app: Client, message):
    # write your logic to handle message from channel
    ...
