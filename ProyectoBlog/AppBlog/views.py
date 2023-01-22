from django.shortcuts import render
from .models import Avatar, Posteo
from django.http import HttpResponse

from AppBlog.forms import RegistroUsuarioForm, UserEditForm, AvatarForm, PostForm
from django.urls import reverse_lazy

from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, authenticate

from django.contrib.auth.decorators import login_required

import datetime


# Create your views here.

def inicio (request):
    return render (request, "AppBlog/inicio.html")


def registro (request):
    if request.method == "POST":
        form= RegistroUsuarioForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get ("username")
            form.save()
            return render (request, "AppBlog/inicio.html", {"mensaje": f"usuario {username} creado correctamente"})
        else:
            return render (request, "AppBlog/registro.html", {"form": form})
    else:
        form= RegistroUsuarioForm()
        return render (request, "AppBlog/registro.html", {"form": form, "mensaje": "Error al crear usuario"})



def login_request (request):
    if request.method == "POST":
        form=AuthenticationForm (request, data=request.POST)
        if form.is_valid ():
            info= form.cleaned_data
            usu= info["username"]
            clave= info ["password"]
            usuario= authenticate (username = usu, password = clave)
            if usuario is not None:
                login (request, usuario)
                return render (request, "AppBlog/inicio.html", {"mensaje": f"usuario {usu} logueado correctamente"})
            else:
                return render (request, "AppBlog/login.html", {"form": form, "mensaje": "usuario o contraseÃ±a incorrecto"})
        else:
            return render (request, "AppBlog/login.html", {"form": form, "mensaje": "usuario o contraseÃ±a incorrecto"})
    else:
        form = AuthenticationForm()
        return render (request, "AppBlog/login.html", {"form": form})


def leerPerfil (request):
    usuario = request.user
    return render (request, "AppBlog/perfil.html", {"usuario": usuario, "avatar": obtenerAvatar(request)})


def obtenerAvatar (request):
    lista= Avatar.objects.filter (user= request.user)
    if len (lista)!= 0:
        avatar= lista[0].imagen.url
    else:
        avatar= "/media/avatars/images.jpg"
    return avatar

def editarPerfil (request):
    usuario= request.user
    if request.method == "POST":
        form= UserEditForm (request.POST)
        if form.is_valid ():
            info = form.cleaned_data
            usuario.email = info["email"]
            usuario.password1 = info["password1"]
            usuario.password2 = info["password2"]
            usuario.first_name = info["first_name"]
            usuario.last_name = info["last_name"]
            usuario.save ()
            return render (request, "AppBlog/inicio.html", {"mensaje":f"usuario {usuario.username} editado correctamente", "avatar": obtenerAvatar(request)})
        else:
            return render (request, "AppBlog/editarPerfil.html", {"form": form, "nombreusuario": usuario.username, "avatar": obtenerAvatar(request)})
    else:
        
        form = UserEditForm (instance = usuario)
        return render (request, "AppBlog/editarPerfil.html", {"form": form, "nombreusuario": usuario.username, "avatar": obtenerAvatar(request)} )


def agregarAvatar(request):
    if request.method == "POST":
        form=AvatarForm(request.POST, request.FILES)
        if form.is_valid():
            avatar=Avatar(user=request.user, imagen=request.FILES["imagen"])
            avatarViejo = Avatar.objects.filter(user = request.user)
            if len(avatarViejo) > 0:
                avatarViejo[0].delete()
            avatar.save()
            return render (request, "AppBlog/inicio.html", {"mensaje":f"Avatar agregado correctamente"})
        else:
           return render (request, "AppBlog/agregarAvatar.html", {"form":form, "usuario": request.user, "mensaje": "Error al agregar avatar"}) 
    else:
        form=AvatarForm()
        return render (request, "AppBlog/agregarAvatar.html", {"form":form, "usuario": request.user})


def acercaDeMi (request):
    return render (request, "AppBlog/acercaDeMi.html", {"avatar": obtenerAvatar(request)})


def agregarPost (request):
    if request.method=="POST":
        form= PostForm(request.POST, request.FILES)
        if form.is_valid():
            info=form.cleaned_data
            titulo = info ["titulo"]
            subtitulo = info ["subtitulo"]
            cuerpo = info ["cuerpo"]
            imagen = request.FILES["imagen"]
            fecha = datetime.datetime.now()
            autor = request.user
            posteo = Posteo (titulo=titulo, subtitulo=subtitulo, cuerpo=cuerpo, fecha=fecha, autor = autor, imagen = imagen)
            posteo.save()
            posteos= Posteo.objects.all ()
            return render (request, "AppBlog/listaPosteos.html", {"posteos": posteos, "mensaje": "Creaste un nuevo post", "avatar": obtenerAvatar (request)})
        else:
            return render (request, "AppBlog/agregarPost.html", {"form": form, "mensaje": "informacion no valida", "avatar": obtenerAvatar (request)})
    else:
        form=PostForm()
        return render (request, "AppBlog/agregarPost.html", {"form": form, "avatar": obtenerAvatar (request)})

def listaPosteos (request):
    p = Posteo.objects.all()
    return render (request, "AppBlog/listaPosteos.html", {"p": p, "avatar": obtenerAvatar (request)})

def verPosteo (request, id):
    posteo = Posteo.objects.get(id=id)
    return render (request, "AppBlog/verPosteo.html", {"posteo": posteo})


def eliminarPosteo (request, id):
    post = Posteo.objects.get(id=id)
    post.delete()
    posteos = Posteo.objects.all()
    return render (request, "AppBlog/listaPosteos.html", {"posteos": posteos, "mensaje": "El posteo fue borrado correctamente"})


def editarPosteo (request, id):
    post=Posteo.objects.get(id=id)
    if request.method =="POST":
        form=PostForm(request.POST, request.FILES)
        if form.is_valid():
            info=form.cleaned_data
            post.titulo=info["titulo"]
            post.subtitulo=info["subtitulo"]
            post.cuerpo=info["cuerpo"]
            post.imagen=info ["imagen"]
            post.save()
            posteos=Posteo.objects.all()
            return render (request, "AppBlog/listaPosteos.html", {"posteos":posteos, "mensaje": "Posteo editado Correctamente"})
        pass
    else:
        formulario=PostForm(initial={"titulo": post.titulo, "subtitulo": post.subtitulo, "cuerpo": post.cuerpo, "imagen": post.imagen})
        return render (request, "AppBlog/editarPosteo.html", {"form": formulario, "post": post})