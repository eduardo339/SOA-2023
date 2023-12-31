from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
from tasks.models import Tarea
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

# Create your views here.
def home(request):
    return render(request, "home.html")


def signup(request):
    if request.method == "GET":
        print("Enviando formulario")
        return render(request, "signup.html", {"form": UserCreationForm})
    else:
        if request.POST["password1"] == request.POST["password2"]:
            # register user
            try:
                user = User.objects.create_user(
                    username=request.POST["username"],
                    password=request.POST["password1"],
                    is_superuser=request.POST["admin"],
                )
                user.save()
                
                return redirect("home")
                # return HttpResponse("Usuario creado con exito")
            except IntegrityError:
                return render(
                    request,
                    "signup.html",
                    {"form": UserCreationForm, "error": "El usuario ya existe"},
                )

        return render(
            request,
            "signup.html",
            {"form": UserCreationForm, "error": "Las contraseñas no coinciden"},
        )
        print(request.POST)
        print("Obteniendo datos")


class tasks(ListView):
    
    model=Tarea

class crearTarea(CreateView):
    model=Tarea
    fields=['tid', 'tname', 'tdesc', 'euser']
    success_url = reverse_lazy('tasks')

class editarTarea(UpdateView):
    model=Tarea
    fields=['tid', 'tname', 'tdesc', 'euser']
    success_url = reverse_lazy('tasks')

class borrarTarea(DeleteView):
    model=Tarea
    success_url = reverse_lazy('tasks')

    

def signout(request):
    logout(request)
    return redirect("home")


def signin(request):
    if request.method == "GET":
        return render(request, "signin.html", {"form": AuthenticationForm})
    else:
        user= authenticate(
            request,
            username=request.POST["username"],
            password=request.POST["password"],
        )
        if user is None:
            return render(request, "signin.html", {
                "form": AuthenticationForm,
                'error': 'El usuario o contraseña son incorrectos'
                })
        else: 
            login(request, user)
            return redirect('home')
        

def newTask(request):
    return render(request, "newTask.html")   

def editTask(request):
    return render(request, "editTask.html") 
