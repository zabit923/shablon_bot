import logging
from aiogram import Dispatcher
from data.config import admins




async def on_startup_notify(dp: Dispatcher):
    for admin in admins:    # Проходимся по ID админов
        try:
            text = 'Бот запущен'
            await dp.bot.send_message(chat_id=admin, text=text)     # Уведомляем админов о запуске бота (используя их ID в chat_id)
        except Exception as err:
            logging.exception(err)