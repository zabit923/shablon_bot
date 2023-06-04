from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

delete_kb = InlineKeyboardMarkup(row_width=2,
                                 inline_keyboard=[
                                     [
                                         InlineKeyboardButton('Да', callback_data='да')
                                     ],
                                     [
                                         InlineKeyboardButton('Нет', callback_data='нет')
                                     ]
                                 ])
