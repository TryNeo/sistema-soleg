import re

from django.core.exceptions import ValidationError

class Validators(object):
    def __init__(self, value):
        self.value = value
        self.REGEX_STRING = '^[a-zA-ZáéíóñÁÉÍÓÚÑ \-]+$'
        self.REGEX_INTEGER = '^[0-9]+$'
        self.REGEX_EMAIL = '^([a-z0-9_\.-]+)@([\da-z\.-]+)\.([a-z\.]{2,6})$'
        self.REGEX_NAME = "^([a-zA-Z]{2,}\s[a-zA-Z]{1,}'?-?[a-zA-Z]{2,}\s?([a-zA-Z]{1,})?)"

    def validateStringLength(self,minLength : int):
        if len(self.value) >= minLength:
            return False
        return True
    
    def validateString(self):
        if re.search(self.REGEX_STRING,self.value):
            return False
        return True

    def validateEmptyField(self):
        if len(str(self.value)) >= 2:
            return False
        return True
    
    def validateNumber(self):
        if re.search(self.REGEX_INTEGER,self.value):
            return False
        return True
    
    def validateExists(self,message  : str,instance,filter):
        filter = filter
        if not instance.pk:
            return ValidationError(
                (message),
                params={'value': self.value},
                )
        if instance.pk != filter.pk:
            return ValidationError(
                ('No puedes actualizar el registro, ya existe '+self.value),
                params={'value': self.value},
                )
        return False

    def validateEmail(self):
        if re.search(self.REGEX_EMAIL,self.value):
            return False
        return True
    
    def validateName(self):
        if re.search(self.REGEX_EMAIL,self.value):
            return False
        return True


    def messageAlert(self,message  : str):
        return ValidationError(
                (message),
                params={'value': self.value},
            )