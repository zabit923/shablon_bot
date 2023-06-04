from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

balance_kb = InlineKeyboardMarkup(row_width=2,
    inline_keyboard=[
        [
            InlineKeyboardButton('Да', callback_data='да_')
        ],
        [
           InlineKeyboardButton('Нет', callback_data='нет_')
        ]
])