from django.shortcuts import render

from .models import Encuesta, Pregunta, Respuesta
# Create your views here.
def encuesta(request, encuesta_id):
    #encuesta = Encuesta.objects.get(pk=1)
    return render(request, 'encuesta.html', {})