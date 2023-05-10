from django.db import models

class Alumno(models.Model):
    nombre = models.CharField(max_length=128, verbose_name="Nombre")
    apellido = models.CharField(max_length=128, verbose_name="Apellido")
    mail = models.EmailField(max_length=128, verbose_name="Mail")
    fecha_nacimiento = models.DateField(null=True)
    dni = models.CharField(max_length=8, verbose_name="DNI", null=True)