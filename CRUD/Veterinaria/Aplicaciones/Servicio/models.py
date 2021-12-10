from django.db import models

# Create your models here.

class Servicios(models.Model):
    id=models.CharField(primary_key=True,max_length=4)
    nombre=models.CharField(max_length=50)

    def __str__(self):
        texto = "{0}"
        return texto.format(self.nombre)