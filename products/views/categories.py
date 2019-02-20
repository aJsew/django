import json
from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import Http404

from products.models import Category
from products.forms import CategoryForm, CategoryModelForm


def category_create_view(request):
    form = CategoryModelForm()
    success_url = reverse('products:list')

    if request.method == 'POST':
        form = CategoryModelForm(data=request.POST)

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
        'categories/create.html',
        {'form': form},
    )


def category_update_view(request, pk):
    try:
        obj = Category.objects.get(pk=pk)
    except Exception as err:
        raise Http404
    form = CategoryModelForm(instance=obj)
    success_url = reverse('products:list')

    if request.method == 'POST':
        form = CategoryModelForm(
            request.POST,
            files=request.FILES,
            initial=obj
        )

        if form.is_valid():
            form.save()

            return redirect(success_url)

    return render(
        request,
        'categories/update.html',
        {'form': form}
    )
