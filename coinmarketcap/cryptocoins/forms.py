from django import forms

from cryptocoins.models import Cryptocurrency, Exchange


class CryptocurrencyForm(forms.Form):
    name = forms.CharField(label='Name', max_length=100)
    slug = forms.CharField(label='Slug', max_length=100)
    symbol = forms.CharField(label='Symbol', max_length=10)
    rank = forms.IntegerField(label='Rank')
    price_usd = forms.DecimalField(
        label='Price USD', max_digits=7, decimal_places=2)
    price_btc = forms.DecimalField(
        label='Price BTC', max_digits=8, decimal_places=7)
    volume_usd_24h = forms.DecimalField(
        label='Volume USD 24hs', max_digits=14, decimal_places=2)
    market_cap_usd = forms.DecimalField(
        label='Market Cap USD', max_digits=14, decimal_places=2)
    available_supply = forms.DecimalField(
        label='Available Supply', max_digits=20, decimal_places=2)
    total_supply = forms.DecimalField(
        label='Total Supply', max_digits=20, decimal_places=2)
    max_supply = forms.DecimalField(
        label='Max Supply', required=False, max_digits=20, decimal_places=2)
    percent_change_1h = forms.DecimalField(
        label='Percent Change 1hr', max_digits=5, decimal_places=2)
    percent_change_24h = forms.DecimalField(
        label='Percent Change 24hs', max_digits=5, decimal_places=2)
    percent_change_7d = forms.DecimalField(
        label='Percent Change 1d', max_digits=5, decimal_places=2)
    exchange = forms.ModelChoiceField(
        label='Exchange', queryset=Exchange.objects.all())
