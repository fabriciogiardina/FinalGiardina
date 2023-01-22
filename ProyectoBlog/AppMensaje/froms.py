from django import forms

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Mensaje


class MensajeForm (forms.ModelForm):
    class Meta:
        model = Mensaje
        fields = ['recibe','cuerpo']   




