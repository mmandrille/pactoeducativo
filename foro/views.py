# -*- coding: utf-8 -*-
#Importamos modulos necesarios standars
import datetime
from django.template import RequestContext
from django.shortcuts import render

#traemos los modulos propios necesarios
from .models import Thread, Subforo, Post

#Definimos todo el conjunto de vistas de threads
def Vindex(request):
	subforos = Subforo.objects.all()
	threads = Thread.objects.all()
	return render(request, 'foro.html', {'subforos': subforos, 'threads' : threads })