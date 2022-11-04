from django import forms
from validator.validators import Validators
from django.core.exceptions import MultipleObjectsReturned, ValidationError
from django.contrib.auth.forms import AuthenticationForm


class LoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update(
                {
                    'class': 'form-control',
                }
            )

    def clean_username(self):
        username = self.cleaned_data.get('username')
        validator = Validators(username)
        if validator.validateString():
                raise validator.messageAlert('El nombre contiene numeros')
        return username