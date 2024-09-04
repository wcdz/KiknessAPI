from django.http.response import JsonResponse
from ..models import AuditoriaIngresos


def listado_auditoria_ingresos(request):
    fecha_inicio = request.GET.get("fecha_inicio", "").strip()
    fecha_fin = request.GET.get("fecha_fin", "").strip()
    
    ingresos = AuditoriaIngresos.objects.all()

    if fecha_inicio and fecha_fin:
        ingresos = ingresos.filter(fecha_ingreso__range=[fecha_inicio, fecha_fin])
    elif fecha_inicio:
        ingresos = ingresos.filter(fecha_ingreso__gte=fecha_inicio)
    elif fecha_fin:
        ingresos = ingresos.filter(fecha_ingreso__lte=fecha_fin)

    # Convertir el queryset a una lista de diccionarios y devolver como JSON
    ingresos_list = list(ingresos.values())
    return JsonResponse(ingresos_list, safe=False)
