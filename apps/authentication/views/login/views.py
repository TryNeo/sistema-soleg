from django.contrib.auth import login, logout
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import redirect
from django.views.generic import RedirectView

class LoginFormView(LoginView):
    template_name = 'login.html'
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('/')
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Iniciar Sesión'
        return context