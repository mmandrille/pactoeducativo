from django.conf.urls import url
from django.urls import path
#Import personales
from . import views

app_name = 'encuestas'
urlpatterns = [
    path('<int:encuesta_id>/', views.encuesta, name='encuesta'),
    path('resultado/<int:encuesta_id>/', views.resultado, name='resultado'),
]