from aiogram import Router, types
from aiogram.filters import CommandStart
from aiogram.utils.markdown import hbold

async def command_start_handler(message: types.Message) -> None:
    """
    This handler receives messages with `/start` command
    """
    await message.answer(f"Hello, {hbold(message.from_user.full_name)}!")

def register_handlers_start(dp: Router):
    dp.message.register(command_start_handler, CommandStart())