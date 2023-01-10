from bot_config import dp
from aiogram.types import Message
import data
import random
import human_step
import pc_step


@dp.message_handler(commands=['new_game'])
async def start_new_game(message: Message):
    if not data.game():
        data.start_new_game()
        if data.game():
            who_is_first = random.randint(0, 1)
            if who_is_first == 1:
                await human_step.human_turn(message)
            else:
                await pc_step.pc_turn(message)
    else:
        await message.answer(f'{message.from_user.first_name}, ты уже в игре. '
                             f'Закончи партию или нажми /stop_game для окончания '
                             f'текущей игры.')