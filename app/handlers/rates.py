from app import parser
from aiogram import types, Dispatcher


def register_handlers_rates(dp: Dispatcher):
    dp.register_message_handler(process_rates_command, commands=['rates'])


async def process_rates_command(message: types.Message):
    data = await parser.fetch_rates()
    await message.answer(f'Інформація про поточний курс валют: \n\n'
                         f'{format_currency_data(data)}')


def format_currency_data(data):
    # Create an empty list of strings
    str_list = []
    for row in data:
        # For each available currency, add this currency rate to the list of strings
        str_list.append(f'{row["cc"]}: {row["rate"]}\n')

    return ''.join(str_list)  # Concatenate strings in list


def print_currency_data(data):
    str_list = []
    for row in data:
        # For each available currency, add this currency rate to the list of strings
        str_list.append(f'{row["cc"]:15}: {row["rate"]}\n')

    print(''.join(str_list))  # Concatenate strings in list and print
