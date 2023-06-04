from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


kb_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Регистрация⚙️'),
        ],
        [
            KeyboardButton(text='Обновить профиль🔄'),
            KeyboardButton(text='Профиль📋'),
            KeyboardButton(text='Баланс💰'),
        ],
        [
            KeyboardButton(text='Помощь📚'),
            KeyboardButton(text='Удалить профиль🗑'),
            KeyboardButton(text='Аватар🏙'),
        ],
        [
            KeyboardButton(text='Реф. ссылка✉️'),
            KeyboardButton(text='Вперед➡️')
        ],
    ],
    resize_keyboard=True
)