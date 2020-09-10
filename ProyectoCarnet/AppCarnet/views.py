from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, Http404
from .forms import forms, CreateUserForm
from .models import *

# Create your views here.
def registerPage(request):
    if(request.user.is_authenticated):
        return redirect('index')
    else:
        form = CreateUserForm()
        if(request.method == 'POST'):
            form = CreateUserForm(request.POST)
            if(form.is_valid()):
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, "Cuenta "+user+" creada satisfatoriamente.")
                return redirect('login')

        context = {'form': form}
        return render(request, 'register.html', context)

def loginPage(request):
    if(request.user.is_authenticated):
        return redirect('index')
    else:
        if(request.method == 'POST'):
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password) #name q esta en el html
            if(user is not None):
                login(request, user)     
                return redirect('index')
            else:
                messages.info(request, "Nombre de usuario o contraseña incorrecto.")

        context = {}
        return render(request, 'login.html', context)

def logoutUser(request):
    logout(request)
    return redirect('login')

def index(request):
    
    return render(request,'index.html')