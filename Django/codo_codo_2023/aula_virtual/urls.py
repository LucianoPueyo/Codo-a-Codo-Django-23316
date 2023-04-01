from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('alta_alumno', views.alta_alumno, name="alta_alumno"),
    path('baja_alumno', views.baja_alumno, name="baja_alumno"),
]