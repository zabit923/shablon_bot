from aiogram import types
from loader import dp
from filters import IsPrivate, IsSubscriber

HELP = '''
<b>/start</b>-Запустить бота
<b>Помощь</b>-получить помощь
<b>Регистрация</b>-Пройти регистрацию
<b>Обновить</b>-Обновить данные профиля
<b>Реферальная ссылка</b>-Получить реферальную ссылку
<b>Профиль</b>-Данные профиля
<b>Удалить профиль</b>-Удаление профиля
<b>Аватар</b>-Добавить фото профиля
<b>Баланс</b>-Изменить баланс
'''


@dp.message_handler(IsPrivate(), IsSubscriber(), text=['Помощь📚'])
async def help_command(message: types.Message):
    await message.answer(text=HELP, parse_mode='HTML')
