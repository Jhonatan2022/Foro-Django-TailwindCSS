"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# Importamos admin para poder usar el panel de administración
from django.contrib import admin

# Importamos path para poder usar las rutas
# Importamos include para poder incluir las rutas de las apps
from django.urls import path, include

urlpatterns = [

    # Incluimos las rutas del panel de administración de Django
    path('admin/', admin.site.urls),


    # Incluimos la ruta de __reload__ para poder recargar el servidor de desarrollo cuando se haga un cambio
    path("__reload__/", include("django_browser_reload.urls")),
]
