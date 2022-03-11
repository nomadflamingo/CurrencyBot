import logging
import os

from aiogram import Bot, executor, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.contrib.middlewares.logging import LoggingMiddleware

from app.handlers.register_handlers import register_handlers


async def set_commands(_):
    """
    Set commands list
    """
    commands = [
        types.BotCommand('/help', 'Отримати інформацію про бота та команди'),
        types.BotCommand('/rates', 'Отримати інформацію про поточний курс валют'),
        types.BotCommand('/convert', 'Конвертувати гривні в іншу валюту')
    ]
    await bot.set_my_commands(commands)


API_TOKEN = os.getenv('API_TOKEN')

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot, storage=MemoryStorage())
dp.middleware.setup(LoggingMiddleware())

if __name__ == '__main__':
    executor.start_polling(dp, on_startup=[set_commands, register_handlers])
