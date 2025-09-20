from django.urls import path
from . import views

urlpatterns = [
    path('', views.customer, name='customer'),
    path('filter/', views.customer_filter, name='customer_filter'),
    path('create/', views.Customer_create, name='create_customer'),
    path('edit/<int:pk>/', views.Customer_edit, name='edit_customer'),
    path('delete/<int:pk>/', views.Customer_delete, name='delete_customer'),
    path('purchases/<int:pk>/', views.customer_purchases, name='customer_purchases'),
    path('detail/<int:pk>/', views.customer_detail_sale, name='customer_detail_sale'),
]
