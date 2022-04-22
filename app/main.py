import logging
import os

from aiogram import Bot, executor, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.contrib.middlewares.logging import LoggingMiddleware

from app import setup


API_TOKEN = os.getenv('API_TOKEN')

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dispatcher = Dispatcher(bot, storage=MemoryStorage())
dispatcher.middleware.setup(LoggingMiddleware())


async def on_startup(dp: Dispatcher):
    await setup.set_commands(bot)
    await setup.register_handlers(dp)

if __name__ == '__main__':
    executor.start_polling(dispatcher, on_startup=[on_startup])
