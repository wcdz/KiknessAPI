
from ..models import Facultades

def listado_facultades(request):
    facultades = list(Facultades.objects.values())
    return facultades