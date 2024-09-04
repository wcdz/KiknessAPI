from ..models import NivelesAcademicos

def listado_niveles_academicos(request):
    niveles_academicos = list(NivelesAcademicos.objects.values())
    return niveles_academicos