from django.shortcuts import render
from datetime import datetime, timedelta
#Import Personales
from .models import Evento

# Create your views here.
def calendario(request):
    eventos = Evento.objects.filter(fecha_inicio__date=date.today())
    importantes = Evento.objects.filter(importante=True, fecha_inicio__date__gt=date.today())
    return render(request, 'home.html', { 'eventos': eventos, 'importantes': importantes, 'hoy' : datetime.now().strftime('%d/%m/%Y')})