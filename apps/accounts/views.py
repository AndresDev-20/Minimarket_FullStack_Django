from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

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
    return render(request, 'dashboard.html')



def logout_view(request):
    logout(request)
    return redirect('login')