from django.shortcuts import render

#import Personales
from .models import Album, Foto

# Create your views here.
def encontrate(request):
    albums = Album.objects.all()
    return render(request, 'encontrate.html', {'albums' :albums})

def album(request, album_id):
    album = Album.objects.get(pk=album_id)
    fotos = Foto.objects.filter(album=album_id)
    return render(request, 'mostrar_album.html', {'album': album,'fotos': fotos})