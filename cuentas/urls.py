from django.urls import path
from cuentas.views import login


urlpatterns = [
    path('login/', login, name='login'),
]
