from django.shortcuts import render

from .models import Encuesta, Pregunta, Opcion, Respuesta
# Create your views here.
def encuesta(request, encuesta_id):
    encuesta = Encuesta.objects.get(pk=1)
    if request.method == 'POST':
        respuesta = Respuesta()
        respuesta.encuesta = encuesta
        respuesta.usuario = request.user
        #Recogemos todas las respuestas seleccionadas:
        for pregunta in encuesta.preguntas.all():
                respuesta.respuestas+= request.POST[str(pregunta.id)] + ','
        respuesta.save()
        return render(request, 'encuesta_resp.html')
    else:
        return render(request, 'encuesta.html', {'encuesta': encuesta,})
