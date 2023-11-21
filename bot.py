import asyncio
import logging
import sys

from aiogram import Bot, Dispatcher, Router, types
from aiogram.enums import ParseMode
from handlers.commands.start import register_handlers_start
from handlers.messages.echo import register_handlers_echo
from config import TELEGRAM_API_TOKEN


# All handlers should be attached to the Router (or Dispatcher)
dp = Dispatcher()

# Регистрация обработчиков
register_handlers_start(dp)
register_handlers_echo(dp)

async def main() -> None:
    # Initialize Bot instance with a default parse mode which will be passed to all API calls
    bot = Bot(TELEGRAM_API_TOKEN, parse_mode=ParseMode.HTML)
    # And the run events dispatching
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())