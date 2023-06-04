from aiogram.dispatcher.filters.state import StatesGroup, State


class edit_states(StatesGroup):  # Определяем класс register, который наследуется от класса StatesGroup
    test1 = State()  # Состояние test1
    test2 = State()  # Состояние test2

    # Они позволяют отслеживать прогресс бота в разговоре с пользователем
    # и действовать по-разному в зависимости от текущего состояния