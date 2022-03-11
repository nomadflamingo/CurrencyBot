help_message = 'Цей бот дозволяє конвертувати валюту та бачити поточний курс. \n' \
               '*Дані взяти з офіційного сайту* [НБУ](https://bank.gov.ua/)'

currency_code_prompt_message = 'Введіть код валюти, в яку хочете перевести:'
invalid_currency_code_message = 'Код валюти введено некоректно'
amount_prompt_message = 'Введіть суму грошей:'
invalid_amount_message = 'Сума грошей введена некоректно (має бути додатнє число)'
command_cancelled_message = 'Команда скасована'
no_command_cancelled_message = 'Нема активних команд для скасування'

MESSAGES = {
    'help': help_message,
    'cc_prompt': currency_code_prompt_message,
    'cc_invalid': invalid_currency_code_message,
    'amount_prompt': amount_prompt_message,
    'amount_invalid': invalid_amount_message,
    'cancel': command_cancelled_message,
    'cancel_nothing': no_command_cancelled_message,
}
