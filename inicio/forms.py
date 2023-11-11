from django import forms

class CrearVehiculoFormulario(forms.Form):
    marca = forms.CharField(max_length=30)
    descripcion = forms.CharField(max_length=250)

class BusquedaVehiculoFormulario(forms.Form):
    marca = forms.CharField(max_length=50, required=False)
    modelo = forms.CharField(max_length=40, required=False)
    
    
    