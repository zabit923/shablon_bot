from aiogram import Dispatcher
from .private_chat import IsPrivate
from .chat_subscriber import IsSubscriber




def setup(dp: Dispatcher):
    dp.filters_factory.bind(IsPrivate)
    dp.filters_factory.bind(IsSubscriber)
