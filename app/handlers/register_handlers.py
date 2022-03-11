from aiogram import Dispatcher

from app.handlers.cancel import register_handlers_cancel
from app.handlers.convert import register_handlers_convert
from app.handlers.help import register_handlers_help
from app.handlers.rates import register_handlers_rates


async def register_handlers(dp: Dispatcher):
    register_handlers_cancel(dp)
    register_handlers_convert(dp)
    register_handlers_help(dp)
    register_handlers_rates(dp)
