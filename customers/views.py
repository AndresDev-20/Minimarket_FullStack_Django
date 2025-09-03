from django.shortcuts import render
from .models import Customer

# Create your views here.
def customer(request):
    customers = Customer.objects.all()
    return render(request, 'dashboard/customers.html', {'customers': customers})