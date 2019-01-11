from django import forms

from cryptocoins.models import Cryptocurrency, Exchange


class CryptocurrencyForm(forms.ModelForm):
    class Meta:
        model = Cryptocurrency
        fields = [
            'name', 'slug', 'symbol', 'rank', 'price_usd', 'price_btc',
            'volume_usd_24h', 'market_cap_usd', 'available_supply',
            'total_supply', 'max_supply', 'percent_change_1h',
            'percent_change_24h', 'percent_change_7d', 'exchange',
            'is_active'
        ]
