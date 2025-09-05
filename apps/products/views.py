from django.shortcuts import render
from .models import Category, Product
from .forms import ProductForm, CategoryForm

# Create your views here.
# Products
def product_list(request):
    list_products = Product.objects.all()
    return render(request, 'product/products.html', {'list_products': list_products})

def product_create(request):
    form = ProductForm()
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'product/products.html', {'list_products': Product.objects.all()})
    return render(request, 'product/create.html', {'form': form})




# Categories
def category_list(request):
    list_categories = Category.objects.all()
    return render(request, 'category/categories.html', {'list_categories': list_categories})

def category_create(request):
    form = CategoryForm()
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'category/categories.html', {'list_categories': Category.objects.all()})
    return render(request, 'category/create.html', {'form': form})