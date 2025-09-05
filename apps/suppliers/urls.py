from django.urls import path
from . import views

urlpatterns = [
    path('', views.supplier, name='supplier'),
]
