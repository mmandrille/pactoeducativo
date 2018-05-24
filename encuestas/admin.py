from django.contrib import admin
#Modulos extras
from nested_inline.admin import NestedStackedInline, NestedModelAdmin
# Register your models here.
from .models import Encuesta, Pregunta, Opcion, Respuesta

#Definimos inline
class OpcionInline(NestedStackedInline):
    model = Opcion
    extra = 1
    fk_name = 'pregunta'

class PreguntaInline(NestedStackedInline):
    model = Pregunta
    extra = 1
    fk_name = 'encuesta'
    inlines = [OpcionInline]

class EncuestaAdmin(NestedModelAdmin):
    model = Encuesta
    inlines = [PreguntaInline]

# Register your models here.
admin.site.register(Encuesta, EncuestaAdmin)