from django.urls import path
from django.http import HttpResponse
from . import views


urlpatterns = [
    # Productos
    path('', views.product_list, name='products'),
    path('create/', views.product_create, name='product_create'),
    # Categorias
    path('categories/', views.category_list, name='category'),
    path('categories/create/', views.category_create, name='category_create')
]
