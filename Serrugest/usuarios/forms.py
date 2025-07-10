from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Usuario
import re

class RegistroUsuarioForm(UserCreationForm):
    nombre = forms.CharField(max_length=30, label='Nombre')
    apellidos = forms.CharField(max_length=30, label='Apellidos')
    ci = forms.CharField(max_length=11, min_length=11, label='Carnet de Identidad')
    rol = forms.ChoiceField(choices=Usuario.ROL_CHOICES, label='Rol')

    class Meta:
        model = Usuario
        fields = ['username', 'nombre', 'apellidos', 'ci', 'rol', 'password1', 'password2']
        labels = {
            'username': 'Nombre de usuario',
            'nombre': 'Nombre',
            'apellidos': 'Apellidos',
            'ci': 'Carnet de Identidad',
            'rol': 'Rol',
            'password1': 'Contraseña',
            'password2': 'Confirmar contraseña',
        }
        help_texts = {field: '' for field in fields}

    def clean_nombre(self):
        nombre = self.cleaned_data.get('nombre')
        if not re.match(r'^[a-zA-ZáéíóúÁÉÍÓÚüÜñÑ\s]+$', nombre):
            raise forms.ValidationError("El nombre solo puede contener letras.")
        return nombre

    def clean_apellidos(self):
        apellidos = self.cleaned_data.get('apellidos')
        if not re.match(r'^[a-zA-ZáéíóúÁÉÍÓÚüÜñÑ\s]+$', apellidos):
            raise forms.ValidationError("Los apellidos solo pueden contener letras.")
        return apellidos

    def clean_ci(self):
        ci = self.cleaned_data.get('ci')
        if not ci.isdigit() or len(ci) != 11:
            raise forms.ValidationError("El CI debe tener exactamente 11 dígitos numéricos.")

        anio = int(ci[:2])
        mes = int(ci[2:4])
        dia = int(ci[4:6])

        if not (1 <= mes <= 12):
            raise forms.ValidationError("El mes del CI no es válido.")
        if not (1 <= dia <= 31):
            raise forms.ValidationError("El día del CI no es válido.")
        return ci

    def clean_password1(self):
        password = self.cleaned_data.get('password1')

        if len(password) < 8:
            raise forms.ValidationError("La contraseña debe tener al menos 8 caracteres.")
        if not re.search(r'[A-Z]', password):
            raise forms.ValidationError("La contraseña debe contener al menos una letra mayúscula.")
        if not re.search(r'[a-z]', password):
            raise forms.ValidationError("La contraseña debe contener al menos una letra minúscula.")
        if not re.search(r'\d', password):
            raise forms.ValidationError("La contraseña debe contener al menos un número.")
        if not re.search(r'[^\w\s]', password):
            raise forms.ValidationError("La contraseña debe contener al menos un carácter especial.")
        return password
