from django.urls import path
from vehiculo.views import ListadoVehiculos,CrearVehiculo

urlpatterns = [
    path('vehiculos/',ListadoVehiculos.as_view(),name='vehiculos'),
    path('vehiculos/crear/',CrearVehiculo.as_view(),name='crear_vehiculo'),
]
