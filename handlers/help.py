from bot_config import dp
from aiogram.types import Message
import rules


@dp.message_handler(commands=['help'])
async def get_help(message: Message):
    await message.answer(rules.help_message)
