from django.shortcuts import render,redirect
from django.views.generic.list import ListView
from vehiculo.models import Vehiculo, Camioneta, SUVs
from django.views.generic.edit import CreateView, DeleteView
from django.views.generic.detail import DetailView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from vehiculo.forms import BaseForm


class ListadoVehiculos(ListView):
    model = Vehiculo
    context_object_name = 'Listado_de_vehiculos'
    template_name = 'vehiculo/vehiculos.html'
    def get_queryset(self):
        modelo_a_buscar = self.request.GET.get('modelo')
        if modelo_a_buscar:
            return Vehiculo.objects.filter(modelo__icontains=modelo_a_buscar)
        else:
            return Vehiculo.objects.all()

class ListadoCamionetas(ListView):
  model = Camioneta
  context_object_name = 'Listado_de_camionetas'
  template_name = 'vehiculo/camionetas.html'
  def get_queryset(self):
        modelo_a_buscar = self.request.GET.get('modelo')
        if modelo_a_buscar:
            return Camioneta.objects.filter(modelo__icontains=modelo_a_buscar)
        else:
            return Camioneta.objects.all()

class ListadoSuvs(ListView):
  model = SUVs
  context_object_name = 'Listado_de_SUVs'
  template_name = 'vehiculo/SUVs.html'
  def get_queryset(self):
        modelo_a_buscar = self.request.GET.get('modelo')
        if modelo_a_buscar:
            return SUVs.objects.filter(modelo__icontains=modelo_a_buscar)
        else:
            return SUVs.objects.all()
          
class CrearVehiculo(LoginRequiredMixin,CreateView):
   model = Vehiculo
   template_name = "vehiculo/crear_vehiculo.html"
   fields =['tipo','modelo','descripcion']
   success_url = reverse_lazy('vehiculos')
   
class EliminarVehiculo(LoginRequiredMixin,DeleteView):
  model = Vehiculo
  template_name = "vehiculo/eliminar_vehiculo.html"
  success_url = reverse_lazy('vehiculos')
  
class DetalleVehiculo(DetailView):
  model = Vehiculo
  template_name = "vehiculo/detalle_vehiculo.html"
  

def actualizar(request, id):
    actualizar_vehiculo = Vehiculo.objects.get(id=id)
    if request.method == 'POST':
        formulario = BaseForm(request.POST)
        if formulario.is_valid():
            info_nueva = formulario.cleaned_data
            
            actualizar_vehiculo.tipo = info_nueva.get('tipo')
            actualizar_vehiculo.modelo = info_nueva.get('modelo')
            actualizar_vehiculo.descripcion = info_nueva.get('descripcion')
            
            actualizar_vehiculo.save()
            return redirect('vehiculos')
        else:
            return render(request, 'vehiculo/actualizar_vehiculo.html', {'formulario_actualizar' :formulario})
    
    
    
    formulario = BaseForm(initial={'tipo': actualizar_vehiculo.tipo, 'modelo': actualizar_vehiculo.modelo, 'descripcion': actualizar_vehiculo.descripcion})
    return render(request,'vehiculo/actualizar_vehiculo.html', {'formulario_actualizar': formulario})
