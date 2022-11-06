from django import forms
from validator.validators import Validators
from django.core.exceptions import MultipleObjectsReturned, ValidationError
from django.contrib.auth.forms import AuthenticationForm


class LoginForm(AuthenticationForm):
    remember_me = forms.BooleanField(required=False)  # and add the remember_me field

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update(
                {
                    'class': 'form-control',
                }
            )
        self.fields['username'].required = False
        self.fields['password'].required = False
        self.fields['remember_me'].widget.attrs.update(
            {
                'class': 'form-check-input',
            }
        )


    def clean_username(self):
        email = self.cleaned_data.get('username')
        validator = Validators(email)
        if validator.validateEmail():
            raise validator.messageAlert(f'El correo electrónico {email} no es valido')
        return email

    def clean_password(self):
        password = self.cleaned_data.get('password')
        validator = Validators(password)
        if validator.validatePassword():
            raise validator.messageAlert(f'La contraseña ingresada no es valida')
        return password