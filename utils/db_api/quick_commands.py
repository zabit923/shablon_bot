from utils.db_api.schemas.user import User
from asyncpg import UniqueViolationError
from utils.db_api.DB import db



# __________________________________________________________________________________________________ #
async def update_user(user_id: int, first_name: str, age: str, photo: str):
    user = await User.get(user_id)
    try:
        await user.update(
            first_name=first_name,
            age=age,
            balance=user.balance,
            photo=photo
        ).apply()
        print(f'Данные пользователя с id {user_id} обновлены')
    except Exception:
        print(f'Ошибка при обновлении данных пользователя')
# __________________________________________________________________________________________________ #

async def add_ref(user_id: int, referal_id: int):
    try:
        user = User(user_id=user_id,
                    first_name='0',
                    age='0',
                    referal_id=referal_id,
                    balance=0,
                    photo='0'
                    )
        await user.create()
    except UniqueViolationError:
        pass

# __________________________________________________________________________________________________ #

async def add_photo(user_id: int, photo: str):
    user = await User.get(user_id)
    try:
        await user.update(
            photo=photo
        ).apply()
    except UniqueViolationError:
        pass

# __________________________________________________________________________________________________ #

async def select_all_users():
    users = await User.query.gino.all()
    return users

# __________________________________________________________________________________________________ #

async def count_users():
    count = db.func.count(User.user_id).gino.scalar()
    return count

# __________________________________________________________________________________________________ #

async def select_user(user_id):
    user = await User.query.where(User.user_id == user_id).gino.first()
    return user

# __________________________________________________________________________________________________ #

async def update_status(user_id, status):
    user = await select_user(user_id)
    await user.update(status=status).apply()

# __________________________________________________________________________________________________ #

async def count_refs(user_id):
    refs = await User.query.where(User.referal_id == user_id).gino.all()
    return len(refs)

# __________________________________________________________________________________________________ #

# Функция для передачи аргументов переданных при регистрации
async def check_args(args, user_id: int):
    if args == '':
        args = '0'
        return args

# Если в аргумент переданы не только числа, а и буквы
    elif not args.isnumeric():
        args = '0'
        return args

# Если в аргумент переданы ТОЛЬКО числа
    elif args.isnumeric():

        # Если аргумент такой же как и айди пользователя
        if int(args) == user_id:
            args = '0'
            return args

        # Получаем из базы данных пользователя у которого user_id такой же как и переданый аргумент
        elif await select_user(user_id=int(args)) is None:
            args = '0'
            return args

        # Если наш аргумент прошел все проверки, то возвращаем его
        else:
            args = str(args)
            return args

    # Если что то пошло не так
    else:
        args = '0'
        return args

# __________________________________________________________________________________________________ #

async def change_balance(user_id: int, amound):
    user = await select_user(user_id)
    new_balance = user.balance + amound
    await user.update(balance=new_balance).apply()


# __________________________________________________________________________________________________ #

async def check_balance(user_id: int, amound):
    user = await select_user(user_id)
    try:
        amound = float(amound)
        if user.balance + amound >= 0:
            await change_balance(user_id, amound)
            return True
        elif user.balance + amound < 0:
            return 'no money'
    except Exception:
        return False



