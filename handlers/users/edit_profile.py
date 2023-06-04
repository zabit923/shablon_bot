from loader import dp
from aiogram import types
from filters import IsPrivate, IsSubscriber
from utils.db_api import quick_commands as commands

from aiogram.dispatcher import FSMContext
from states import edit_states
from keyboards.default import kb_menu



# ___________________________________________________________________________________________________ #


@dp.message_handler(IsPrivate(), IsSubscriber(), text=['Обновить профиль🔄'])
async def edit_func(message: types.Message):
    user = await commands.select_user(message.from_user.id)
    try:
        if user.first_name != '0' or user == message.from_user.id:
            await message.answer('Введи новое имя')
            await edit_states.test1.set()
    except Exception:
        await message.answer('Сперва создайте профиль')


# ________________________________________________FSM________________________________________________ #

@dp.message_handler(state=edit_states.test1)
async def state1(message: types.Message, state: FSMContext):
    answer = message.text

    await state.update_data(test1=answer)
    await message.answer(f'{answer}, сколько тебе лет?')
    await edit_states.test2.set()



# ________________________________________________test2________________________________________________ #


@dp.message_handler(state=edit_states.test2)
async def state2(message: types.Message, state: FSMContext):
    answer = message.text


    await state.update_data(test2=answer)
    data = await state.get_data()
    name = data.get('test1')
    years = data.get('test2')


    await commands.update_user(
        user_id=message.from_user.id,
        first_name=name,
        age=years,
        photo='0'
    )
    await message.answer(f'Профиль обновлен', reply_markup=kb_menu)

    await state.finish()
