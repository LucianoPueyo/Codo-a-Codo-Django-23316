from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("<h1>Bienvenido</h1> al Aula Virtual 2.0")

def alta_alumno(request):
    return HttpResponse("<h2>Alta de nuevos estudiantes</h2>")

def baja_alumno(request):
    return HttpResponse("<h2>Baja de estudiantes activos</h2>")