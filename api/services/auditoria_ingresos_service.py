from django.db.models import Q
from ..models import AuditoriaIngresos


def listados_auditoria_ingresos(request):
    fecha_inicio = request.GET.get("fecha_inicio", "").strip()
    fecha_fin = request.GET.get("fecha_fin", "").strip()

    filtros = Q()
    if fecha_inicio:
        filtros &= Q(fecha_ingreso__gte=fecha_inicio)
    if fecha_fin:
        filtros &= Q(fecha_ingreso__lte=fecha_fin)

    auditoria_ingresos = list(AuditoriaIngresos.objects.filter(filtros).values())
    return auditoria_ingresos


def insert_auditoria_ingreso(request):
    return request
