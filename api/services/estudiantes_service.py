from ..models import ViewEstudiantes, Estudiantes
from django.db.models import Q
from django.http.response import JsonResponse

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

    # Obtener los valores para los campos que requieren OR
    nombres_estudiante = request.GET.get("nombres_estudiante", "").strip()
    apellidos_estudiante = request.GET.get("nombres_estudiante", "").strip()

    # Crear el queryset base
    estudiantes = ViewEstudiantes.objects.filter(estado_estudiante="1")

    # Crear filtros OR para nombres y apellidos
    if nombres_estudiante or apellidos_estudiante:
        q_objects = Q()
        if nombres_estudiante:
            q_objects |= Q(nombres_estudiante__icontains=nombres_estudiante)
        if apellidos_estudiante:
            q_objects |= Q(apellidos_estudiante__icontains=apellidos_estudiante)
        estudiantes = estudiantes.filter(q_objects)

    # Aplicar filtros restantes
    filtros_activos = {campo: valor for campo, valor in filtros.items() if valor}
    if filtros_activos:
        estudiantes = estudiantes.filter(**filtros_activos)

    # Convertir el queryset a una lista de diccionarios y devolver como JSON
    estudiantes_list = list(estudiantes.values())
    return JsonResponse(estudiantes_list, safe=False)
