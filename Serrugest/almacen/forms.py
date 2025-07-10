# almacen/forms.py
from django import forms
from .models import Material, ValeEntrada

class MaterialForm(forms.ModelForm):
    class Meta:
        model = Material
        fields = ['nombre', 'unidad', 'cantidad_disponible']

    def clean_nombre(self):
        nombre = self.cleaned_data['nombre']
        if Material.objects.filter(nombre__iexact=nombre).exists():
            raise forms.ValidationError("Ya existe un material con ese nombre.")
        return nombre

class ValeEntradaForm(forms.ModelForm):
    class Meta:
        model = ValeEntrada
        fields = ['descripcion', 'material', 'cantidad']

    def clean_cantidad(self):
        cantidad = self.cleaned_data['cantidad']
        if cantidad <= 0:
            raise forms.ValidationError("La cantidad debe ser mayor a cero.")
        return cantidad
