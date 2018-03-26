from django.shortcuts import render
from datetime import datetime, timedelta
#Import Personales
from .models import Evento

# Create your views here.
def calendario(request):
    eventos = Evento.objects.order_by('fecha')
    return render(request, 'calendario.html', { 'eventos': eventos, 'hoy' : datetime.now().strftime('%d/%m/%Y')})