import json
import urllib.request
from string import Template
import time

# Configure source url
CURRENCY_RATES_SRC = 'https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?json'
CURRENCY_CODE_REQUEST_TEMPLATE = Template('https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?valcode=$cc&date=$date&json')


async def fetch_rates():
    """
    Fetch rates for every currency available
    """
    with urllib.request.urlopen(CURRENCY_RATES_SRC) as response:
        return json.loads(response.read())


def fetch_rate_for_currency(currency_code):
    """
    Fetch rate for the specific currency
    """
    request_url = CURRENCY_CODE_REQUEST_TEMPLATE.substitute(cc=currency_code, date=time.strftime('%Y%m%d'))
    with urllib.request.urlopen(request_url) as response:
        return json.loads(response.read())
