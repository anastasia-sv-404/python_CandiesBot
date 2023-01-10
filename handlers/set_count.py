from bot_config import dp
from aiogram.types import Message
import data


@dp.message_handler(commands=['set_count'])
async def set_count(message: Message):
    if data.game():
        await message.answer(f'{message.from_user.first_name}, игра уже идет. '
                             f'Поменяй число конфет на столе для новой партии.')
    else:
        if len(message.text.split()) > 1:
            new_count = message.text.split()[1]
            if new_count.isdigit():
                new_count = int(new_count)
                if new_count == 150:
                    await message.reply(f'{message.from_user.first_name}, ты хочешь оставить 150 конфет? '
                                        f'Окей, принято!\n'
                                        f'Чтобы начать играть, нажми /new_game')
                elif new_count < 150:
                    await message.reply(f'{message.from_user.first_name}, игра будет слишком легкой. '
                                        f'Оставь 150 конфет или введи больше.')
                else:
                    data.set_count_of_candies(new_count)
                    await message.reply(f'{message.from_user.first_name}, на столе теперь {new_count} конфет(ы).\n'
                                        f'Чтобы начать играть, нажми /new_game\n')
            else:
                await message.reply(f'{message.from_user.first_name}, ты ввел(а) что-то странное. '
                                    f'Введи команду снова и укажи новое количество конфет.')
        else:
            await message.answer(f'{message.from_user.first_name}, после команды /set_count нужно '
                                 f'поставить пробел, написать новое число конфет и отправить это сообщение.')