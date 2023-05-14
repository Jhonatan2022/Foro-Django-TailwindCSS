# Importamos admin para poder usar el panel de administración
from django.contrib import admin

# Importamos path para poder usar las rutas
# Importamos include para poder incluir las rutas de las apps
from django.urls import path, include

# Importamos settings para poder usar las variables de configuración
from django.conf import settings

# Importamos static para poder usar los archivos estáticos
from django.conf.urls.static import static
#--------------------------------------IMPORT LIBRARIES--------------------------------------#




#--------------------------------------URLS--------------------------------------
# Definimos las rutas
urlpatterns = [

    # Incluimos las rutas del panel de administración de Django
    path('admin/', admin.site.urls),


    # Incluimos la ruta de __reload__ para poder recargar el servidor de desarrollo cuando se haga un cambio
    path("__reload__/", include("django_browser_reload.urls")),
]
#--------------------------------------URLS--------------------------------------




#--------------------------------------URLS MEDIA--------------------------------------
# Indicamos la ruta de los archivos estáticos
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)