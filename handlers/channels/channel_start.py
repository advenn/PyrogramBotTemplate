from loader import app
from pyrogram import filters


@app.on_message(filters.channel & filters.command(['start', 'help']))
async def start(client, message):
    await app.send_message(chat_id=message.from_user.id,
                           text='EN 🏴󠁧󠁢󠁥󠁮󠁧󠁿 : This message will sen sent to channel\nUZ 🇺🇿:Ushbu xabar kanalga yuboriladi')
