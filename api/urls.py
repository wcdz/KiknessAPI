from django.urls import path, include
from rest_framework import routers
from api import controllers
from .controllers import EstudiantesView

urlpatterns = [
    path('estudiantes/', EstudiantesView.as_view(), name="lista_estudiantes"),
]
