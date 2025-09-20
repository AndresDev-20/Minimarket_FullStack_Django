from django.shortcuts import render, redirect
from .models import Supplier
from .forms import SupplierForm

# Create your views here.
def supplier(request):
    list_suppliers = Supplier.objects.all()
    return render(request, 'supplier/suppliers.html', {'list_suppliers': list_suppliers})

# Create Supplier
def create_supplier(request):
    if request.method == 'POST':
        form = SupplierForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('supplier')
    else:
        form = SupplierForm()
    return render(request, 'supplier/create.html', {'form': form})

# Edit Supplier
def edit_supplier(request, supplier_id):
    supplier = Supplier.objects.get(id=supplier_id)
    if request.method == 'POST':
        form = SupplierForm(request.POST, instance=supplier)
        if form.is_valid():
            form.save()
            return redirect('supplier')
    else:
        form = SupplierForm(instance=supplier)
    return render(request, 'supplier/edit.html', {'form': form, 'supplier': supplier})


# Delete Supplier
def delete_supplier(request, supplier_id):
    supplier = Supplier.objects.get(id=supplier_id)
    if request.method == 'POST':
        supplier.delete()
        return redirect('supplier')
    return render(request, 'supplier/delete.html', {'supplier': supplier})