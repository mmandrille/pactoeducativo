#Importamos librerias standars
import datetime
from django import forms
from django.contrib.admin import widgets
from django.forms import ModelForm
from django.forms.models import modelformset_factory

#Librerias realizadas por nosotros
from .models import Subforo, Thread

#Definicion de formularios de trabajo
class ThreadForm(ModelForm):
	nombre = forms.CharField(label='Titulo', widget=forms.TextInput(attrs={'size':35}))
	body = forms.CharField(label="Cuerpo", widget=forms.Textarea(attrs={'style':'width: 450px; height: 350px'}))
	class Meta:
		model = Thread
		fields = ['nombre','subforo','body']
		exclude = ['user','autor', 'fecha_creacion', 'estado']

class PostForm(forms.Form):
	body = forms.CharField(label="", widget=forms.Textarea(attrs={'style':'width:50%; left:25%; margin-left:0%; height:100px'}))

class SubForoForm(ModelForm):
	class Meta:
		model = Subforo
		exclude = ["activo"]