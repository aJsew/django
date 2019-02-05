from django.shortcuts import render


def product_list_view(request):
    return render(
        request, 'products/catalog.html'
    )
