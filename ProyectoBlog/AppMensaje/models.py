from django.db import models
from django.contrib.auth.models import User
import datetime

# Create your models here.

class Mensaje (models.Model):
    envia = models.ForeignKey (User, related_name="envia", on_delete=models.CASCADE)
    recibe = models.ForeignKey (User, related_name="recibe", on_delete=models.CASCADE)
    cuerpo = models.TextField (max_length=255)
    fecha = models.DateField ()
    