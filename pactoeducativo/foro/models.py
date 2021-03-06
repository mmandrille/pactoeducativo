#Importamos modulos standars
import datetime
from django.db import models
from django.contrib.auth.models import User
from tinymce.models import HTMLField

# Create your models here.
class Subforo(models.Model):
	nombre = models.CharField(max_length=50, unique=True)
	descripcion = models.CharField(max_length=200)
	icono = models.FileField(upload_to='icono')
	activo = models.BooleanField(default=True)
	def __str__(self):
		return self.nombre		

class Thread(models.Model):
	subforo = models.ForeignKey(Subforo, on_delete=models.CASCADE)
	autor = models.ForeignKey(User, on_delete=models.CASCADE)
	fecha_creacion = models.DateField(default=datetime.date.today)
	nombre = models.CharField(max_length=50, unique=True)
	body = HTMLField()
	def __str__(self):
		return self.nombre + ": " + " -Autor: " + self.autor.username + ")"
	def link(self):
		return ("/foro/ver/" + str(self.id))

class Post(models.Model):
	thread = models.ForeignKey(Thread, on_delete=models.CASCADE)
	autor = models.ForeignKey(User, on_delete=models.CASCADE)
	body = models.CharField(max_length=200)
	fecha_creacion = models.DateField(default=datetime.date.today)
	def __str__(self):
		return self.autor.username + " comento: " + self.body + "| al contenido: " + self.thread.nombre + "| " + str(self.fecha_creacion) + ")"