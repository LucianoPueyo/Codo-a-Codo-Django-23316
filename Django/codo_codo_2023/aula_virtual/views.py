from django.contrib import messages
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotFound
from django.views.generic.list import ListView
from django.contrib.auth.decorators import login_required
from rest_framework import viewsets, permissions
from .serializers import AlumnoSerializer


from .forms import AltaAlumnoForm, EnviarConsultaForm, AltaInstructorForm
from .models import Alumno, Instructor
def index(request):
    print(request.method)

    # Hagamos de cuenta que este dato viene de la BBDD
    alumno_ficticio = {
        'name': 'Maria',
        'last_name': 'Del Cerro',
        'age': 25,
        'valid': False
    }

    listado_alumnos = Alumno.objects.all()

    print(listado_alumnos.query)

    context = {
        'first_name': 'Carlos',
        'last_name': 'Lopez',
        'alumn': alumno_ficticio,
        'listado_alumnos': listado_alumnos
    }

    return render(request, 'aula_virtual/index.html', context)

def saludar(request, nombre):
    return HttpResponse(f"Hola, <b>{nombre}</b> Bienvenid@ al Aula Virtual")

def alta_alumno(request):
    if request.method == "POST":
        alta_alumno_form = AltaAlumnoForm(request.POST)
        if alta_alumno_form.is_valid():

            nombre = alta_alumno_form.cleaned_data["nombre"]
            apellido = alta_alumno_form.cleaned_data["apellido"]
            dni = alta_alumno_form.cleaned_data["dni"]
            
            alumno_nuevo = Alumno(
                nombre = nombre,
                apellido = apellido,
                mail = alta_alumno_form.cleaned_data["mail"],
                dni = dni,
                legajo = dni + nombre + apellido
            )

            alumno_nuevo.save()

            messages.add_message(request, messages.SUCCESS, 'Alumno dado de alta con éxito', extra_tags="tag1")

            return redirect("listar_alumnos")
    else:
        # GET
        alta_alumno_form = AltaAlumnoForm()
    
    context = {
        'form': alta_alumno_form
    }

    return render(request, 'aula_virtual/alta_alumno.html', context)

def alta_instructor(request):
    context = {}
    if request.method == "POST":
        form = AltaInstructorForm(request.POST)
        if form.is_valid():
            form.save()

            messages.add_message(request, messages.SUCCESS, 'Instructor dado de alta con éxito')
            return redirect("listar_instructores")
    else:
        form = AltaInstructorForm()

    context["form"] = form
    return render(request, 'aula_virtual/alta_instructor.html', context)

def baja_alumno(request):
    return HttpResponse("<h2>Baja de estudiantes activos</h2>")

@login_required
def listar_alumnos(request):
    context = {}

    listado = Alumno.objects.all().order_by('dni')

    context['listado_alumnos'] = listado

    return render(request, 'aula_virtual/listar_alumnos.html', context)


class listar_instructores(ListView):
    model = Instructor
    context_object_name = 'Instructores'
    template_name = 'aula_virtual/listar_instructores.html'
    ordering = ['dni']


def alumnos_2023(request):
    return HttpResponse(
        "<h2>Listado alumnos 2023</h2>"+
        "<p>1 - Carlos Lopez</p>" +
        "<p>2 - Maria Del Cerro</p>" +
        "<p>3- Pedro Gomez</p>"
        )

def alumnos_by_year(request, year):
    if int(year) < 2020:
        return HttpResponseNotFound("<h2> No hay registros para ese año. Sólo válido del 2021 en adelante.</h2>")
    
    else:
        return HttpResponse(
            f"<h2>Listado alumnos {year}</h2>"+
            "<p>2023: 50 alumnos</p>" +
            "<p>2022: 35 alumnos inscriptos</p>" +
            "<p>2021: 127 alumnos inscriptos</p>"
        )
    
def alumnos_by_year_month(request, year, month):
    if int(year) < 2020:
        return HttpResponseNotFound("<h2> No hay registros para ese año. Sólo válido del 2021 en adelante.</h2>")
    
    else:
        if int(month) > 4:
            return HttpResponseNotFound("<h2>Sólo hay registros para el primer cuatrimestre del año.</h2>")
        
        else:
            return HttpResponse(
                f"<h2>Listado alumnos {year}</h2>"+
                "<p>2023: 50 alumnos</p>" +
                "<p>2022: 35 alumnos inscriptos</p>" +
                "<p>2021: 127 alumnos inscriptos</p>"
            )
        
def docentes_by_year(request, year, curso):
    return HttpResponse(
        f"<h2>Docentes correspondientes al año: {year} del curso de {curso}</h2>"+
        "<p>Docente 1</p>" + 
        "<p>Docente 2</p>"
    )

def enviar_consulta(request):
    if request.method == "POST":
        form = EnviarConsultaForm(request.POST)
        if form.is_valid():
            print("------------------------")
            print(form.cleaned_data['mail'])

            messages.add_message(request, messages.SUCCESS, 'Consulta enviada con exito', extra_tags="tag1")

            # Usualmente cuando se completa exitosamente un formulario
            # redirijimos al usuario a otra parte del sitio (por ejemplo al index)
            # para que no intente enivar dos veces el mismo formulario.
            return redirect("index")
    else:
        # GET
        form = EnviarConsultaForm()

    context = {'form': form}

    return render(request, 'aula_virtual/enviar_consulta.html', context)


class AlumnoViewSet(viewsets.ModelViewSet):
    queryset = Alumno.objects.all()
    serializer_class = AlumnoSerializer
    permissions_classes = [permissions.IsAuthenticatedOrReadOnly]
