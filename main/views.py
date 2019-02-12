from django.template import Template, Context
from django.template.loader import get_template, render_to_string
from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    template = get_template(
        'main/index.html'
    )
    context = {
        'name': 'Anton'
    }
    return HttpResponse(
        template.render(context)
    )
    # template = Template(
    #     'Hello {{ name }}'
    # )
    # context = Context({
    #     'name': 'Anton'
    # })
    # return HttpResponse(
    #     template.render(context)
    # )
    # return render(
    #  request,
    # 'main/index.html'
    # )


def contact(request):
    template = get_template(
        'main/contact.html'
    )
    context = {
        'name': 'Anton'
    }
    return HttpResponse(
        template.render(context)
    )
    # te


# def catalog(request):
#     template = get_template(
#         'main/catalog.html'
#     )
#     context = {
#         'name': 'Anton'
#     }
#     return HttpResponse(
#         template.render(context)
#     )


def product_details(request):
    template = get_template(
        'main/product_details.html'
    )
    context = {
        'name': 'Anton'
    }
    return HttpResponse(
        template.render(context)
    )
