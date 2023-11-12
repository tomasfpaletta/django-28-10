from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login as django_login


def login(request):
    if request.method == 'POST':
        formulario = AuthenticationForm(request, data=request.POST)
        if formulario.is_valid():
            usuario = formulario.cleaned_data.get('username')
            contra = formulario.cleaned_data.get('password')
    
            user = authenticate(username=usuario, password=contra)
            
            django_login(request, user)
            
            return redirect('inicio')
        
    formulario = AuthenticationForm()
    return render(request,'cuentas/login.html', {'form_iniciar_sesion': formulario})


