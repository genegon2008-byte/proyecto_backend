from django.test import TestCase

from .models import Producto


class ProductoTestCase(TestCase):
    def test_creacion_producto(self):
        producto = Producto.objects.create(nombre='Teclado', precio=85000, stock=10)
        self.assertTrue(producto.disponible)
