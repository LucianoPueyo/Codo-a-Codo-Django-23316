from django.db import models

class Alumno(models.Model):
    nombre = models.CharField(max_length=128, verbose_name="Nombre")
    apellido = models.CharField(max_length=128, verbose_name="Apellido")
    mail = models.EmailField(max_length=128, verbose_name="Mail")
    dni = models.CharField(max_length=8, verbose_name="DNI", null=True)


class Detalle_Alumno(models.Model):
    fecha_nacimiento = models.DateField(null=True)
    mail_alternativo = models.EmailField(max_length=128, verbose_name="Mail Alternativo")
    telefono_alternativo = models.IntegerField(max_length=10 ,verbose_name="Teléfono alternativo")
    alumno = models.OneToOneField(Alumno, on_delete=models.CASCADE, primary_key=True) # Uno a uno


class Instructor(models.Model):
    nombre = models.CharField(max_length=128, verbose_name="Nombre")
    apellido = models.CharField(max_length=128, verbose_name="Apellido")
    mail = models.EmailField(max_length=128, verbose_name="Mail")
    dni = models.CharField(max_length=8, verbose_name="DNI", null=True)


class Curso(models.Model):
    comision = models.IntegerField(max_length=4 ,verbose_name="Número de comisión")
    instructor = models.ForeignKey(Instructor, on_delete=models.CASCADE) # muchos a uno
    alumnos = models.ManyToManyField(Alumno) # Muchos a muchos

