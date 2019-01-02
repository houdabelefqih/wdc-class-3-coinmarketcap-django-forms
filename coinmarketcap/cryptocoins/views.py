from django.db.models import Q
from django.shortcuts import render, redirect, get_object_or_404

from cryptocoins.models import Cryptocurrency, Exchange


def index(request):
    order_param = request.GET.get('order_param', 'rank')
    order_direction = request.GET.get('order_direction', 'asc')
    order_by = 'rank'

    coins = Cryptocurrency.objects.all()

    search = request.GET.get('search')
    if search:
        coins = coins.filter(
            Q(name__icontains=search) | Q(exchange__name__icontains=search)
        )

    if order_param == 'price':
        order_by = 'price_usd'
    if order_direction == 'desc':
        order_by = '-' + order_by

    coins = coins.order_by(order_by)
    return render(request, 'index.html', {
        'order_param': order_param,
        'order_direction': order_direction,
        'coins': coins
    })


def detail(request, coin_id):
    coin = get_object_or_404(Cryptocurrency, id=coin_id)
    return render(request, 'detail.html', {
        'coin': coin
    })


def delete(request, coin_id):
    currency = Cryptocurrency.objects.get(id=coin_id)
    if request.method == 'GET':
        return render(
            request,
            'delete_cryptocurrency.html',
            context={'currency': currency}
        )
    elif request.method == "POST":
        currency.delete()
        return redirect('index')


def create(request):
    exchanges = Exchange.objects.all()
    if request.method == 'GET':
        return render(request, 'create_cryptocurrency.html', {'exchanges': exchanges})
    elif request.method == 'POST':
        fields = [
            'name', 'slug', 'symbol', 'rank', 'price_usd', 'price_btc',
            'volume_usd_24h', 'market_cap_usd', 'available_supply',
            'total_supply', 'percent_change_1h', 'percent_change_24h',
            'percent_change_7d', 'exchange'
        ]
        errors = {}
        for field in fields:
            if not request.POST.get(field):
                errors[field] = 'This field is required.'

        if errors:
            return render(
                request,
                'create_cryptocurrency.html',
                context={'exchanges': exchanges, 'errors': errors}
            )

        exchange = Exchange.objects.get(name=request.POST.get('exchange'))
        cryptocurrency = Cryptocurrency.objects.create(
            name=request.POST.get('name'),
            slug=request.POST.get('slug'),
            symbol=request.POST.get('symbol'),
            rank=float(request.POST.get('rank')),
            price_usd=float(request.POST.get('price_usd')),
            price_btc=float(request.POST.get('price_btc')),
            volume_usd_24h=float(request.POST.get('volume_usd_24h')),
            market_cap_usd=float(request.POST.get('market_cap_usd')),
            available_supply=float(request.POST.get('available_supply')),
            total_supply=float(request.POST.get('total_supply')),
            max_supply=float(request.POST.get('max_supply')),
            percent_change_1h=float(request.POST.get('percent_change_1h')),
            percent_change_24h=float(request.POST.get('percent_change_24h')),
            percent_change_7d=float(request.POST.get('percent_change_7d')),
            exchange=exchange
        )

        return redirect('index')
