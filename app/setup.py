from aiogram import Bot, Dispatcher
from aiogram.types import BotCommand

from app.handlers.help import register_handlers_help
from app.handlers.rates import register_handlers_rates
from app.handlers.convert import register_handlers_convert
from app.handlers.cancel import register_handlers_cancel


async def set_commands(bot: Bot):
    commands = [
        BotCommand('/help', 'Отримати інформацію про бота та команди'),
        BotCommand('/rates', 'Отримати інформацію про поточний курс валют'),
        BotCommand('/convert', 'Конвертувати гривні в іншу валюту'),
        BotCommand('/cancel', 'Скасувати поточну команду')
    ]
    await bot.set_my_commands(commands)


async def register_handlers(dp: Dispatcher):
    register_handlers_help(dp)
    register_handlers_rates(dp)
    register_handlers_convert(dp)
    register_handlers_cancel(dp)

