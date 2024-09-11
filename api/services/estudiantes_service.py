from django.db.models import Q
from ..models import ViewEstudiantes, Estudiantes
from ..helpers import (
    get_id_by_name_nivel_academico,
    get_id_by_name_facultad,
    get_id_by_ids_naf_name_especialidad,
    cod_estudiante_exist,
)
import json


def listado_estudiantes(request):
    # Obtener todos los parámetros de la solicitud
    filtros = {
        "cod_estudiante__icontains": request.GET.get("cod_estudiante", "").strip(),
        "anio_ingreso__icontains": request.GET.get("anio_ingreso", "").strip(),
        "nombre_nivel_academico__icontains": request.GET.get(
            "nombre_nivel_academico", ""
        ).strip(),
        "nombre_facultad__icontains": request.GET.get("nombre_facultad", "").strip(),
        "nombre_especialidad__icontains": request.GET.get(
            "nombre_especialidad", ""
        ).strip(),
    }

    # Obtener el valor para el campo id_estudiante (numérico)
    id_estudiante = request.GET.get("id_estudiante", "").strip()

    # Crear el queryset base
    estudiantes = ViewEstudiantes.objects.filter(estado_estudiante="1")

    # Crear filtros OR para nombres y apellidos
    nombres_estudiante = request.GET.get("nombres_estudiante", "").strip()
    apellidos_estudiante = request.GET.get("nombres_estudiante", "").strip()

    if nombres_estudiante or apellidos_estudiante:
        q_objects = Q()
        if nombres_estudiante:
            q_objects |= Q(nombres_estudiante__icontains=nombres_estudiante)
        if apellidos_estudiante:
            q_objects |= Q(apellidos_estudiante__icontains=apellidos_estudiante)
        estudiantes = estudiantes.filter(q_objects)

    # Aplicar filtro para id_estudiante si es un número
    if id_estudiante.isdigit():
        estudiantes = estudiantes.filter(id_estudiante=id_estudiante)

    # Aplicar filtros restantes
    filtros_activos = {campo: valor for campo, valor in filtros.items() if valor}
    if filtros_activos:
        estudiantes = estudiantes.filter(**filtros_activos)

    # Convertir el queryset a una lista de diccionarios y devolver como JSON
    estudiantes_list = list(estudiantes.values())
    return estudiantes_list


def insertar_estudiante(request):
    rq = json.loads(request.body)
    cod_estudiante = rq.get("cod_estudiante")

    len_cod_estudiante = len(cod_estudiante)
    if len_cod_estudiante > 9 or len_cod_estudiante < 9:
        return {
            "status": False,
            "message": f"La longitud del codigo tiene que ser de 9 caracteres",
        }

    # * Validacion de que no exista un registro con el mismo codigo de estudiante
    estudiante_exists = cod_estudiante_exist(cod_estudiante)
    if estudiante_exists:
        return {
            "status": False,
            "message": f"Ya existe un registro con codigo {cod_estudiante}",
        }

    nombres_estudiante = rq.get("nombres_estudiante")
    apellidos_estudiante = rq.get("apellidos_estudiante")
    anio_ingreso = rq.get("anio_ingreso")
    perfil_estudiante = rq.get("perfil_estudiante")
    captura_biometrica = rq.get("captura_biometrica")
    nombre_nivel_academico = rq.get("nombre_nivel_academico")
    nombre_facultad = rq.get("nombre_facultad")
    nombre_especialidad = rq.get("nombre_especialidad")

    # * Aca usaremos los helpers
    id_nivel_academico = get_id_by_name_nivel_academico(nombre_nivel_academico)
    id_facultad = get_id_by_name_facultad(nombre_facultad)
    id_especialidad = get_id_by_ids_naf_name_especialidad(
        id_nivel_academico, id_facultad, nombre_especialidad
    )

    nuevo_estudiante = Estudiantes.objects.create(
        cod_estudiante=cod_estudiante,
        nombres_estudiante=nombres_estudiante,
        apellidos_estudiante=apellidos_estudiante,
        anio_ingreso=anio_ingreso,
        perfil_estudiante=perfil_estudiante,
        captura_biometrica=captura_biometrica,
        id_nivel_academico_id=id_nivel_academico,
        id_facultad_id=id_facultad,
        id_especialidad_id=id_especialidad,
    )

    _nuevo_estudiante = {
        "cod_estudiante": cod_estudiante,
        "nombres_estudiante": nombres_estudiante,
        "apellidos_estudiante": apellidos_estudiante,
        "anio_ingreso": anio_ingreso,
        "perfil_estudiante": perfil_estudiante,
        "captura_biometrica": captura_biometrica,
        "id_nivel_academico_id": id_nivel_academico,
        "id_facultad_id": id_facultad,
        "id_especialidad_id": id_especialidad,
    }

    return _nuevo_estudiante


def delete_estudiante(request):
    cod_estudiante = request.GET.get("cod_estudiante", "").strip()
    estudiante = Estudiantes.objects.get(cod_estudiante=cod_estudiante)
    estudiante.estado_estudiante = 0
    estudiante.save()
    response = {"message": f"Estudiante con codigo {cod_estudiante} desactivado"}

    return response
