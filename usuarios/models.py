"""Modelos de la aplicacion usuarios."""

from django.db import models


class Usuario(models.Model):
    """Representa a un usuario registrado en el sistema."""

    nombre = models.CharField(max_length=100)
    correo = models.EmailField(unique=True)
    telefono = models.CharField(max_length=20, blank=True)
    activo = models.BooleanField(default=True)
    fecha_registro = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'
        ordering = ['nombre']

    def __str__(self):
        return f'{self.nombre} ({self.correo})'
