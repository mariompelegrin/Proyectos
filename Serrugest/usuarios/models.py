from django.db import models
from django.contrib.auth.models import AbstractUser

class Usuario(AbstractUser):
    ROL_CHOICES = (
        ('admin', 'Administrador'),
        ('almacen', 'Almacenero'),
        ('comercial', 'Comercial'),
        ('diseñador', 'Diseñador'),
        ('tecnico', 'Técnico de producción'),
        ('economico', 'Económico'),
    )

    nombre = models.CharField(max_length=30)
    apellidos = models.CharField(max_length=30)
    ci = models.CharField(max_length=11, unique=True)
    rol = models.CharField(max_length=20, choices=ROL_CHOICES)

    def __str__(self):
        return f"{self.username} ({self.rol})"