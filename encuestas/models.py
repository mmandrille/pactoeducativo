from django.db import models
from tinymce.models import HTMLField
from django.contrib.auth.models import User

# Create your models here.
class Encuesta(models.Model):
    titulo = models.CharField('Encuesta', max_length=100)
    descripcion = HTMLField()
    def __str__(self):
        return self.titulo

class Pregunta(models.Model):
    encuesta = models.ForeignKey(Encuesta, on_delete=models.CASCADE, related_name='preguntas')
    orden = models.IntegerField()
    pregunta = models.CharField('Pregunta', max_length=200)
    def __str__(self):
        return self.pregunta

class Opcion(models.Model):
    pregunta =  models.ForeignKey(Pregunta, on_delete=models.CASCADE, related_name='opciones')
    orden = orden = models.IntegerField()
    opcion = models.CharField('Opcion', max_length=200)
    def __str__(self):
        return self.opcion

class Respuesta(models.Model):
    encuesta = models.ForeignKey(Encuesta, on_delete=models.CASCADE, related_name='respuestas')
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    respuestas= models.CharField('Respuesta', max_length=200)
    def __str__(self):
        return self.encuesta.titulo + '-' + self.usuario.username