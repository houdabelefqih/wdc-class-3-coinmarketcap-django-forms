from django.contrib import admin

from .models import Cryptocurrency, Exchange


@admin.register(Cryptocurrency)
class CryptocurrencyAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'symbol', 'exchange', 'price_usd', 'rank',
                    'volume_usd_24h', 'total_supply', 'last_updated')


@admin.register(Exchange)
class ExchangeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'url')
