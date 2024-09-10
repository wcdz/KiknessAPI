from ..models import EnvioAlertas, Usuarios


def register_send_mails(nueva_alerta):
    from ..services import listado_usuarios

    usuarios = listado_usuarios("")
    ids_usuarios = [usuario["id_usuario"] for usuario in usuarios]

    for id_usuario in ids_usuarios:
        usuario_instance = Usuarios.objects.get(id_usuario=id_usuario)
        EnvioAlertas.objects.create(id_alerta=nueva_alerta, id_usuario=usuario_instance)

    return "envio_alertas_send"
