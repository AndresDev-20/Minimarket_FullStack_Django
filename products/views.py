from django.shortcuts import render
from .models import Category, Product
from .forms import ProductForm, CategoryForm

# Create your views here.
# Products
def product_list(request):
    list_products = Product.objects.all()
    return render(request, 'dashboard/products.html', {'list_products': list_products})

def product_create(request):
    form = ProductForm()
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'dashboard/products.html', {'list_products': Product.objects.all()})
    return render(request, 'dashboard/gestion/product_create.html', {'form': form})




# Categories
def category_list(request):
    list_categories = Category.objects.all()
    return render(request, 'dashboard/categories.html', {'list_categories': list_categories})

def category_create(request):
    form = CategoryForm()
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'dashboard/categories.html', {'list_categories': Category.objects.all()})
    return render(request, 'dashboard/gestion/category_create.html', {'form': form})