from loader import app
from pyrogram import filters


@app.on_message(filters.private)
async def start(client, message):
    await app.send_message(chat_id=message.from_user.id,
                           text=message.text)
