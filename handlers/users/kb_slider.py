from aiogram import types
from loader import dp
from filters import IsPrivate

from keyboards.default.keyboard_menu_2 import kb_menu2
from keyboards.default.keyboard_menu import kb_menu



@dp.message_handler(IsPrivate(), text=['Вперед➡️'])
async def next_command(message: types.Message):
    await message.answer(text='клавиатура изменена', reply_markup=kb_menu2)


@dp.message_handler(IsPrivate(), text=['Назад⬅️'])
async def back_command(message: types.Message):
    await message.answer(text='клавиатура изменена', reply_markup=kb_menu)