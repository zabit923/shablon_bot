from loader import dp
from aiogram import types
from filters import IsPrivate, IsSubscriber
from utils.db_api import quick_commands as commands
from utils.db_api.quick_commands import User

from keyboards.inline import ikb_menu
from keyboards.default import kb_menu

from loader import bot




@dp.message_handler(IsPrivate(), IsSubscriber(), text='Удалить профиль🗑')
async def show_inline(message: types.Message):
    user = await User.get(message.from_user.id)
    try:
        if user == message.from_user.id or user.first_name != '0':
            await message.answer(text='Вы уверены?', reply_markup=ikb_menu)
    except Exception:
        await bot.send_message(message.from_user.id, text='У вас нет профиля, чтоб его удалять')







@dp.callback_query_handler(text='Нет')
async def save_profile(callback: types.CallbackQuery):
    await bot.send_message(callback.from_user.id, text='Профиль не удален')
    await callback.answer('')


@dp.callback_query_handler(text='Да')
async def del_profile(callback: types.CallbackQuery):
    user = await commands.select_user(user_id=callback.from_user.id)
    await user.delete()

    await bot.send_message(callback.from_user.id, 'Профиль удален', reply_markup=kb_menu)
    await callback.answer('')


