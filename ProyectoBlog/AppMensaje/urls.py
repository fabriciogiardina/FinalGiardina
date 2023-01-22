from django.urls import path
from .views import *


urlpatterns = [
  
    path("enviarMensaje", enviarMensaje, name="enviarMensaje"),
    path("mensajes", mensajes, name="mensajes")

]