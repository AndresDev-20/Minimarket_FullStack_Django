from django.urls import path
from . import views

urlpatterns = [
    path('', views.customer, name='customer'),
   # path('/create', views.Customer_create, name='create_customer'),
]
