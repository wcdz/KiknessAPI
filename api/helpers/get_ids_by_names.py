from django.http import HttpRequest


def get_id_by_name_nivel_academico(name_nivel_academico):
    from ..services import listado_niveles_academicos

    niveles_academicos = listado_niveles_academicos("")
    niveles_dict = {
        nivel["nombre_nivel_academico"]: nivel["id_nivel_academico"]
        for nivel in niveles_academicos
    }
    return niveles_dict.get(name_nivel_academico, None)


def get_id_by_name_facultad(name_facultad):
    from ..services import listado_facultades

    facultades = listado_facultades("")
    facultad_dic = {
        nivel["nombre_facultad"]: nivel["id_facultad"] for nivel in facultades
    }
    return facultad_dic.get(name_facultad, None)


def get_id_by_ids_naf_name_especialidad(
    id_nivel_academico, id_facultad, name_especialidad
):
    from ..services import listado_especialidades

    request = HttpRequest()
    request.GET = {
        "nivel_academico": str(id_nivel_academico),
        "facultad": str(id_facultad),
    }

    especialidades = listado_especialidades(request)
    especialidades_dic = {
        nivel["nombre_especialidad"]: nivel["id_especialidad"]
        for nivel in especialidades
    }
    return especialidades_dic.get(name_especialidad, None)
