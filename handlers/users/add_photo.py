from loader import dp
from aiogram import types
from filters import IsPrivate, IsSubscriber
from utils.db_api import quick_commands as commands

from aiogram.dispatcher import FSMContext
from states import photo
from keyboards.default import kb_menu



# ___________________________________________________________________________________________________ #


@dp.message_handler(IsPrivate(), IsSubscriber(), text=['Аватар🏙'])
async def photo_func(message: types.Message):
    user = await commands.select_user(message.from_user.id)
    try:
        if user == message.from_user.id or user.first_name != '0':
            await message.answer('Привет, скинь свое фото')
            await photo.test1.set()
    except Exception:
        await message.answer('У тебя нет профиля')


# ________________________________________________FSM________________________________________________ #

@dp.message_handler(state=photo.test1, content_types=types.ContentType.PHOTO)
async def state1(message: types.Message, state: FSMContext):
    answer = message.photo[-1].file_id

    await state.update_data(test1=answer)
    data = await state.get_data()
    photo_ = data.get('test1')


    await commands.add_photo(
        user_id=message.from_user.id,
        photo=photo_
    )

    await message.answer(f'Фото добавлено', reply_markup=kb_menu)

    await state.finish()


