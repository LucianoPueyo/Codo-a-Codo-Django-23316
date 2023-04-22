from django import forms

class AltaAlumnoForm(forms.Form):
    nombre = forms.CharField(label="Nombre Alumno", required=True)
    apellido = forms.CharField(label="Apellido Alumno", required=True)
    mail = forms.EmailField(label="Mail", required=True)
