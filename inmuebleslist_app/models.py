from django.db import models
from django.utils import timezone

# Create your models here.

class Empresa(models.Model):
    nombre = models.CharField(max_length=250)
    website = models.URLField(max_length=250)
    fecha_creado = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)
    
    def __str__(self):
        return self.nombre


class Edificacion(models.Model):
    direccion = models.CharField(max_length=250)
    pais = models.CharField(max_length=150)
    descripcion = models.CharField(max_length=500)
    imagen = models.CharField(max_length=900)
    #fecha_creado = models.DateTimeField(default=timezone.now)
    fecha_creado = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE, related_name='edificacionlist')
    
    def __str__(self): 
        return self.direccion

