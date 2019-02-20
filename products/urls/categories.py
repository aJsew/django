from django.urls import path
from products.views import (
    category_create_view, category_update_view
)

app_name = 'categories'

urlpatterns = [
    path('create/', category_create_view, name='category'),
    path('<int:pk>/update/', category_update_view, name='update'),
]

