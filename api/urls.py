from django.urls import path, include
from rest_framework import routers
from api import controllers
from .controllers import EstudiantesView, FacultadesView, NivelesAcademicosView, EspecialidadesView, AuditoriaIngresosView, UsuariosView

urlpatterns = [
    path('estudiantes/', EstudiantesView.as_view(), name="lista_estudiantes"),
    path('facultades/', FacultadesView.as_view(), name="lista_facultades"),
    path('niveles_academicos/', NivelesAcademicosView.as_view(), name="lista_niveles_academicos"),
    path('especialidades/', EspecialidadesView.as_view(), name="lista_especialidades"),
    path('auditoria_ingresos/', AuditoriaIngresosView.as_view(), name="lista_auditoria_ingresos"),
    path('usuarios/', UsuariosView.as_view(), name="lista_usuarios"),
]
