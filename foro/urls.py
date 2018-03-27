# -*- coding: utf-8 -*-
#Importamos modulos standars
from django.conf.urls import url
from django.urls import path
#Import de modulos personales
from . import views

#Estas urls se encargaran de parcear todo lo que viene despues de www.mundofacu.com.ar/usr/
urlpatterns = [
	path('', views.foro, name='foro'),
	path('subforo/<int:subforo_id>/', views.subforo, name='subforo'),
	path('thread/<int:thread_id>/', views.thread, name='thread'),
]
