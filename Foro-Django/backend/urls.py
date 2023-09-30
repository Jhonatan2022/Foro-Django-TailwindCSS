from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


# Definimos las rutas
urlpatterns = [
    # Incluimos las rutas del panel de administración de Django
    path("admin/", admin.site.urls),
    # Incluimos las rutas de los usuarios
    path("users/", include("users.urls")),
    # Incluimos las rutas de los blogs
    path("blogs/", include("blogs.urls")),
]


# Indicamos la ruta de los archivos estáticos
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)