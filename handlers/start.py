from bot_config import dp
from aiogram.types import Message
import rules
import keyboards


@dp.message_handler(commands=['start'])
async def on_start(message: Message):
    await message.answer(text=f'{message.from_user.first_name}, '
                              f'{rules.hello_message}', reply_markup=keyboards.kb_start)
