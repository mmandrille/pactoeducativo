from django.shortcuts import render

#import Personales
from .models import Archivo
from .forms import BuscarForm

# Create your views here.
def biblioteca(request):
    if request.method == 'POST':
        form = BuscarForm(request.POST)
        if form.is_valid():
            archivos = Archivo.objects.filter(nombre__icontains=form.cleaned_data['texto'])
    else:
        archivos = Archivo.objects.all()
    form = BuscarForm()
    return render(request, 'biblioteca.html', {'archivos' : archivos, 'form' : form})

def archivo(request, archivo_id):
    archivo = Archivo.objects.get(pk=archivo_id)
    return render(request, 'mostrar_archivo.html', { 'archivo' : archivo })