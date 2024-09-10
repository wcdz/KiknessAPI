from django.http import HttpRequest
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.http.response import HttpResponse
from ..services import listado_alertas, insertar_alerta
from django.http import JsonResponse


class AlertasView(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request: HttpRequest, *args, **kwargs) -> HttpResponse:
        return super().dispatch(request, *args, **kwargs)

    # * En get solo necesito manejar la view de bd mas no la data en crudo
    def get(self, request):
        _listado_alertas = listado_alertas(request)
        return JsonResponse(_listado_alertas, safe=False)

    def post(self, request):
        create_alerta = insertar_alerta(request)
        return JsonResponse(create_alerta, status=201, safe=False)
