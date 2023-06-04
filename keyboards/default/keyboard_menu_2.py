from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


kb_menu2 = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Назад⬅️')
        ]
    ],
    resize_keyboard=True
)