from django.http import HttpRequest


def cod_estudiante_exist(cod_estudiante):
    from ..services import listado_estudiantes

    request = HttpRequest()
    request.GET = {"cod_estudiante": str(cod_estudiante)}

    estudiante = listado_estudiantes(request)

    return bool(len(estudiante))
