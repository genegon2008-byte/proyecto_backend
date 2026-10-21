from django.test import TestCase

from .models import Usuario


class UsuarioTestCase(TestCase):
    def test_creacion_usuario(self):
        usuario = Usuario.objects.create(nombre='Ana Gomez', correo='ana@correo.com')
        self.assertTrue(usuario.activo)
