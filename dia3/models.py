from django.db import models

# Create your models here.
class Tarea(models.Model):
    descripcion = models.TextField(default='', unique=True)
    eliminada = models.BooleanField(default=False)
    # subtareas = [Subtarea 1, Subtarea 2, ...]    

class SubTarea(models.Model):
    descripcion = models.TextField(default='')
    eliminada = models.BooleanField(default=False)
    tarea = models.ForeignKey(Tarea, related_name='subtareas', on_delete=models.CASCADE)
    
