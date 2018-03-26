# -*- coding: utf-8 -*-
#Importamos librerias standars
import datetime
from django import forms
from django.contrib.admin import widgets
from django.forms import ModelForm
from django.forms.models import modelformset_factory
from django.forms.extras.widgets import SelectDateWidget

#Librerias realizadas por nosotros
from models import subforos, threads

#Definicion de formularios de trabajo
class Fthread(ModelForm):
	titulo = forms.CharField(label='Titulo', widget=forms.TextInput(attrs={'size':35}))
	resumen = forms.CharField(label="Resumen", widget=forms.Textarea(attrs={'style':'width: 450px; height: 100px'}))
	body = forms.CharField(label="Cuerpo", widget=forms.Textarea(attrs={'style':'width: 450px; height: 350px'}))
	class Meta:
		model = threads
		fields = ['titulo','subforo','body','resumen']
		exclude = ['user','autor', 'fecha_creacion', 'padre', 'puntaje', 'estado','tipo_thread']


class Fcomentario(forms.Form):
	body = forms.CharField(label="", widget=forms.Textarea(attrs={'style':'width:50%; left:25%; margin-left:0%; height:100px'}))

class Fdenuncia(forms.Form):
	motivo = forms.CharField(label="Razon", widget=forms.Textarea(attrs={'style':'width:480px; left:25%; margin-left:0%; height:100px'}))

class Fsubforo(ModelForm):
	class Meta:
		model = subforos
		exclude = ["activo"]