# trabajos/models.py
from django.db import models
from usuarios.models import Usuario

class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    contacto = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.nombre

class Trabajo(models.Model):
    ESTADOS = [
        ('comercial', 'Comercial'),
        ('diseno', 'Diseño'),
        ('produccion', 'Producción'),
        ('economia', 'Económica'),
        ('despacho', 'Despacho'),
        ('entregado', 'Entregado'),
        ('cancelado', 'Cancelado'),
    ]

    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    cliente = models.ForeignKey(Cliente, on_delete=models.SET_NULL, null=True)
    fecha_creacion = models.DateField(auto_now_add=True)
    fecha_entrega = models.DateField(null=True, blank=True)
    estado = models.CharField(max_length=20, choices=ESTADOS, default='comercial')
    trabajadores_asignados = models.ManyToManyField(Usuario, related_name='trabajos_asignados', blank=True)

    def __str__(self):
        return f"{self.nombre} - {self.get_estado_display()}"

class ArchivoDiseno(models.Model):
    trabajo = models.ForeignKey(Trabajo, on_delete=models.CASCADE, related_name='archivos_diseno')
    archivo = models.FileField(upload_to='disenos/')
    fecha_subida = models.DateTimeField(auto_now_add=True)

class DetalleDiseno(models.Model):
    trabajo = models.OneToOneField(Trabajo, on_delete=models.CASCADE, related_name='detalle_diseno')
    materiales = models.TextField()
    medidas = models.CharField(max_length=100)
    observaciones = models.TextField(blank=True)

class Produccion(models.Model):
    trabajo = models.OneToOneField(Trabajo, on_delete=models.CASCADE)
    corte_realizado = models.BooleanField(default=False)
    impresion_realizada = models.BooleanField(default=False)
    montaje_realizado = models.BooleanField(default=False)
    observaciones = models.TextField(blank=True)

class FichaCosto(models.Model):
    trabajo = models.OneToOneField(Trabajo, on_delete=models.CASCADE)
    costo_materiales = models.DecimalField(max_digits=10, decimal_places=2)
    costo_mano_obra = models.DecimalField(max_digits=10, decimal_places=2)
    tiempo_disenio = models.FloatField(help_text="En horas")
    total = models.DecimalField(max_digits=10, decimal_places=2)
