import json
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.http import Http404
from django.views.generic import (
    ListView, DetailView, CreateView, UpdateView, DeleteView
)

from products.models import Product
from products.forms import ProductForm

class ProductListView(ListView):
    model = Product
    template_name = 'products/catalog.html'

class ProductDetailView(DetailView):
    model = Product
    template_name = 'products/detail.html'

class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'products/create.html'
    success_url = reverse_lazy('products:list')

class ProductUpdateView(UpdateView):
    model = Product
    fields = [
        'name', 'image', 'category',
        'description', 'cost'
    ]
    template_name = 'products/create.html'
    success_url = reverse_lazy('products:list')

class ProductDeleteView(DeleteView):
    model = Product
    template_name = 'products/delete.html'
    success_url = reverse_lazy('products:list')


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


def product_create_view(request):
    form = ProductForm()
    success_url = reverse('products:list')

    if request.method == 'POST':
        form = ProductForm(data=request.POST)

        if form.is_valid():
            form.save()
            # obj = Category(
            #     name=form.cleaned_data.get('name'),
            #     description=form.cleaned_data.get('description'),
            # )
            # obj.save()

            return redirect(success_url)

    return render(
        request,
        'products/create.html',
        {'form': form},
    )


def product_update_view(request, pk):
    obj = get_object_or_404(Product, pk=pk)

    form = ProductForm(instance=obj)
    success_url = reverse('products:list')

    if request.method == 'POST':
        form = ProductForm(
            request.POST,
            files=request.FILES,
            instance=obj
        )

        if form.is_valid():
            form.save()

            return redirect(success_url)

    return render(
        request,
        'products/update.html',
        {'form': form}
    )


def product_delete_view(request, pk):
    obj = get_object_or_404(Product, pk=pk)
    success_url = reverse('products:list')

    if request.method == 'POST':
        obj.delete()

        return redirect(success_url)

    return render(
        request,
        'products/delete.html',
        {'object': obj}
    )

