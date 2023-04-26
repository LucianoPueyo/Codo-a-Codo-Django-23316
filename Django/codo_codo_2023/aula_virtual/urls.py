from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('saludar/<str:nombre>/', views.saludar, name="saludar"),
    path('alta_alumno/', views.alta_alumno, name="alta_alumno"),
    path('baja_alumno/', views.baja_alumno, name="baja_alumno"),

    path('alumnos/2023/', views.alumnos_2023, name="alumnos_2023"),
    re_path(r'^alumnos/(?P<year>[0-9]{4})/$', views.alumnos_by_year, name="alumnos_by_year"),
    re_path(r'^alumnos/(?P<year>[0-9]{4})/(?P<month>[0-9]{2})/$', views.alumnos_by_year_month, name="alumnos_by_year_month"),

    path('docentes/<int:year>/', views.docentes_by_year, {'curso': 'Python'}, name="docentes_by_year"),

    path('enviar_consulta',views.enviar_consulta, name="enviar_consulta"),
]