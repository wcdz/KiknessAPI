from django.db.models import Q
from ..models import AuditoriaIngresos, Estudiantes
import json
import datetime as dt

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
    rq = json.loads(request.body)
    id_estudiante = rq.get("id_estudiante")
    fecha_ingreso = dt.date.today()
    hora_ingreso = dt.datetime.now().time().strftime("%H:%M:%S")
    
    estudiante = Estudiantes.objects.get(id_estudiante=id_estudiante)
    
    auditoria_ingreso = AuditoriaIngresos.objects.create(
        fecha_ingreso=fecha_ingreso,
        hora_ingreso=hora_ingreso,
        id_estudiante=estudiante
    )
    
    return {"status": True, "message": "Se registro un acceso"}
