from django import template
register = template.Library()

@register.simple_tag
def retornar_valor(respuestas, pregunta, opcion):
    return respuestas[str(pregunta) +'-'+ str(opcion)]