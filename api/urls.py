from django.urls import path, include
from rest_framework import routers
from api import controllers
from .controllers import EstudiantesView, FacultadesView

urlpatterns = [
    path('estudiantes/', EstudiantesView.as_view(), name="lista_estudiantes"),
    path('facultades/', FacultadesView.as_view(), name="lista_facultades"),
]
