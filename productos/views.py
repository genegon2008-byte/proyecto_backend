"""Vistas de la aplicacion productos."""

from django.http import JsonResponse

from .models import Producto


def lista_productos(request):
    """Devuelve en formato JSON todos los productos registrados."""
    productos = Producto.objects.values('id', 'nombre', 'precio', 'stock', 'disponible')
    return JsonResponse(
        {'total': productos.count(), 'productos': list(productos)},
        json_dumps_params={'indent': 2},
    )
