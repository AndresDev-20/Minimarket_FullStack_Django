from django.urls import path
from . import views

urlpatterns = [
    path('', views.supplier, name='supplier'),
    path('create/', views.create_supplier, name='create_supplier'),
    path('edit/<int:supplier_id>/', views.edit_supplier, name='edit_supplier'),
    path('delete/<int:supplier_id>/', views.delete_supplier, name='delete_supplier'),
]
