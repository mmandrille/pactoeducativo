# -*- coding: utf-8 -*-
#Importamos modulos necesarios standars
import datetime
from django.template import RequestContext
from django.shortcuts import render

#traemos los modulos propios necesarios
from .models import Thread, Subforo, Post

#Definimos todo el conjunto de vistas de threads
def foro(request):
	subforos = Subforo.objects.all()
	threads = Thread.objects.all()
	return render(request, 'foro.html', {'subforos': subforos, 'threads' : threads })

def subforo(request, subforo_id):
	return render(request, 'subforo.html',)

def thread(request, thread_id):
	return render(request, 'thread.html',)