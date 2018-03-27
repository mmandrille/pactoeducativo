from __future__ import unicode_literals
import datetime
from django.db import models
#Agregar Modulos personales

#Elementos del FAQ
class Faq(models.Model):
    orden = models.IntegerField()
    pregunta = models.CharField('Titulo', max_length=200)
    respuesta = models.TextField()
    def __str__(self):
        return self.pregunta
