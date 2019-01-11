from django import forms

from cryptocoins.models import Cryptocurrency, Exchange


class CryptocurrencyForm(forms.ModelForm):
    CHOICES=[
        (True, 'Yes'),
        (False, 'No')
    ]
    is_active = forms.ChoiceField(
        label="Is active?", choices=CHOICES, initial=CHOICES[0][0],
        widget=forms.RadioSelect
    )

    class Meta:
        model = Cryptocurrency
        fields = [
            'name', 'slug', 'symbol', 'rank', 'price_usd', 'price_btc',
            'volume_usd_24h', 'market_cap_usd', 'available_supply',
            'total_supply', 'max_supply', 'percent_change_1h',
            'percent_change_24h', 'percent_change_7d', 'exchange',
            'is_active'
        ]

    def clean_price_usd(self):
        price_usd = self.cleaned_data['price_usd']
        if price_usd < 0:
            raise forms.ValidationError("Price can't be a negative number")

        return price_usd

    def clean(self):
        cleaned_data = super().clean()
        name = cleaned_data.get("name")

        if Cryptocurrency.objects.filter(name__iexact=name).exists():
            msg = "There's already a Cryptocurrency called {}".format(name)
            self.add_error('name', msg)
