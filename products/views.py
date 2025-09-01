from django.shortcuts import render
from .models import Product

# Create your views here.
def product_list(request):
    list_products = Product.objects.all()
    return render(request, 'dashboard/products.html', {'list_products': list_products})