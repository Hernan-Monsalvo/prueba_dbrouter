from django.db import models

# Create your models here.
class Cliente(models.Model):
    nombre = models.CharField(max_length=64)
    apellido = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.nombre} -- {self.apellido}"
