from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import authenticate, login as django_login
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy
from cuentas.forms import MiFormularioDeCreacion, EditarPerfil


def login(request):
    if request.method == 'POST':
        formulario = AuthenticationForm(request, data=request.POST)
        if formulario.is_valid():
            usuario = formulario.cleaned_data.get('username')
            contra = formulario.cleaned_data.get('password')
    
            user = authenticate(username=usuario, password=contra)
            
            django_login(request, user)
            
            return redirect('inicio')
        else:
            return render(request,'cuentas/login.html', {'form_iniciar_sesion': formulario})

        
    formulario = AuthenticationForm()
    return render(request,'cuentas/login.html', {'form_iniciar_sesion': formulario})

def registro(request):
    formulario = MiFormularioDeCreacion()
    if request.method == 'POST':
        formulario = MiFormularioDeCreacion(request.POST)
        if formulario.is_valid():
            
            formulario.save()
            
            return redirect('login')
         
    return render(request, 'cuentas/registro.html',{'form_iniciar_registro': formulario})

def editar_perfil(request):
    formulario = EditarPerfil(instance=request.user)
    
    if request.method == 'POST':
        formulario = editar_perfil(request.POST,intance=request.user)
        
        if formulario.is_valid():
            
            formulario.save()
        
    return render(request, 'cuentas/editar_perfil.html', {'formulario': formulario})

class CambioPassword(PasswordChangeView):
    template_name = 'cuentas/cambiar_password.html'
    success_url = reverse_lazy('editar_perfil')