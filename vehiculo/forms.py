from django import forms

class BaseForm(forms.Form):
    tipo = forms.CharField(max_length=20)
    modelo = forms.CharField(max_length=20)
    descripcion = forms.CharField(max_length=200)
