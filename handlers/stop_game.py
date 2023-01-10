from bot_config import dp
from aiogram.types import Message
import data
import keyboards

@dp.message_handler(commands=['stop_game'])
async def stop_current_game(message: Message):
    if data.game():
        data.start_new_game()
        await message.answer(f'{message.from_user.first_name}, игра остановлена. '
                             f'Для запуска новой игры введи команду /new_game', reply_markup=keyboards.kb_end)
    else:
        await message.answer(f'{message.from_user.first_name}, ты еще не начинал(а) играть.', reply_markup=keyboards.kb_start)
