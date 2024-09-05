from django.http import HttpRequest
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.http.response import HttpResponse
from ..services import listado_estudiantes, insertar_estudiante
from django.http.response import JsonResponse


class EstudiantesView(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request: HttpRequest, *args, **kwargs) -> HttpResponse:
        return super().dispatch(request, *args, **kwargs)

    # * En get solo necesito manejar la view de bd mas no la data en crudo
    def get(self, request):
        _listado_estudiantes = listado_estudiantes(request)
        return JsonResponse(_listado_estudiantes, safe=False)

    # * En post si que requiero
    def post(self, request):
        create_estudiante = insertar_estudiante(request)
        return JsonResponse(create_estudiante, status=201, safe=False)
