from __future__ import unicode_literals
import datetime

from django.db import models
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.models import *
from django.contrib.auth.models import User
from pactoeducativo.settings import MEDIA_URL
from django.utils import timezone

# Create your models here.
class Album(models.Model):
    nombre = models.CharField('Titulo', max_length=200)
    descripcion = models.TextField()
    portada = models.FileField(upload_to='fotos/')
    pub_date = models.DateTimeField('Fecha de Publicacion', default=timezone.now)
    def __str__(self):
        return self.nombre

class Foto(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    foto = models.FileField(upload_to='fotos/')
    pub_date = models.DateTimeField('Fecha de Publicacion', default=timezone.now)