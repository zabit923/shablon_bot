from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

ikb_menu = InlineKeyboardMarkup(row_width=2,
                                inline_keyboard=[
                                    [
                                        InlineKeyboardButton('Да', callback_data='Да')
                                    ],
                                    [
                                        InlineKeyboardButton('Нет', callback_data='Нет')
                                    ],
                                ])
