from __future__ import unicode_literals
import datetime

from django.db import models
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.models import *
from django.contrib.auth.models import User
from pactoeducativo.settings import MEDIA_URL

# Create your models here.
class Archivo(models.Model):
    nombre = models.CharField('Titulo', max_length=200)
    descripcion = models.TextField()
    archivo = models.FileField(upload_to='')
    pub_date = models.DateTimeField('Fecha de Publicacion', default=datetime.datetime.now())
    def __str__(self):
        return self.nombre