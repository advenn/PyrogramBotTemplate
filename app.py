import asyncio
import logging

from pyrogram import Client
from pyrogram.types import BotCommand

from data.config import *

app = Client(
    "MY_CLIENT",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN if BOT_TOKEN is not None else None,
    plugins=dict(root="handlers")
)

logging.basicConfig(level=logging.INFO)


async def main():
    """
    `main` is an async function that runs before the bot
    """
    # if you are running this bot first time set generate=True, it creates database, later set it to False
    await init_db(generate=True)
    async with app:
        if app.bot_token is not None:
            # register commands
            await app.set_bot_commands(commands=[BotCommand(command="start", description="Start the bot"),
                                                 BotCommand(command="help", description="Get help from the bot"),
                                                 BotCommand(command="kb", description="get sample inline keyboard"), ])
        await app.send_message(admins[0], "Bot started")


if __name__ == "__main__":
    try:
        asyncio.get_event_loop().run_until_complete(main())
        logging.info("Bot started")
        app.run()
    except KeyboardInterrupt:
        logging.info("Bot stopped")
        asyncio.get_event_loop().run_until_complete(close_db())
