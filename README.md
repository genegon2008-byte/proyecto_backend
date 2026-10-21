# Backend con Django

Proyecto backend desarrollado con **Python**, **Django** y **entornos virtuales**.

## Contenido

- Proyecto Django: `backend`
- Aplicaciones: `usuarios` y `productos`

## Instalacion y ejecucion

```bash
# 1. Clonar el repositorio
git clone <URL-DEL-REPOSITORIO>
cd proyecto_backend

# 2. Crear el entorno virtual
python -m venv env

# 3. Activar el entorno virtual
env\Scripts\activate        # Windows
source env/bin/activate     # Linux / macOS

# 4. Instalar las dependencias
pip install -r requirements.txt

# 5. Aplicar las migraciones
python manage.py makemigrations
python manage.py migrate

# 6. Ejecutar el servidor
python manage.py runserver
```

El backend queda disponible en `http://127.0.0.1:8000/`

## Rutas disponibles

| Ruta | Descripcion |
|---|---|
| `/` | Estado del backend (JSON) |
| `/admin/` | Panel de administracion de Django |
| `/api/usuarios/` | Listado de usuarios (JSON) |
| `/api/productos/` | Listado de productos (JSON) |
