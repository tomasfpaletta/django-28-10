from django.urls import path
from vehiculo.views import ListadoVehiculos,CrearVehiculo,ListadoCamionetas,ListadoSuvs,EliminarVehiculo

urlpatterns = [
    path('vehiculos/',ListadoVehiculos.as_view(),name='vehiculos'),
    path('vehiculos/camionetas',ListadoCamionetas.as_view(),name='eliminar_vehiculo'),
    path('vehiculos/camionetas',ListadoCamionetas.as_view(),name='camionetas'),
    path('vehiculos/SUVs',ListadoSuvs.as_view(),name='SUVs'),
    path('vehiculos/crear/',CrearVehiculo.as_view(),name='crear_vehiculo'),
    path('automoviles/<int:pk>/eliminar/', EliminarVehiculo.as_view(),name='eliminar_vehiculo'),
]
