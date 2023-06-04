from aiogram import types
from aiogram.dispatcher.filters import BoundFilter
from aiogram.dispatcher.handler import CancelHandler
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from data import config
from loader import bot, dp


class IsSubscriber(BoundFilter):
    async def check(self, message: types.Message):
        subscribes = 0
        for chat_id in config.chat_ids:
            sub = await bot.get_chat_member(chat_id=chat_id, user_id=message.from_user.id)
            if sub.status != types.ChatMemberStatus.LEFT:
                subscribes += 1
            else:
                break
        else:
            if subscribes == len(config.chat_ids):
                return True
            else:
                markup = InlineKeyboardMarkup(row_width=1,
                                              inline_keyboard=[
                                                  [
                                                      InlineKeyboardButton('Телеграм чат', url='-865051211')
                                                  ]
                                              ])
                await dp.bot.send_message(chat_id=message.from_user.id, text=f'Подпишитесь на телеграм чат и '
                                                                             f'повторите попытку',
                                          reply_markup=markup)
                raise CancelHandler()