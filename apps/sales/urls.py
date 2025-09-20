from django.urls import path
from . import views

urlpatterns = [
    path('', views.sales, name='sales'),
    path('create/', views.create_sale, name='create_sale'),
    path('detail/<int:pk>/', views.detail_sale, name='detail_sale'),
    path('detail/<int:pk>/create/', views.create_detail_sale, name='create_detail_sale'),
]
