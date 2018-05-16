from __future__ import unicode_literals
import datetime

from django.db import models
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.models import *
from django.contrib.auth.models import User
from pactoeducativo.settings import MEDIA_URL
from django.utils import timezone

# Create your models here.
class Archivo(models.Model):
    tipos_de_archivos = (
        (1, 'Biblioteca'),
        (2, 'Insumos'),
    )
    tipo = models.IntegerField(choices=tipos_de_archivos, default=1)
    nombre = models.CharField('Titulo', max_length=200)
    descripcion = models.TextField()
    portada = models.FileField(upload_to='portadas/', default='/archivos/defaults/noimage.gif')
    archivo = models.FileField(upload_to='')
    pub_date = models.DateTimeField('Fecha de Publicacion', default=timezone.now)
    def __str__(self):
        return self.nombre