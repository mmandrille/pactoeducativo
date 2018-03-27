from __future__ import unicode_literals
import datetime
from django.db import models
from django.contrib.auth.models import *
from django.utils import timezone

#Create your models here.
class Evento(models.Model):
    nombre = models.CharField('Titulo', max_length=200)
    descripcion = models.TextField()
    fecha = models.DateTimeField('Fecha del Evento')
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    pub_date = models.DateTimeField('Fecha de Publicacion', default=timezone.now, editable = False)
    def __str__(self):
        return self.nombre