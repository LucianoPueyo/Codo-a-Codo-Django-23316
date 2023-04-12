from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

def index(request):
    print(request.method)

    # Hagamos de cuenta que este dato viene de la BBDD
    alumno_ficticio = {
        'name': 'Maria',
        'last_name': 'Del Cerro',
        'age': 25,
        'valid': False
    }

    listado_alumnos = [
        {
            'name': 'Maria',
            'last_name': 'Del Cerro',
            'age': 25,
            'valid': False,
        },
        {
            'name': 'Florencia',
            'last_name': 'Perez',
            'age': 30,
            'valid': False,
        },
        {
            'name': 'Martin',
            'last_name': 'Del Moro',
            'age': 35,
            'valid': False,
        },
    ]

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
    return HttpResponse("<h2>Alta de nuevos estudiantes</h2>")

def baja_alumno(request):
    return HttpResponse("<h2>Baja de estudiantes activos</h2>")

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