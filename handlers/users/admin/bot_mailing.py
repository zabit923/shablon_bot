from aiogram import types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from asyncio import sleep

from filters import IsPrivate, IsSubscriber
from loader import dp
from utils.db_api import quick_commands as commands
from aiogram.dispatcher import FSMContext

from states.Mailing import bot_mailing
from data.config import admins





@dp.message_handler(IsPrivate(), IsSubscriber(), text='Рассылка', chat_id=admins)
async def start_mailing(message: types.Message):
    user = await commands.select_user(message.from_user.id)
    try:
        if user.first_name != '0' or user == message.from_user.id:
            await message.answer(f'Введите текст рассылки:')
            await bot_mailing.text.set()
    except Exception:
        await message.answer('Ты не зарегестрирован')

# ______________________________________________________________________________________ #

@dp.message_handler(IsPrivate(), state=bot_mailing.text)
async def mailing_text(message: types.Message, state: FSMContext):
    answer = message.text
    markup = InlineKeyboardMarkup(row_width=2,
                                  inline_keyboard=[
                                      [
                                          InlineKeyboardButton(text='Добавить фото', callback_data='Да__'),
                                          InlineKeyboardButton(text='Далее', callback_data='Нет__'),
                                          InlineKeyboardButton('Отменить', callback_data='quit')
                                      ]
                                  ])
    await state.update_data(text=answer)
    await message.answer(text=answer, reply_markup=markup)
    await bot_mailing.state.set()

# ______________________________________________________________________________________ #

@dp.callback_query_handler(text='Нет__', state=bot_mailing.state)
async def start(callback: types.CallbackQuery, state: FSMContext):
    users = await commands.select_all_users()
    data = await state.get_data()
    text = data.get('text')
    await state.finish()
    for user in users:
        try:
            await dp.bot.send_message(chat_id=user.user_id, text=text)
            print(user.user_id)
            await sleep(0.33)
        except Exception:
            pass
    await callback.message.answer('Рассылка выполнена')
    await callback.answer('')

# ______________________________________________________________________________________ #

@dp.callback_query_handler(text='Да__', state=bot_mailing.state)
async def add_photo(callback: types.CallbackQuery):
    await callback.message.answer('Пришлите фото')
    await bot_mailing.photo.set()
    await callback.answer('')

# ______________________________________________________________________________________ #

@dp.message_handler(IsPrivate(), state=bot_mailing.photo, content_types=types.ContentType.PHOTO)
async def mailing__(message: types.Message, state: FSMContext):
    photo_file_id = message.photo[-1].file_id
    await state.update_data(photo=photo_file_id)
    data = await state.get_data()
    text = data.get('text')
    photo = data.get('photo')
    markup = InlineKeyboardMarkup(row_width=2,
                                  inline_keyboard=[
                                      [
                                          InlineKeyboardButton(text='Далее', callback_data='Нет__'),
                                          InlineKeyboardButton('Отменить', callback_data='quit')
                                      ]
                                  ])
    await message.answer_photo(photo=photo, caption=text, reply_markup=markup)

# ______________________________________________________________________________________ #

@dp.callback_query_handler(text='Нет__', state=bot_mailing.photo)
async def start(callback: types.CallbackQuery, state: FSMContext):
    users = await commands.select_all_users()
    data = await state.get_data()
    text = data.get('text')
    photo = data.get('photo')
    await state.finish()
    for user in users:
        try:
            await dp.bot.send_photo(chat_id=user.user_id, photo=photo, caption=text)
            print(user.user_id)
            await sleep(0.33)
        except Exception:
            pass
    await callback.message.answer('Рассылка выполнена')
    await callback.answer('')


# ______________________________________________________________________________________ #

@dp.message_handler(IsPrivate(), state=bot_mailing.photo)
async def no_photo(message: types.Message):
    markup = InlineKeyboardMarkup(row_width=2,
                                  inline_keyboard=[
                                      InlineKeyboardButton('Отменить', callback_data='quit')
                                  ])
    await message.answer('Пришли фотографию', reply_markup=markup)

# ______________________________________________________________________________________ #

@dp.callback_query_handler(text='quit', state=[bot_mailing.text, bot_mailing.text, bot_mailing.state])
async def quit_(callback: types.CallbackQuery, state: FSMContext):
    await state.finish()
    await callback.message.answer('Рассылка отменена')
    await callback.answer('')









