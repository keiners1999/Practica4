from django.db import models
from apps.empleado.models import Empleado

# Create your models her

class Equipo(models.Model):
    nombre = models.CharField(max_length=30)
    marca = models.CharField(max_length=30)
    modelo = models.CharField(max_length=30)
    empleado = models.ManyToManyField(Empleado, through='Mantenimiento')
    
    def __str__(self):
        return self.nombre
    
    
    
class Mantenimiento(models.Model):
    EmpleadoId= models.ForeignKey(Empleado, on_delete= models.CASCADE)
    EquipoId = models.ForeignKey(Equipo, on_delete= models.CASCADE)
    fecha = models.CharField(max_length=30)
    tipoMantenimiento = models.CharField(max_length=30)
    