from django.urls import path
from vehiculo.views import ListadoVehiculos,CrearVehiculo,ListadoCamionetas,ListadoSuvs,EliminarVehiculo,DetalleVehiculo,actualizar

urlpatterns = [
    path('vehiculos/',ListadoVehiculos.as_view(),name='vehiculos'),
    path('vehiculos/camionetas',ListadoCamionetas.as_view(),name='camionetas'),
    path('vehiculos/SUVs',ListadoSuvs.as_view(),name='SUVs'),
    path('vehiculos/crear/',CrearVehiculo.as_view(),name='crear_vehiculo'),
    path('vehiculos/<int:pk>/detalle/',DetalleVehiculo.as_view(),name='detalle_vehiculo'),
    path('vehiculos/<int:pk>/eliminar/',EliminarVehiculo.as_view(),name='eliminar_vehiculo'),
    path('vehiculos/<int:id>/actualizar/', actualizar, name='actualizar_vehiculo'),
]
