from django.db.models import Q
from django.shortcuts import render, redirect, get_object_or_404

from cryptocoins.forms import CryptocurrencyForm
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
    if request.method == 'GET':
        cryptocurrency_form = CryptocurrencyForm()
        return render(
            request,
            'create_cryptocurrency.html',
            context={'cryptocurrency_form': cryptocurrency_form}
        )
    elif request.method == 'POST':
        cryptocurrency_form = CryptocurrencyForm(request.POST)
        if cryptocurrency_form.is_valid():
            cryptocurrency = Cryptocurrency.objects.create(
                **cryptocurrency_form.cleaned_data)
            return redirect('index')

        return render(
            request,
            'create_cryptocurrency.html',
            context={'cryptocurrency_form': cryptocurrency_form}
        )
