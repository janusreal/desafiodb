from django.db import models

# Create your models here.

class Cliente(models.Model):
    usuario = models.CharField(max_length=20)
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=20)
    correo = models.EmailField(max_length=50)

class Producto(models.Model):
    descripcion = models.CharField(max_length=100)
    cliente = models.ForeignKey(Cliente, on_delete = models.CASCADE)
    
