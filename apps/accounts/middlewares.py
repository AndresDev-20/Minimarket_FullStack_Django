from django.shortcuts import redirect
from django.urls import reverse

class LoginRequiredMiddleware:
    """
    Middleware que obliga a que el usuario esté autenticado
    para acceder a cualquier ruta excepto las públicas.
    """

    def __init__(self, get_response):
        self.get_response = get_response
        self.public_paths = [
            reverse('login'),
            reverse('logout'),
            reverse('admin:index'),
        ]

    def __call__(self, request):
        # Si la URL actual no está en las públicas y el usuario no está autenticado
        if not request.user.is_authenticated and request.path not in self.public_paths:
            return redirect('login')

        response = self.get_response(request)
        return response
