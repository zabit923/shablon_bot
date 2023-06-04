from aiogram import types
from aiogram.utils.deep_linking import get_start_link


from loader import dp
from filters import IsPrivate, IsSubscriber
from utils.db_api import quick_commands as commands




@dp.message_handler(IsPrivate(), IsSubscriber(), text=['Реф. ссылка✉️'])
async def ref_command(message: types.Message):
    user = await commands.select_user(message.from_user.id)
    try:
        if user == message.from_user.id or user.first_name != '0':
            ref_link = await get_start_link(payload=message.from_user.id)
            count_refs = await commands.count_refs(user_id=message.from_user.id)
            await message.answer(f'Привет <b>{user.first_name}</b>\n'
                                 f'У тебя {count_refs} рефералов\n'
                                 f'Твоя реферальная ссылка:\n'
                                 f'{ref_link}')
    except Exception:
        await message.answer(f'У тебя нет профиля чтоб кого-то приглашать, зарегестрируйся')

