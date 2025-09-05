from django.shortcuts import render

# Create your views here.
def sales(request):
    return render(request, 'sale/sales.html')
