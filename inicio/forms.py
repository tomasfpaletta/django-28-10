from django import forms

class CrearVehiculoFormulario(forms.Form):
    marca = forms.CharField(max_length=30)
    descripcion = forms.CharField(max_length=250)
    
    
    