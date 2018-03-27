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
	threads = Thread.objects.filter(subforo=subforo_id)
	return render(request, 'subforo.html', {'threads' : threads})

def thread(request, thread_id):
	thread = Thread.objects.get(pk=thread_id)
	posts = Post.objects.filter(thread=thread_id)
	return render(request, 'thread.html', {'thread' : thread, 'posts' : posts})

def newthread(request):
	return render(request, 'newthread.html',)