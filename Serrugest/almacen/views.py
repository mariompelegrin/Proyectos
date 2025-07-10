from django.shortcuts import render
from django.shortcuts import render, redirect
from .forms import MaterialForm, ValeEntradaForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required

@login_required
def registrar_material(request):
    if request.method == 'POST':
        form = MaterialForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Material registrado correctamente.")
            return redirect('registrar_material')
        else:
            messages.error(request, "Por favor corrige los errores.")
    else:
        form = MaterialForm()
    return render(request, 'almacen/registrar_material.html', {'form': form})

@login_required
def registrar_entrada(request):
    if request.method == 'POST':
        form = ValeEntradaForm(request.POST)
        if form.is_valid():
            vale = form.save(commit=False)
            vale.responsable = request.user
            vale.save()
            messages.success(request, "Entrada registrada correctamente.")
            return redirect('registrar_entrada')
        else:
            messages.error(request, "Hay errores en el formulario.")
    else:
        form = ValeEntradaForm()
    return render(request, 'almacen/registrar_entrada.html', {'form': form})
