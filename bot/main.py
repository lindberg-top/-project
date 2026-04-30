from aiogram import Bot, Dispatcher
from dotenv import load_dotenv
from os import getenv
from actions import handlers

import logging
import asyncio



logging.basicConfig(level=logging.INFO)

load_dotenv()

token = getenv('BOT_TOKEN')

dp = Dispatcher()
dp.include_router(handlers.router)
bot = Bot(token=token)

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())