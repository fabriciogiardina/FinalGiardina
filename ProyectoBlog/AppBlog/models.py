from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.

class Avatar (models.Model):
    imagen= models.ImageField (upload_to="avatars")
    user= models.ForeignKey (User, on_delete=models.CASCADE)

class Posteo (models.Model):
    titulo = models.CharField (max_length= 50)
    subtitulo = models.CharField (max_length= 50)
    cuerpo = RichTextField(blank=True, null=True)
    fecha = models.DateField()
    autor = models.ForeignKey (User, on_delete=models.CASCADE)
    imagen = models.ImageField (upload_to="imagenes", blank=True)