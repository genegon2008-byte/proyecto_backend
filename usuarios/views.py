"""Vistas de la aplicacion usuarios."""

from django.http import JsonResponse

from .models import Usuario


def lista_usuarios(request):
    """Devuelve en formato JSON todos los usuarios registrados."""
    usuarios = Usuario.objects.values('id', 'nombre', 'correo', 'activo')
    return JsonResponse(
        {'total': usuarios.count(), 'usuarios': list(usuarios)},
        json_dumps_params={'indent': 2},
    )
