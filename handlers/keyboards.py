from pyrogram import filters, Client
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup


@Client.on_message(filters.private & filters.command(['kb', 'keyboard']))
async def keyboard_example(app: Client, message):
    keyboard_markup = InlineKeyboardMarkup(inline_keyboard=[[]])
    # first row of keyboards
    keyboard1 = [
        InlineKeyboardButton(text='Button 1', callback_data='button_1'),
        InlineKeyboardButton(text='Button 2', callback_data='button_2'),
        InlineKeyboardButton(text='Button 3', callback_data='button_3'),
        InlineKeyboardButton(text='Button 4', callback_data='button_4'),
    ]
    # second row of keyboards
    keyboard2 = [
        InlineKeyboardButton(text='Button 5', callback_data='button_5'),
        InlineKeyboardButton(text='Button 6', callback_data='button_6'),
        InlineKeyboardButton(text='Button 7', callback_data='button_7'),
        InlineKeyboardButton(text='Button 8', callback_data='button_8'),
        InlineKeyboardButton(text='Button 9', callback_data='button_9'),
    ]
    keyboard_markup.inline_keyboard = [keyboard1, keyboard2]

    await message.reply(text='This is a keyboard example', reply_markup=keyboard_markup)


@Client.on_callback_query(filters.regex('^button_'))
async def callback_query_example(app: Client, callback_query):
    await callback_query.answer(text=f'You pressed {callback_query.data}')
    await callback_query.message.edit_text(f'You pressed {callback_query.data}')
