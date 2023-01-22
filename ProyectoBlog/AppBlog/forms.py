from django import forms

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Posteo
from ckeditor_uploader.fields import RichTextUploadingField
from ckeditor.fields import RichTextField


class RegistroUsuarioForm (UserCreationForm):
    email=forms.EmailField (label="Email")
    password1=forms.CharField (label="Contraseña", widget=forms.PasswordInput)
    password2=forms.CharField (label="Confirmar Contraseña", widget=forms.PasswordInput)
    first_name=forms.CharField (label="Nombre")
    last_name=forms.CharField (label="Apellido")

    class Meta:
        model=User
        fields= ["username", "email", "password1", "password2", "first_name", "last_name"]
        help_texts = {k:"" for k in fields}


class UserEditForm (UserCreationForm):
    email=forms.EmailField (label="Email Usuario")
    password1=forms.CharField (label="Contraseña", widget=forms.PasswordInput)
    password2=forms.CharField (label="Confirmar Contraseña", widget=forms.PasswordInput)
    first_name=forms.CharField (label="modificar Nombre")
    last_name=forms.CharField (label="modificar Apellido")
    

    class Meta:
        model=User
        fields= ["email", "password1", "password2", "first_name", "last_name"]
        help_texts = {k:"" for k in fields}

class AvatarForm (forms.Form):
    imagen= forms.ImageField (label= "imagen")


class PostForm (forms.ModelForm):
    class Meta:
        model = Posteo
        fields = ['titulo','subtitulo','cuerpo','imagen']    
    