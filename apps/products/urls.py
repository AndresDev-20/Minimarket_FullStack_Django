from django.urls import path
from django.http import HttpResponse
from . import views


urlpatterns = [
    # Productos
    path('', views.product_list, name='products'),
    # filtrado por categoria
    path('filter/', views.product_filter, name='product_filter'),
    path('create/', views.product_create, name='product_create'),
    path('edit/<int:product_id>/', views.product_edit, name='product_edit'), 
    path('delete/<int:product_id>/', views.product_delete, name='product_delete'), 
    # Categorias
    path('categories/', views.category_list, name='category'),
    path('categories/create/', views.category_create, name='category_create'),
    path('categories/edit/<int:category_id>/', views.category_edit, name='category_edit'),
    path('categories/delete/<int:category_id>/', views.category_delete, name='category_delete'),
]
