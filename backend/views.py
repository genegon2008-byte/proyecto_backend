"""Vista de bienvenida del backend."""

from django.http import JsonResponse


def inicio(request):
    """Devuelve un JSON con el estado del backend y sus rutas disponibles."""
    return JsonResponse({
        'proyecto': 'backend',
        'estado': 'en ejecucion',
        'aplicaciones': ['usuarios', 'productos'],
        'rutas': {
            'admin': '/admin/',
            'usuarios': '/api/usuarios/',
            'productos': '/api/productos/',
        },
    }, json_dumps_params={'indent': 2})
