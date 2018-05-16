from django.contrib import admin

#Incluimos modelos
from .models import Album, Foto
# Register your models here.
admin.site.register(Album)
admin.site.register(Foto)