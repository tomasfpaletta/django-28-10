from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import authenticate, login as django_login
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy
from cuentas.forms import MiFormularioDeCreacion, EditarPerfil
from cuentas.models import DatosExtra
from django.views.generic.list import ListView 


def login(request):
    if request.method == 'POST':
        formulario = AuthenticationForm(request, data=request.POST)
        if formulario.is_valid():
            usuario = formulario.cleaned_data.get('username')
            contra = formulario.cleaned_data.get('password')
    
            user = authenticate(username=usuario, password=contra)
            
            django_login(request, user)
            
            DatosExtra.objects.get_or_create(user=request.user)
            
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
    
    datos_extra = request.user.datosextra
    
    formulario = EditarPerfil(instance=request.user, initial={'biografia': datos_extra.biografia, 'avatar': datos_extra.avatar,'user':datos_extra.user})
    
    if request.method == 'POST':
        formulario = EditarPerfil(request.POST,request.FILES, instance=request.user)
        
        if formulario.is_valid():
            
            nueva_biografia = formulario.cleaned_data.get('biografia')
            nueva_avatar = formulario.cleaned_data.get('avatar')
            nueva_user = formulario.cleaned_data.get('user')
            
            if nueva_biografia: 
                datos_extra.biografia = nueva_biografia
            if nueva_avatar:
                datos_extra.avatar = nueva_avatar
            if nueva_user:
                datos_extra.user = nueva_user
                    
            datos_extra.save()   
            formulario.save()
            
            return redirect('perfil')
        
    return render(request, 'cuentas/editar_perfil.html', {'formulario': formulario})

class CambioPassword(PasswordChangeView):
    template_name = 'cuentas/cambiar_password.html'
    success_url = reverse_lazy('perfil')
    
    
    
class Perfil(ListView):
    model = DatosExtra
    template_name = 'cuentas/perfil.html'
    