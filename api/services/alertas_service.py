from django.db.models import Q
from ..models import Alertas
from ..helpers import register_send_mails
import datetime as dt
import json
from ..models import ViewEstudiantes, Estudiantes
from ..helpers import cod_estudiante_exist


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

    # * Validar que se genera la alerta para generar la tabla intermedia de envio de alertas
    if nueva_alerta:
        register_send_mails(nueva_alerta)

    data = {
        "fecha_alerta": fecha_actual,
        "hora_alerta": hora_alerta,
        "foto_captura": foto_captura,
    }

    return data


def actualizar_alerta(request):
    rq = json.loads(request.body)
    id_alerta = request.GET.get("id_alerta")
    cod_estudiante = rq.get("cod_estudiante")
    detalle_alerta = rq.get("detalle_alerta")
    estado_alerta = rq.get("estado_alerta")

    estudiante_exists = cod_estudiante_exist(cod_estudiante)
    if not estudiante_exists:
        return {
            "status": False,
            "message": f"No existe un registro con codigo {cod_estudiante}",
        }

    # obtener el id de estudiante por el codigo de estudiante
    estudiante = Estudiantes.objects.get(cod_estudiante=cod_estudiante)
    alerta = Alertas.objects.get(id_alerta=id_alerta)

    # Actualizacion de la alerta
    alerta.id_estudiante = estudiante
    if detalle_alerta:
        alerta.detalle_alerta = detalle_alerta
    if isinstance(estado_alerta, int):
        alerta.estado_alerta = estado_alerta

    alerta.save()

    response = f"Alerta con id {id_alerta} actualizada"
    return response
