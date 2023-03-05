from django.shortcuts import render, redirect
from .models import Phone


def index(request):
    return redirect('catalog')


def show_catalog(request):
    SORTS_DICT = {
        "min_price": "price",
        "max_price": "-price",
        "name": "name"
    }

    template = 'catalog.html'
    phones = Phone.objects.all()

    sort_parameter = request.GET.get("sort")

    if sort_parameter:
        phones = phones.order_by(SORTS_DICT.get(sort_parameter, "name"))

    context = {
        "phones": phones
    }
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    phone = Phone.objects.get(slug=slug)

    context = {
        "phone": phone,
    }

    return render(request, template, context)
