from aiogram import Bot, Dispatcher, types
from data import config
from aiogram.contrib.fsm_storage.memory import MemoryStorage

from utils.db_api.DB import db


# Создаем переменную бота где токен=config.BOT_TOKEN
bot = Bot(token=config.BOT_TOKEN, parse_mode=types.ParseMode.HTML)


storage = MemoryStorage()


# Создаем диспетчер
dp = Dispatcher(bot, storage=storage)



__all__ = ['bot', 'storage', 'dp', 'db']