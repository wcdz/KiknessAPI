from ..models import Usuarios

def listado_usuarios(request):
    usuarios = list(Usuarios.objects.values())
    return usuarios