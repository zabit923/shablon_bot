from loader import dp
from aiogram import types
from filters import IsPrivate, IsSubscriber
from utils.db_api import quick_commands as commands


from aiogram.dispatcher import FSMContext
from states import register
from keyboards.default import kb_menu



# ___________________________________________ /register _____________________________________________ #


@dp.message_handler(IsPrivate(), IsSubscriber(), text=['Регистрация⚙️'])
async def register_(message: types.Message):
    user = await commands.select_user(message.from_user.id)
    try:
        if user.first_name == '0':
            await message.answer('Привет, ты начал регистрацию,\nВведи свое имя')
            await register.test1.set()
        else:
            await message.answer(f'Привет  <b>{user.first_name}</b>\n'
                                 f'Ты уже был зарегестрирован')
    except Exception:
        if user != message.from_user.id:
            await commands.add_ref(user_id=message.from_user.id,
                                   referal_id=0
                                   )
            await message.answer('Привет, ты начал регистрацию,\nВведи свое имя')
            await register.test1.set()
        else:
            await message.answer('Привет, ты начал регистрацию,\nВведи свое имя')
            await register.test1.set()  # Устанавливаем состояние state1


# ________________________________________________FSM________________________________________________ #

@dp.message_handler(state=register.test1)  # Ловит все сообщения когда пользователь находится в состоянии register.state1
async def state1(message: types.Message, state: FSMContext):
    answer = message.text  # Получаем текст который отправил пользователь

    await state.update_data(test1=answer)  # Обновляем данные (в test1 записываем ответ пользователя)
    await message.answer(f'<b>{answer}</b>, сколько тебе лет?')
    await register.test2.set()  # Устанавливаем состояние register.test2


# ________________________________________________test2________________________________________________ #


@dp.message_handler(state=register.test2)  # Ловит все сообщения когда пользователь находится в состоянии register.state2
async def state2(message: types.Message, state: FSMContext):
    answer = message.text  # Получаем текст который отправил пользователь

    await state.update_data(test2=answer)  # Обновляем данные (в test2 записываем ответ пользователя)
    data = await state.get_data()  # Создаем data через которую будем доставать ответы пользователя
    name = data.get('test1')  # Достаем имя из data
    years = data.get('test2')  # Достаем возраст из data

    await commands.update_user(
        user_id=message.from_user.id,
        first_name=name,
        age=years,
        photo='0'
    )

    await message.answer(f'Регистрация завершена', reply_markup=kb_menu)

    await state.finish()  # Завершаем состояние для пользователя
