from django.urls import path
from .views.login.views import *

urlpatterns = [
    path('login/',LoginFormView.as_view(),name='login'),
]