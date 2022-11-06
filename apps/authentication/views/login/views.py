from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import redirect
from django.http import JsonResponse
from apps.authentication.forms.login.form_login import *
from django.views.generic import RedirectView
from soleg.secretkeys import *

class LoginFormView(LoginView):
    form_class = LoginForm
    template_name = 'login/login.html'

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('/')
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        if request.headers.get('x-requested-with') == 'XMLHttpRequest':
            form = self.form_class(data=request.POST)
            if self.login_recaptcha(request):
                if form.is_valid():
                    self.form_valid(form=form)
                    if not form.cleaned_data['remember_me']:
                        request.session.set_expiry(0) 
                        request.session.modified = True
                    data['message'] = 'Bienvenido'
                    return self.response_codes(data,200)
                else:
                    data['message'] = form.errors
                    return self.response_codes(data,400)
            else:
                data['message'] = {
                    'g-recaptcha-response':['El reCAPTCHA no es valido, por favor intente de nuevo o refresque la pagina.']
                }
                return self.response_codes(data,498)
        else:
            return redirect(self.success_url)

    
    def login_recaptcha(self, request):
        recaptcha_response = request.POST.get('g-recaptcha-response')
        url = 'https://www.google.com/recaptcha/api/siteverify'
        values = {
                'secret': RECAPTCHA_SECRET_KEY,
                'response': recaptcha_response,
                }
        datas = urllib.parse.urlencode(values).encode()
        req =  urllib.request.Request(url, data=datas)
        response = urllib.request.urlopen(req)
        result = json.loads(response.read().decode())
        if not result['success']:
            return False
        return True

    def response_codes(self,data,code):
        response = JsonResponse(data)
        response.status_code = code
        return response

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Iniciar Sesión'
        context['creador'] = 'Josue Lopez'
        return context