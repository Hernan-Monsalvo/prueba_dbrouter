from django.db import models
from clientes.models import Cliente

# Create your models here.
class Vehiculo(models.Model):
    dominio = models.CharField(max_length=64)
    marca = models.CharField(max_length=64)
    modelo = models.CharField(max_length=64)
    titular = models.ForeignKey(Cliente, on_delete=models.SET("eliminado"), related_name="titular")

    def __str__(self):
        return f"{self.dominio} --- {self.modelo}"

class Informe(models.Model):
    vehiculo = models.ForeignKey(Vehiculo, on_delete=models.SET("eliminado"), related_name="vehiculo")
    fecha = models.DateField()
    condicion = models.BooleanField()

    def __str__(self):
        return f"{self.fecha} -- {self.vehiculo} --- {self.condicion}"




