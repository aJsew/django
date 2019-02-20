from django.urls import path
from .views import (
    index, contact, product_details
)

app_name = 'main'

urlpatterns = [
    path('product_details/', product_details),
    path('contact/', contact),
    path('', index),
]