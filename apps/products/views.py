from django.shortcuts import render, HttpResponse, redirect
from .models import Category, Product
from .forms import ProductForm, CategoryForm

# Create your views here.

# Products
# List all products
def product_list(request):
    list_products = Product.objects.all()
    list_categories = Category.objects.all()
    return render(request, 'product/products.html', {'list_products': list_products, 'list_categories': list_categories})

# Filter products by category
def product_filter(request):
    category_id = request.GET.get('category')
    list_categories = Category.objects.all()
    if category_id:
        list_products = Product.objects.filter(category_id=category_id)
    else:
        list_products = Product.objects.all()
    return render(request, 'product/products.html', {'list_products': list_products, 'list_categories': list_categories, 'selected_category': int(category_id) if category_id else None})

# Create a new product
def product_create(request):
    form = ProductForm()
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('products')
    return render(request, 'product/create.html', {'form': form})

# Edit an existing product
def product_edit(request, product_id):
    product = Product.objects.get(id=product_id)
    form = ProductForm(instance=product)
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('products')
    return render(request, 'product/edit.html', {'form': form, 'product': product})

# Delete an existing product
def product_delete(request, product_id):
    product = Product.objects.get(id=product_id)
    if request.method == 'POST':
        product.delete()
        return redirect('products')
    return HttpResponse(status=405)





# Categories
# List all categories
def category_list(request):
    list_categories = Category.objects.all()
    return render(request, 'category/categories.html', {'list_categories': list_categories})

# Create a new category
def category_create(request):
    form = CategoryForm()
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('category')
    return render(request, 'category/create.html', {'form': form})

# Edit an existing category
def category_edit(request, category_id):
    category = Category.objects.get(id=category_id)
    form = CategoryForm(instance=category)
    if request.method == 'POST':
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            return redirect('category')
    return render(request, 'category/edit.html', {'form': form, 'category': category})

# Delete an existing category
def category_delete(request, category_id):
    category = Category.objects.get(id=category_id)
    if request.method == 'POST':
        category.delete()
        return redirect('category')
    return HttpResponse(status=405)