from django.urls import path, include
from inicio.views import inicio,vehiculos

urlpatterns = [
    path('', inicio, name= 'inicio'),
    #path('vehiculos/',vehiculos,name='vehiculos'),
    path('vehiculos/', include('vehiculo.urls')),   
]
