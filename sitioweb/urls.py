from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('inicio.urls')),
    path('vehiculo/', include('vehiculo.urls')),
    path('cuentas/', include('cuentas.urls')),
    path('admin/', admin.site.urls),
]
