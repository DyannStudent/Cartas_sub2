from django.db import models


class Vendedor(models.Model):
    nombre = models.CharField(max_length=100)
    reputacion = models.FloatField()
    especialidad = models.CharField(max_length=200)
    ventas_realizadas = models.IntegerField(default=0)
# Create your models here.


# ---------------- Recurso Cliente (Andrés) ----------------
class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField()
    ciudad = models.CharField(max_length=100)
    cartas_compradas = models.IntegerField(default=0)

    def __str__(self):
        return self.nombre
