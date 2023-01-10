from bot_config import dp
from aiogram.types import Message
import data


@dp.message_handler(commands=['level'])
async def bot_level(message: Message):
    data.change_bot_level()
    if data.get_bot_level() == 1:
        await message.reply(f'{message.from_user.first_name}, игра будет немного проще :)')
    else:
        await message.reply(f'{message.from_user.first_name}, ты поставил(а) уровень "сложный". \n'
                            f'Будь внимателен(льна) и думай лучше на каждом ходе!')
    if not data.game():
        await message.answer(f'А теперь начинай игру: жми /new_game!')



