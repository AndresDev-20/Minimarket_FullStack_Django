from django.shortcuts import render, redirect
from .models import Customer
from .forms import CustomerForm 

# Create your views here.
def customer(request):
    customers = Customer.objects.all()
    return render(request, 'customers.html', {'customers': customers})

def Customer_create(request):
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('customer')
    else:
        form = CustomerForm()
    return render(request, 'create.html', {'form': form})