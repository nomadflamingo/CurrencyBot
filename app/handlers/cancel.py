from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext

from app.messages import MESSAGES


def register_handlers_cancel(dp: Dispatcher):
    dp.register_message_handler(process_cancel_command, commands='cancel', state='*')


async def process_cancel_command(message: types.Message, state: FSMContext):
    current_state = await state.get_state()
    if current_state is None:
        await message.answer(MESSAGES['cancel_nothing'])
    else:
        await state.finish()
        await message.answer(MESSAGES['cancel'], reply_markup=types.ReplyKeyboardRemove())
