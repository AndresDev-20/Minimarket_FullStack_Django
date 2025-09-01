from django.shortcuts import render

def index(request):
    data = request.POST
    if request.method == "POST":
        username = data.get("username")
        password = data.get("password")
        # Aquí puedes agregar la lógica para autenticar al usuario
        if username == "Andres.dev" and password == "1234":
            return render(request, 'dashboard/dashboard.html', {})
        else:
            return render(request, 'index.html', {})
    return render(request, 'index.html', {})