from django.shortcuts import render,redirect
from django.views.generic.list import ListView
from vehiculo.models import Vehiculo
from django.views.generic.edit import CreateView 
from django.urls import reverse_lazy
# from inicio.forms import CrearVehiculoFormulario


class ListadoVehiculos(ListView):
    model = Vehiculo
    context_object_name = 'Listado_de_vehiculos'
    template_name = 'vehiculo/vehiculos.html'

class CrearVehiculo(CreateView):
   model = Vehiculo
   template_name = "vehiculo/crear_vehiculo.html"
   fields =['marca','modelo','descripcion','fecha_creacion']
   success_url = reverse_lazy('vehiculos')
   
# def crear_vehiculo(request):
    
#   #V2 (Django Forms)
#     if request.method == 'POST':
#       formulario = CrearVehiculoFormulario(request.POST)
#       if formulario.is_valid():
#         info_limpia=formulario.cleaned_data
        
#         marca=info_limpia.get('marca')
#         descripcion=info_limpia.get('descripcion')

        # vehiculo = Vehiculo(marca=marca,descripcion=descripcion)
        # vehiculo.save
        
        # return redirect ('vehiculos')
      # else:
        # return render(request,'vehiculo/vehiculos.html',{'formulario':formulario})
      
    # formulario = CrearVehiculoFormulario()
    # return render(request,'vehiculo/vehiculos.html',{'formulario':formulario})