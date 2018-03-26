from django.http import Http404
from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
#Import Personales
from .models import Archivo, Album, Foto
from .forms import BuscarForm

#@login_required
def home(request):
    return render(request, 'home.html', { })

def faq(request):
    return render(request, 'faq.html', { })

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})

def archivo(request, archivo_id):
    archivo = Archivo.objects.get(pk=archivo_id)
    return render(request, 'mostrar_archivo.html', { 'archivo' : archivo })

def biblioteca(request):
    if request.method == 'POST':
        form = BuscarForm(request.POST)
        if form.is_valid():
            archivos = Archivo.objects.filter(nombre__icontains=form.cleaned_data['texto'])
    else:
        archivos = Archivo.objects.all()
    form = BuscarForm()
    return render(request, 'biblioteca.html', {'archivos' : archivos, 'form': form })

def noticias(request):
    return render(request, 'noticias.html', { })

def encontrate(request):
    return render(request, 'encontrate.html', { })