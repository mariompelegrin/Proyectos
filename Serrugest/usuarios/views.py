from django.shortcuts import render, redirect
from .forms import RegistroUsuarioForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.decorators import login_required, user_passes_test
from django.db.models import Q
from .models import Usuario
from django.contrib.auth import logout
from django.shortcuts import redirect

def cerrar_sesion(request):
    logout(request)
    return redirect('login')

def es_admin(user):
    return user.is_authenticated and user.rol == 'admin'

@login_required
@user_passes_test(es_admin)
def registrar_usuario(request):
    if request.method == 'POST':
        form = RegistroUsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Usuario registrado correctamente.')
            return redirect('registrar_usuario')
        else:
            messages.error(request, 'Corrige los errores del formulario.')
    else:
        form = RegistroUsuarioForm()
    return render(request, 'usuarios/registrar_usuario.html', {'form': form})


@login_required
@user_passes_test(es_admin)
@login_required
def dashboard_admin(request):
    usuarios = Usuario.objects.all()
    form = RegistroUsuarioForm()

    if request.method == 'POST':
        form = RegistroUsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Usuario registrado correctamente.')
            return redirect('dashboard_admin')
        else:
            messages.error(request, 'Corrija los errores del formulario.')

    return render(request, 'usuarios/dashboard_admin.html', {
        'form': form,
        'usuarios': usuarios
    })