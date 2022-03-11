from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import StatesGroup, State

from app import parser
from app.utils import isfloat
from app.messages import MESSAGES


class ConvertForm(StatesGroup):
    currency_code = State()
    amount = State()


def register_handlers_convert(dp: Dispatcher):
    dp.register_message_handler(process_convert_command, commands='convert')
    dp.register_message_handler(process_currency_code, state=ConvertForm.currency_code)
    dp.register_message_handler(process_amount_invalid,
                                lambda message: not isfloat(message.text) or not float(message.text) > 0,
                                state=ConvertForm.amount)
    dp.register_message_handler(process_amount_valid, lambda message: isfloat(message.text) and float(message.text) > 0,
                                state=ConvertForm.amount)


async def process_convert_command(message: types.Message):
    """
    Entry point for converting currency
    """
    await ConvertForm.currency_code.set()

    await message.answer(MESSAGES['cc_prompt'])


async def process_currency_code(message: types.Message, state: FSMContext):
    """
    Process currency code entered by user
    """

    # TODO: check that user sent valid text

    # Receive data
    data = parser.fetch_rate_for_currency(message.text)

    # Check that received data is not empty
    if len(data) == 0:
        await message.answer(f'{MESSAGES["cc_invalid"]}\n{MESSAGES["cc_prompt"]}')
    else:
        async with state.proxy() as form_data:
            form_data['cc'] = message.text
            form_data['rate'] = data[0]['rate']

        await ConvertForm.amount.set()
        await message.answer(MESSAGES["amount_prompt"])


async def process_amount_invalid(message: types.Message):
    """
    Process invalid amount entered by user (if either not a digit or not positive)
    """
    await message.answer(f'{MESSAGES["amount_invalid"]}\n{MESSAGES["amount_prompt"]}')


async def process_amount_valid(message: types.Message, state: FSMContext):
    """
    Process amount entered by user
    """
    amount = float(message.text)
    async with state.proxy() as form_data:
        converted_amount = amount / form_data['rate']
        await message.answer(f'{amount} UAH = {round(converted_amount, 2)} {form_data["cc"].upper()}')

    await state.finish()
