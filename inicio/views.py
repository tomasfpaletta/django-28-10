from django.shortcuts import render,redirect
from django.template import loader
from django.http import HttpResponse
from inicio.models import Vehiculo 
from inicio.forms import CrearVehiculoFormulario



def inicio(request):
    return render(request, 'inicio.html', {})


def vehiculos(request):
    
    modelo_a_buscar = request.GET.get('modelo')
    if modelo_a_buscar:
      listado_de_vehiculos = Vehiculo.objects.filter(modelo=modelo_a_buscar)

    else:  
      listado_de_vehiculos = Vehiculo.objects.all()
  
    return render(request, 'vehiculos.html', {'listado_de_vehiculos':listado_de_vehiculos})


def crear_vehiculo(request):
    
  #V2 (Django Forms)
    if request.method == 'POST':
      formulario = CrearVehiculoFormulario(request.POST)
      if formulario.is_valid():
        info_limpia=formulario.cleaned_data
        
        marca=info_limpia.get('marca')
        descripcion=info_limpia.get('descripcion')

        vehiculo = Vehiculo(marca=marca,descripcion=descripcion)
        vehiculo.save
        
        return redirect (vehiculos)
      else:
        return render(request,'vehiculo/vehiculos.html',{'formulario':formulario})
      
    formulario = CrearVehiculoFormulario()
    return render(request,'vehiculo/vehiculos.html',{'formulario':formulario})
    

    
