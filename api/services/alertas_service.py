from django.db.models import Q
from ..models import Alertas
import datetime as dt


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

    return alertas


def insertar_alerta(request):
    fecha_actual = dt.date.today()
    hora_actual = dt.datetime.now().time()
    hora_alerta = hora_actual.strftime("%H:%M:%S")
    foto_captura = (
        f"alerta_{fecha_actual.strftime('%Y%m%d')}_{hora_actual.strftime('%H%M%S')}"
    )

    nueva_alerta = Alertas.objects.create(
        fecha_alerta=fecha_actual, hora_alerta=hora_alerta, foto_captura=foto_captura
    )

    data = {
        "fecha_alerta": fecha_actual,
        "hora_alerta": hora_alerta,
        "foto_captura": foto_captura,
    }

    return data
