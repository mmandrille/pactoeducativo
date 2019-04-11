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

def resultado(request, encuesta_id):
    #Obtenemos la encuesta
    encuesta = Encuesta.objects.get(pk=1)
    #Iniciamos el Diccionario
    resultados = {}
    #Le cargamos todas las opciones con CERO votos
    for preg in encuesta.preguntas.all():
        for opcion in preg.opciones.all():
            resultados[str(preg.orden)+'-'+str(opcion.orden)] = 0
    #OBtenemos las respuestas
    respuestas = encuesta.respuestas.all()
    #Procesamos las respuestas
    for resp in respuestas:
        for r in resp.respuestas.split(','):
            if r != '':
                resultados[r]+=1
    return render(request, 'resultados.html', {'encuesta': encuesta, 'resultados': resultados})