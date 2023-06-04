from handlers.users.bot_start import dp
from handlers.users.help import dp
from handlers.users.edit_profile import dp
from handlers.users.delete_profile import dp
from handlers.users.register import dp
from handlers.users.bot_balance import dp
from handlers.users.kb_slider import dp
from handlers.users.bot_referrals import dp
from handlers.users.add_photo import dp
from .admin import dp
from handlers.users.error_handler import dp


__all__ = ['dp']