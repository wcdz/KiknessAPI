from django.http.response import JsonResponse
from ..models import NivelesAcademicos

def listado_niveles_academicos(request):
    niveles_academicos = list(NivelesAcademicos.objects.values())
    return JsonResponse(niveles_academicos, safe=False)