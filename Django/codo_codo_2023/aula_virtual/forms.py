from django import forms
from django.core.exceptions import ValidationError
from .models import Alumno, Instructor

BIRTH_YEAR_CHOICES = range(1980,2006)
TYPE_CHOICES = [
    ("General", "General"),
    ("Diploma_tramite", "Diploma en tramite"),
    ("Otros", "Otros"),
]

class AltaAlumnoForm(forms.Form):
    nombre = forms.CharField(label="Nombre Alumno",widget=forms.TextInput(attrs={'class': 'nombre_alumno rojo'}), required=True)
    apellido = forms.CharField(label="Apellido Alumno", required=True)
    mail = forms.EmailField(label="Mail", required=True)
    dni = forms.CharField(label="Dni Alumno", required=True)

    def clean(self):
        # Validar si el Alumno a crear ya existe
        if Alumno.objects.filter(dni=self.cleaned_data["dni"]).exists():
            raise ValidationError("Ya existe un Alumno con ese DNI")

class AltaInstructorForm(forms.ModelForm):
    class Meta:
        model = Instructor
        fields = '__all__'


class EnviarConsultaForm(forms.Form):
    mail = forms.EmailField(label="Mail", required=True)
    # tipo = forms.MultipleChoiceField(
    #     widget=forms.Select,
    #     choices=TYPE_CHOICES,
    # )

    # fecha_ingreso = forms.DateField(
    #     widget=forms.SelectDateWidget(years=BIRTH_YEAR_CHOICES)
    # )

    # Campo Fecha con date picker en el chrome.
    fecha = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    
    mensaje = forms.CharField(widget=forms.Textarea)
    
    def clean_mail(self):
        # Validación del campo Mail

        # Para mas detalle
        # https://docs.djangoproject.com/en/4.2/ref/forms/validation/

        # aqui podemos poner la logica de negocio necesaria para 
        # efectivamente validar si por ejemplo el campo mail es valido
        # o no.

        # Si es valido se devuelve la info, caso contrario se lanza 
        # un ValidationError.

        # Pueden cambiar la logica del if para probar ambos casos.

        data = self.cleaned_data["mail"]
        # if True:
        #     raise ValidationError("El mail utilizado ya existe")

        # Always return a value to use as the new cleaned data, even if
        # this method didn't change it.
        return data

    def clean(self):
        pass

