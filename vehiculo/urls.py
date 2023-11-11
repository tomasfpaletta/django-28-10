from django.urls import path
from vehiculo.views import ListadoVehiculos,CrearVehiculo,ListadoCamionetas

urlpatterns = [
    path('vehiculos/',ListadoVehiculos.as_view(),name='vehiculos'),
     path('vehiculos/camionetas',ListadoCamionetas.as_view(),name='eliminar_vehiculo'),
    path('vehiculos/crear/',CrearVehiculo.as_view(),name='crear_vehiculo'),
]
