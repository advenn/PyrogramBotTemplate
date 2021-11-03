import os

from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = str(os.getenv("bot_token"))
API_ID = str(os.getenv('api_id'))
API_HASH = str(os.getenv('api_hash'))

admins = [
    os.getenv("ADMIN_ID"),
]

