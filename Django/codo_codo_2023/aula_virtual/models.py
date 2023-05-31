from django.db import models


class Persona(models.Model):
    nombre = models.CharField(max_length=128, verbose_name="Nombre")
    apellido = models.CharField(max_length=128, verbose_name="Apellido")
    mail = models.EmailField(max_length=128, verbose_name="Mail")
    dni = models.CharField(max_length=8, verbose_name="DNI", null=True)

    class Meta:
        abstract = True

    def __str__(self):
        return f"{self.nombre} {self.apellido} - dni: {self.dni}"


class Instructor(Persona):
    cuit = models.CharField(max_length=100, verbose_name="Cuit", null=True)
    

class Alumno(Persona):
    legajo  = models.CharField(max_length=100, verbose_name="Legajo", null=True)


class Detalle_Alumno(models.Model):
    fecha_nacimiento = models.DateField(null=True)
    mail_alternativo = models.EmailField(max_length=128, verbose_name="Mail Alternativo")
    telefono_alternativo = models.IntegerField(verbose_name="Teléfono alternativo")
    alumno = models.OneToOneField(Alumno, on_delete=models.CASCADE, primary_key=True) # Uno a uno


class Curso(models.Model):
    comision = models.IntegerField(verbose_name="Número de comisión")
    instructor = models.ForeignKey(Instructor, on_delete=models.CASCADE) # muchos a uno
    alumnos = models.ManyToManyField(Alumno) # Muchos a muchos

    def __str__(self):
        return f"Comisión: {self.comision}"

