from django.contrib.auth import login, logout
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import redirect, render
from django.http import JsonResponse
from django.urls import reverse_lazy
from apps.authentication.forms.login.form_login import *
from django.views.generic import RedirectView
from django.contrib.auth.mixins import LoginRequiredMixin



class LoginFormView(LoginView):
    form_class = LoginForm
    template_name = 'login/login.html'

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('/admin')
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        if request.headers.get('x-requested-with') == 'XMLHttpRequest':
            form = self.form_class(data=request.POST)
            if form.is_valid():
                self.form_valid(form=form)
                data['status'] = 1
                data['url'] = 'admin/'
                data['message'] = 'Bienvenido'
                response = JsonResponse(data)
                response.status_code = 200
                return response
            else:
                data['status'] = 0
                data['message'] = form.errors
                response = JsonResponse(data)
                response.status_code = 400
                return response
        else:
            return redirect(self.success_url)


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Iniciar Sesión'
        return context