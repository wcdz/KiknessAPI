from django.http import HttpRequest
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.http.response import HttpResponse
from ..services import listados_auditoria_ingresos


class AuditoriaIngresosView(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request: HttpRequest, *args, **kwargs) -> HttpResponse:
        return super().dispatch(request, *args, **kwargs)

    # * En get solo necesito manejar la view de bd mas no la data en crudo
    def get(self, request):
        return listados_auditoria_ingresos(request)