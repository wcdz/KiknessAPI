from django.http import HttpRequest
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.http.response import HttpResponse
from django.http.response import JsonResponse
from ..services import listado_usuarios


class UsuariosView(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request: HttpRequest, *args, **kwargs) -> HttpResponse:
        return super().dispatch(request, *args, **kwargs)

    def get(self, request):
        _listado_usuarios = listado_usuarios(request)
        return JsonResponse(_listado_usuarios, safe=False)
