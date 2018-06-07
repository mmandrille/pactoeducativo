from django.shortcuts import render

from .models import Encuesta, Pregunta, Opcion, Respuesta
# Create your views here.
def encuesta(request, encuesta_id):
    encuesta = Encuesta.objects.get(pk=encuesta_id)
    if request.method == 'POST':
        respuesta = Respuesta()
        respuesta.encuesta = encuesta
        respuesta.usuario = request.user
        #Recogemos todas las respuestas seleccionadas:
        for pregunta in encuesta.preguntas.all():
                respuesta.respuestas += request.POST[str(pregunta.orden)] + ','
        respuesta.save()

        #Por cada opcion de cada pregunta, recolectamos la cantidad de elecciones de los distintos usuarios.
        selecciones = []
        for pregunta in encuesta.preguntas.all():
            for opcion in pregunta.opciones.all():
                match = str(pregunta.orden) + '-' + str(opcion.orden) + ','
                matches = encuesta.respuestas.filter(respuestas__contains=match)
                selecciones.append([pregunta.orden, opcion.orden, len(matches)])

        return render(request, 'encuesta_resp.html', {'encuesta': encuesta, 'selecciones': selecciones,})
    else:
        return render(request, 'encuesta.html', {'encuesta': encuesta,})
