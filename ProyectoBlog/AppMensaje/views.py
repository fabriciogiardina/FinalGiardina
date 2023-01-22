from django.shortcuts import render
from .models import Mensaje
from .froms import MensajeForm
from django.contrib.auth.models import User
import datetime

from AppBlog.views import obtenerAvatar
# Create your views here.


def enviarMensaje (request):
    if request.method=="POST":
        form= MensajeForm(request.POST)
        if form.is_valid():
            info=form.cleaned_data
            envia = request.user
            recibe = info ["recibe"]
            cuerpo = info ["cuerpo"]
            fecha = datetime.datetime.now()
            mensaje = Mensaje (envia=envia, recibe=recibe, cuerpo=cuerpo, fecha=fecha)
            mensaje.save()
            mensaje= Mensaje.objects.all ()
            return render (request, "AppMensaje/mensajes.html", {"mensaje": mensaje, "mensaje": "Enviaste mensaje correctamente", "avatar": obtenerAvatar (request)})
        else:
            return render (request, "AppBlog/agregarPost.html", {"form": form, "mensaje": "informacion no valida", "avatar": obtenerAvatar (request)})
    else:
        form=MensajeForm()
        return render (request, "AppMensaje/enviarMensaje.html", {"form": form, "avatar": obtenerAvatar (request)})


def mensajes (request):
    mensajes = Mensaje.objects.filter(recibe = request.user)
    return render (request, "AppMensaje/mensajes.html", {"mensajes": mensajes, "avatar": obtenerAvatar (request)})
