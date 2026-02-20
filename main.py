# главный файллик, запускает бота
import logging
import asyncio
import sys
from dotenv import load_dotenv
from os import getenv

import aiogram
from aiogram import types
from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart


load_dotenv()
TOKEN = getenv("BOT_TOKEN")
dp = Dispatcher()


@dp.message(CommandStart())
async def cmd_start(message: types.Message) -> None:
    await message.answer(f" Hello, {message.from_user.first_name}!")


@dp.message()
async def popugay(message: types.Message) -> None:
    await message.copy_to(message.chat.id)


async def main() -> None:
    bot = Bot(token=TOKEN)
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main=main())