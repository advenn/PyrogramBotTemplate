from pyrogram import filters, Client


@Client.on_message(filters.group & filters.command(['start', 'help']))
async def group_start(app: Client, message):
    await message.reply(chat_id=message.from_user.id,
                        text='EN 🏴󠁧󠁢󠁥󠁮󠁧󠁿 : Welcome to the group\nUZ 🇺🇿: Guruhga xush kelibsiz')
