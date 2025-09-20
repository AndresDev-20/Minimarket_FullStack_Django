from django.shortcuts import render, redirect
from .models import Customer
from .forms import CustomerForm 
from apps.sales.models import Sale, SalesDetail

# Create your views here.
def customer(request):
    customers = Customer.objects.all()
    return render(request, 'customers.html', {'customers': customers})

# filter for customer by cc
def customer_filter(request):
    cc = request.GET.get('cc')
    if cc:
        customers = Customer.objects.filter(cc__icontains=cc)
    else:
        customers = Customer.objects.all()
    return render(request, 'customers.html', {'customers': customers, 'search_cc': cc})

# create customer
def Customer_create(request):
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('customer')
    else:
        form = CustomerForm()
    return render(request, 'create.html', {'form': form})

# edit customer
def Customer_edit(request, pk):
    customer = Customer.objects.get(id=pk)
    if request.method == 'POST':
        form = CustomerForm(request.POST, instance=customer)
        if form.is_valid():
            form.save()
            return redirect('customer')
    else:
        form = CustomerForm(instance=customer)
    return render(request, 'edit.html', {'form': form})

# delete customer
def Customer_delete(request, pk):
    customer = Customer.objects.get(id=pk)
    if request.method == 'POST':
        customer.delete()
        return redirect('customer')
    return render(request, 'delete.html', {'customer': customer})


# view customer purchases
def customer_purchases(request, pk):
    customer = Customer.objects.get(id=pk)
    sales = Sale.objects.filter(customer=customer)
    return render(request, 'purchases.html', {'customer': customer, 'sales': sales})

def customer_detail_sale(request, pk):
    sale = Sale.objects.get(id=pk)
    print(sale)
    detail_sales = SalesDetail.objects.filter(sale=sale)
    return render(request, 'customer_detail.html', {'customer': sale.customer, 'detail_sales': detail_sales})