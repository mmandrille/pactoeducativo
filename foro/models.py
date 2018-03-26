# -*- coding: utf-8 -*-
#Importamos modulos standars
import datetime
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class subforos(models.Model):
	nombre = models.CharField(max_length=50, unique=True)
	descripcion = models.CharField(max_length=200)
	activo = models.BooleanField(default=True)
	def __unicode__(self):
		return self.nombre		

class threads(models.Model):
	subforo = models.ForeignKey(subforos, on_delete=models.CASCADE)
	autor = models.ForeignKey(User, on_delete=models.CASCADE)
	fecha_creacion = models.DateField(default=datetime.date.today)
	titulo = models.CharField(max_length=50, unique=True)
	resumen = models.CharField(max_length=200)
	body = models.CharField(max_length=500)
	def __str__(self):
		return self.titulo + ": " + self.resumen + " -Autor: " + self.autor.username + ". (Puntaje: "+str(self.puntaje) + ")"
	def link(self):
		return ("/foro/ver" + str(self.id))

class posts(models.Model):
	thread= models.ForeignKey(threads, on_delete=models.CASCADE)
	autor= models.ForeignKey(User, on_delete=models.CASCADE)
	body= models.CharField(max_length=200)
	fecha_creacion= models.DateField(default=datetime.date.today)
	def __str__(self):
		return self.autor.username + " comento: " + self.body + "| al contenido: " + self.thread.titulo + "| " + str(self.fecha_creacion) + ". (Puntaje: "+str(self.puntaje)+")"
	def link(self):
		return ("/foro/ver" + str(self.thread.id))