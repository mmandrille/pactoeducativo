from django.contrib import admin
#Modulos extras
from nested_inline.admin import NestedStackedInline, NestedModelAdmin
# Register your models here.
from .models import Encuesta, Pregunta, Respuesta

#Definimos inline
class RespuestaInline(NestedStackedInline):
    model = Respuesta
    extra = 1
    fk_name = 'pregunta'

class PreguntaInline(NestedStackedInline):
    model = Pregunta
    extra = 1
    fk_name = 'encuesta'
    inlines = [RespuestaInline]

class EncuestaAdmin(NestedModelAdmin):
    model = Encuesta
    inlines = [PreguntaInline]

# Register your models here.
admin.site.register(Encuesta, EncuestaAdmin)