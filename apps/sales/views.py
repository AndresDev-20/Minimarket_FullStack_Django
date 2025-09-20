from django.shortcuts import redirect, render
from .models import Sale, SalesDetail
from .forms import SaleForm, SalesDetailForm

# Create your views here.
def sales(request):
    sales_list = Sale.objects.all()
    return render(request, 'sale/sales.html', {'sales': sales_list})

# Create Sale
def create_sale(request):
    form = SaleForm()
    if request.method == 'POST':
        form = SaleForm(request.POST)
        if form.is_valid():
            sale = form.save()
            return redirect('detail_sale', pk=sale.id)
        else:
            print(form.errors)  
    return render(request, 'sale/create.html', {'form': form})



## salesdetail
# list detail sale
def detail_sale(request, pk):
    detail_sale = SalesDetail.objects.filter(sale_id=pk)
    sale = Sale.objects.get(id=pk)
    return render(request, 'detailsale/detailsale.html', {'sale': sale, 'detail_sales': detail_sale})

# Create detail sale
def create_detail_sale(request, pk):
    form = SalesDetailForm(initial={'sale': pk})
    if request.method == 'POST':
        form = SalesDetailForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            form.save()
            # Recalculate total sale
            sale = Sale.objects.get(id=pk)
            sale.calculate_total()
            return redirect('detail_sale', pk=pk)
        else:
            print(form.errors)  
    return render(request, 'detailsale/create.html', {'form': form, 'sale_id': pk})