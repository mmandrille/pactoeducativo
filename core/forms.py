from django import forms

class BuscarForm(forms.Form):
    texto = forms.CharField(max_length=20, help_text='')