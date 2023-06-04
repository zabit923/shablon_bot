from aiogram import types
from loader import dp
from filters import IsPrivate



@dp.message_handler(IsPrivate())
async def error_command(message: types.Message):
    await message.answer(f'Команды-{message.text}, не существует')