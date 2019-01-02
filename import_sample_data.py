import os
import random
import django
import requests

from django.conf import settings
from datetime import datetime

django.setup()
from cryptocoins.models import Cryptocurrency, Exchange


EXCHANGES = [
    {
        'name': 'Bitstamp',
        'url': 'https://www.bitstamp.net'
    },
    {
        'name': 'Poloniex',
        'url': 'https://poloniex.com'
    },
    {
        'name': 'Binance',
        'url': 'https://www.binance.com/'
    },
    {
        'name': 'OKEx',
        'url': 'https://www.okex.com'
    },
]

for exchange in EXCHANGES:
    Exchange.objects.create(
        name=exchange['name'],
        url=exchange['url'],
    )


exchanges = Exchange.objects.all()
response = requests.get('https://api.coinmarketcap.com/v1/ticker/')
for doc in response.json():
    doc['slug'] = doc['id']
    del doc['id']

    doc['volume_usd_24h'] = doc['24h_volume_usd']
    del doc['24h_volume_usd']

    doc['last_updated'] = datetime.fromtimestamp(int(doc['last_updated']))

    doc['exchange'] = random.choice(exchanges)

    Cryptocurrency.objects.create(**doc)
