from django.http import JsonResponse
from django.db.models import Q
from ..models import Alertas

def listado_alertas(request):
    estado = request.GET.get("estado", "").strip()
    fecha_inicio = request.GET.get("fecha_inicio", "").strip()
    fecha_fin = request.GET.get("fecha_fin", "").strip()
    
    alertas = Alertas.objects.all()
    
    if estado: 
        alertas = alertas.filter(estado_alerta=estado)

    filtros = Q()
    if fecha_inicio:
        filtros &= Q(fecha_alerta__gte=fecha_inicio)
    if fecha_fin:
        filtros &= Q(fecha_alerta__lte=fecha_fin)
        
    alertas = list(alertas.filter(filtros).values())
    
    return JsonResponse(alertas, safe=False)
