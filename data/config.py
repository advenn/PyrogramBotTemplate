import os

from dotenv import load_dotenv
from tortoise import Tortoise

load_dotenv()

# simple tortoise sqlite3 connection with db url
TORTOISE_ORM = {
    "connections": {"default": "sqlite://db.sqlite3"},
    "apps": {
        "models": {
            "models": ["utils.db_api.models", "aerich.models"],
            "default_connection": "default",
        },
    },
}

BOT_TOKEN = str(os.getenv("bot_token"))
API_ID = str(os.getenv('api_id'))
API_HASH = str(os.getenv('api_hash'))

admins = [
    int(os.getenv("ADMIN")),
]


async def init_db(generate=False):
    await Tortoise.init(config=TORTOISE_ORM)
    if generate:
        await Tortoise.generate_schemas()


async def close_db():
    await Tortoise.close_connections()


__all__ = ["BOT_TOKEN", "API_ID", "API_HASH", "admins", "init_db", "close_db"]
