# almacen/models.py
from django.db import models
from usuarios.models import Usuario
from trabajos.models import Trabajo

class Material(models.Model):
    nombre = models.CharField(max_length=100)
    unidad = models.CharField(max_length=20)
    cantidad_disponible = models.FloatField(default=0)

    def __str__(self):
        return f"{self.nombre} ({self.cantidad_disponible} {self.unidad})"

class ValeEntrada(models.Model):
    fecha = models.DateField(auto_now_add=True)
    descripcion = models.TextField()
    material = models.ForeignKey(Material, on_delete=models.CASCADE)
    cantidad = models.FloatField()
    responsable = models.ForeignKey(Usuario, on_delete=models.SET_NULL, null=True)

class ValeSalida(models.Model):
    fecha = models.DateField(auto_now_add=True)
    descripcion = models.TextField()
    material = models.ForeignKey(Material, on_delete=models.CASCADE)
    cantidad = models.FloatField()
    trabajo = models.ForeignKey(Trabajo, on_delete=models.CASCADE)
    responsable = models.ForeignKey(Usuario, on_delete=models.SET_NULL, null=True)