# -*- coding: utf-8 -*-
#Importamos modulos necesarios standars
import datetime
from django.template import RequestContext
from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse

#traemos los modulos propios necesarios
from .models import Thread, Subforo, Post
from .forms import ThreadForm, PostForm
#Definimos todo el conjunto de vistas de threads
def foro(request):
	subforos = Subforo.objects.all()
	threads = Thread.objects.all()
	return render(request, 'foro.html', {'subforos': subforos, 'threads' : threads })

def subforo(request, subforo_id):
	threads = Thread.objects.filter(subforo=subforo_id)
	return render(request, 'subforo.html', {'threads' : threads})

def thread(request, thread_id):
	if request.method == 'POST':
		form = PostForm(request.POST)
		if form.is_valid():
			post = Post()
			post.thread = Thread.objects.get(pk=thread_id)
			post.autor = request.user
			post.body = form.cleaned_data['body']
			post.save()
	form = PostForm()
	thread = Thread.objects.get(pk=thread_id)
	posts = Post.objects.filter(thread=thread_id)
	return render(request, 'thread.html', {'thread' : thread, 'posts' : posts, 'form' : form})

def newthread(request):
	if request.method == 'POST':
		form = ThreadForm(request.POST)
		if form.is_valid():
			nt = Thread()
			nt.subforo = form.cleaned_data['subforo']
			nt.autor = request.user
			nt.nombre = form.cleaned_data['nombre']
			nt.body = form.cleaned_data['body']
			nt.save()
			return HttpResponseRedirect('/foro/thread/'+str(nt.id))
	else:
		form = ThreadForm()
		return render(request, 'newthread.html', {'form' : form, })