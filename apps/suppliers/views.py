from django.shortcuts import render
from .models import Supplier

# Create your views here.
def supplier(request):
    list_suppliers = Supplier.objects.all()
    return render(request, 'supplier/suppliers.html', {'list_suppliers': list_suppliers})
