from django.contrib import admin
from .models import Alumno, Instructor, Detalle_Alumno, Curso

admin.site.register(Alumno)
admin.site.register(Instructor)
admin.site.register(Detalle_Alumno)
admin.site.register(Curso)