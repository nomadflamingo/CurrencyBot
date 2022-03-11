from aiogram import Bot
from aiogram.types import BotCommand


async def set_commands(bot: Bot):
    commands = [
        BotCommand('/help', 'Отримати інформацію про бота та команди'),
        BotCommand('/rates', 'Отримати інформацію про поточний курс валют'),
        BotCommand('/convert', 'Конвертувати гривні в іншу валюту'),
        BotCommand('/cancel', 'Скасувати поточну команду')
    ]
    await bot.set_my_commands(commands)
