from django.http import Http404
from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
#Agregamos modulos personales
from .models import Faq
from .models import Texto

def home(request):
    return render(request, 'home.html', { })

def faq(request):
    textos = Texto.objects.all()
    faqs = Faq.objects.all()
    return render(request, 'faq.html', {'textos' : textos, 'faqs' : faqs })

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

def encontrate(request):
    return render(request, 'encontrate.html', { })