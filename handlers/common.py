from bot_config import dp
from aiogram.types import Message
import data
import check_winner
import pc_step


@dp.message_handler()
async def take_candies(message: Message):
    if data.game():
        if message.text.isdigit():
            taken_candies = int(message.text)
            if (1 <= taken_candies <= 28) and (taken_candies <= data.get_total()):
                data.take_candies(taken_candies)
                if await check_winner.who_is_win(message, taken_candies, 'human'):
                    return
                await message.reply(f'{message.from_user.first_name} взял(а) {taken_candies} конфет(у/ы)\n'
                                    f'На столе осталось {data.get_total()} конфет(у/ы).\n'
                                    f'Теперь ходит РС.')
                await pc_step.pc_turn(message)
            else:
                await message.reply(f'{message.from_user.first_name}, ты указал(а) неправильное число конфет.\n'
                                    f'Бери от 1 до 28 конфет за ход.')
        else:
            await message.reply(f'{message.from_user.first_name}, ты указал(а) что-то странное.\n'
                                f'Бери от 1 до 28 конфет за ход.')