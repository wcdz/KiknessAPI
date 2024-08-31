from django.urls import path, include
from rest_framework import routers
from api import controllers
from .controllers import EstudiantesView, FacultadesView, NivelesAcademicosView

urlpatterns = [
    path('estudiantes/', EstudiantesView.as_view(), name="lista_estudiantes"),
    path('facultades/', FacultadesView.as_view(), name="lista_facultades"),
    path('niveles_academicos/', NivelesAcademicosView.as_view(), name="lista_niveles_academicos"),
]
