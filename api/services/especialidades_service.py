from ..models import Especialidades

""" Una condicion de la especialidad es que siempre se tendra que filtrar por ambos queryparams 
    - nivel_academico
    - facultad
"""


def listado_especialidades(request):
    nivel_academico = request.GET.get("nivel_academico", "").strip()
    facultad = request.GET.get("facultad", "").strip()

    # Asegurarse de que ambos parámetros estén presentes
    if nivel_academico and facultad:
        especialidades = list(
            Especialidades.objects.filter(
                id_facultad=facultad, id_nivel_academico=nivel_academico
            ).values()
        )
    else:
        especialidades = []

    return especialidades
