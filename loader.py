from pyrogram import Client
from data.config import *

app = Client(
    "MY_CLIENT",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)
