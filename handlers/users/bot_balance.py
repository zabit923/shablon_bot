from aiogram import types
from filters import IsPrivate, IsSubscriber
from keyboards.default import kb_menu
from loader import dp
from states.balance import balance_state
from utils.db_api import quick_commands as commands
from aiogram.dispatcher import FSMContext
from keyboards.inline import balance_kb

from loader import bot




@dp.message_handler(IsPrivate(), IsSubscriber(), text='Баланс💰')
async def change_balance(message: types.Message):
    user = await commands.select_user(message.from_user.id)
    try:
        if user.first_name != '0' or user == message.from_user.id:
            await message.answer(f'Ваш баланс: {user.balance}'
                                 f' Хотите изменить баланс?', reply_markup=balance_kb)
    except Exception:
        await message.answer('Ты не зарегестрирован')



@dp.callback_query_handler(text='нет_')
async def edit_balance(callback: types.CallbackQuery):
    await bot.send_message(callback.from_user.id, text='Баланс не изменен')
    await callback.answer('')


@dp.callback_query_handler(text='да_')
async def edit_balance(callback: types.CallbackQuery):
    await bot.send_message(callback.from_user.id, text='Введите сумму пополнения:')
    await balance_state.amound.set()
    await callback.answer('')




@dp.message_handler(IsPrivate(), state=balance_state.amound)
async def change_balance_(message: types.Message, state: FSMContext):
    answer = message.text
    check_balance = await commands.check_balance(user_id=message.from_user.id, amound=answer)
    if check_balance == 'no money':
        await message.answer('Баланс пуст', reply_markup=kb_menu)
        await state.finish()
    elif check_balance:
        await message.answer('Баланс изменен', reply_markup=kb_menu)
        await state.finish()
    elif not check_balance:
        await message.answer('Некоректное число')
        await state.finish()
    else:
        await message.answer('Ошибка , используйте команду /start')
        await state.finish()
