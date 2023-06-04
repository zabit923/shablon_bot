from aiogram import types
from aiogram.dispatcher.filters import CommandStart

from loader import bot

from loader import dp

from utils.db_api import quick_commands as commands
from filters import IsPrivate, IsSubscriber
from keyboards.default import kb_menu


# __________________________________________________________________________________________________ #

@dp.message_handler(IsPrivate(), CommandStart())
async def start_command(message: types.Message):

    args = message.get_args()
    print(args)
    new_args = await commands.check_args(args, message.from_user.id)
    new_args = int(new_args)
    try:
        await commands.add_ref(
            user_id=message.from_user.id,
            referal_id=new_args,
            )
    except Exception:
        await commands.add_ref(
            user_id=message.from_user.id,
            referal_id=0,
            )
    try:
        await dp.bot.send_message(chat_id=new_args,
                                  text=f'По твоей ссылке вошел {message.from_user.first_name}'
                                       f'Тебе зачисленно 30 на баланс')
        await commands.check_balance(user_id=new_args, amound=30)
    except Exception:
        pass

    user = await commands.select_user(message.from_user.id)

    if user.first_name == '0':
        await message.answer('Привет, пожалуйста пройди регистрацию', reply_markup=kb_menu)
    else:
        await message.answer(f'Здравствуйте <b>{user.first_name}</b>', reply_markup=kb_menu)



# __________________________________________________________________________________________________ #

@dp.message_handler(IsPrivate(), IsSubscriber(), text=['Профиль📋'])
async def profile_command(message: types.Message):

    user = await commands.select_user(message.from_user.id)
    count_refs = await commands.count_refs(user_id=message.from_user.id)
    try:
        if user == message.from_user.id or user.photo != '0':
            await bot.send_photo(message.from_user.id, photo=user.photo, caption=
                                 f'🆔Айди - {user.user_id}\n'
                                 f'👤Имя - <b>{user.first_name}</b>\n'
                                 f'📝Возраст - {user.age}\n'
                                 f'💰Баланс - {user.balance}\n'
                                 f'📪рефералов - {count_refs} \n'
                                 )
        elif user == message.from_user.id or user.photo == '0':
            await message.answer(f'🆔Айди - {user.user_id}\n'
                                 f'👤Имя - <b>{user.first_name}</b>\n'
                                 f'📝Возраст - {user.age}\n'
                                 f'💰Баланс - {user.balance}\n'
                                 f'📪рефералов - {count_refs} \n'
                                 )
    except Exception:
        await message.answer('У тебя нет профиля, зарегестрируйся')


