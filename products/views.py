import json
from django.shortcuts import render

from .models import Product


def product_list_view(request):
    # with open('products/fixtures/data/data.json') as file:
    #     data = json.load(file)
    data = Product.objects.all()
    return render(
        request, 'products/catalog.html',
        {'object_list': data}
    )


def product_detail_view(request, pk):
    # with open('products/fixtures/data/data.json') as file:
    #     data = json.load(file)

    data = Product.objects.get(pk=pk)
    return render(
        request,
        'products/detail.html',
        {'object': data}
        # [idx]
    )
