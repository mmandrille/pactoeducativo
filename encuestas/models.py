from django.db import models
from tinymce.models import HTMLField

# Create your models here.
class Encuesta(models.Model):
    titulo = models.CharField('Encuesta', max_length=100)
    descripcion = HTMLField()
    def __str__(self):
        return self.titulo

class Pregunta(models.Model):
    encuesta = models.ForeignKey(Encuesta, on_delete=models.CASCADE)
    orden = models.IntegerField()
    pregunta = models.CharField('Pregunta', max_length=200)
    def __str__(self):
        return self.pregunta

class Respuesta(models.Model):
    pregunta =  models.ForeignKey(Pregunta, on_delete=models.CASCADE)
    orden = orden = models.IntegerField()
    opcion = models.CharField('Respuesta', max_length=200)
    def __str__(self):
        return self.opcion