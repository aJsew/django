from django.urls import path
from .views import (
    product_list_view, product_detail_view,
    category_create_view, category_update_view
)


urlpatterns = [
    path('', product_list_view, name='list'),
    path('<int:pk>/', product_detail_view, name='detail'),
    path('categories/create/', category_create_view, name='category'),
    path('categories/<int:pk>/update/', category_update_view, name='update'),
]
