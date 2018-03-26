# -*- coding: utf-8 -*-
#Importamos modulos necesarios standars
import datetime
from django.template import RequestContext
from django.shortcuts import render_to_response, redirect

#traemos los modulos propios necesarios
from .models import threads, subforos, posts

#Definimos todo el conjunto de vistas de threads
def Vindex(request):
	return render_to_response('foro.html')