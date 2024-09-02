from django.http.response import JsonResponse
from ..models import Alertas


def listado_alertas(request):
    alertas = list(Alertas.objects.values())
    return JsonResponse(alertas, safe=False)
