from aiogram import types
from aiogram.dispatcher.filters import BoundFilter



class IsPrivate(BoundFilter):                               # Создаем класс IsPrivate для проверки типа чата
    async def check(self, message: types.Message):          #  Метод check проверяет, является ли тип чата Private
        return message.chat.type == types.ChatType.PRIVATE  # Если тип чата Private, то метод возвращает True, иначе False