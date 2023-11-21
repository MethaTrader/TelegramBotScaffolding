from aiogram import types

async def echo_handler(message: types.Message) -> None:
    """
    Handler will forward receive a message back to the sender
    """
    try:
        # Send a copy of the received message
        await message.send_copy(chat_id=message.chat.id)
    except TypeError:
        # But not all the types is supported to be copied so need to handle it
        await message.answer("Nice try!")

def register_handlers_echo(dp):
    dp.message.register(echo_handler)
