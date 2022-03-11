from aiogram import types, Dispatcher

from app.messages import MESSAGES


def register_handlers_help(dp: Dispatcher):
    dp.register_message_handler(process_help_command, commands=['start', 'help'])


async def process_help_command(message: types.Message):
    await message.answer(MESSAGES['help'], parse_mode='Markdown')
