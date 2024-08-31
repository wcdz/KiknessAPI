from django.http.response import JsonResponse
from ..models import Facultades

def listado_facultades(request):
    facultades = list(Facultades.objects.values())
    return JsonResponse(facultades, safe=False)