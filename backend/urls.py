"""Rutas principales (URLconf raiz) del proyecto backend."""

from django.contrib import admin
from django.urls import path, include

from .views import inicio

urlpatterns = [
    path('', inicio, name='inicio'),
    path('admin/', admin.site.urls),
    path('api/usuarios/', include('usuarios.urls')),
    path('api/productos/', include('productos.urls')),
]
