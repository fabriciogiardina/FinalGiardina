
from django.urls import path
from .views import *
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path("", inicio, name= "inicio"),
    path("registro/", registro, name="registro"),
    path('login/', login_request, name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("perfil/", leerPerfil, name="perfil"),
    path("editarPerfil/", editarPerfil, name="editarPerfil"),
    path("agregarAvatar/", agregarAvatar, name="agregarAvatar"),
    path("acercaDeMi/", acercaDeMi, name="acercaDeMi"),
    path("agregarPost/", agregarPost, name="agregarPost"),
    path("listaPosteos/", listaPosteos, name="listaPosteos"),
    path("verPosteo/<id>", verPosteo, name="verPosteo"),
    path("eliminarPosteo/<id>", eliminarPosteo, name= "eliminarPosteo"),
    path("editarPosteo/<id>", editarPosteo, name= "editarPosteo"),
]