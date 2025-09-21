from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from apps.sales.models import Sale, SalesDetail
from datetime import date

# Create your views here.
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            if user.is_staff:
                login(request, user)
                return redirect('dashboard')
            else:
                return render(request, 'login.html', {'error': 'No tienes permisos de administrador.'})
        else:
            return render(request, 'login.html', {'error': 'Credenciales inválidas.'})
    return render(request, 'login.html')



@login_required
def dashboard_view(request):
    today = date.today()
    sales_list = len(Sale.objects.filter(date__date=today))
    sales_list_mont = len(Sale.objects.filter(date__month=today.month, date__year=today.year))
    sale_detail_earnings = SalesDetail.objects.all()
    total_earnings = sum(detail.profit for detail in sale_detail_earnings)
    total_earnings_formatted = "{:,.2f}".format(total_earnings).replace(",", "X").replace(".", ",").replace("X", ".")
    return render(request, 'dashboard.html', {"day": sales_list, "month": sales_list_mont, "total_earnings_formatted": total_earnings_formatted, "total_earnings": total_earnings})



def logout_view(request):
    logout(request)
    return redirect('login')