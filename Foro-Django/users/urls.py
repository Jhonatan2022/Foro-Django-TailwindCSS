# Importamos path para poder usar las rutas
from django.urls import path

# Importamos las vistas de usuarios
from . import views
#--------------------------------------IMPORT LIBRARIES--------------------------------------#




#--------------------------------------URLS--------------------------------------#
# Definimos las rutas de la app de usuarios
urlpatterns = [

    # Creamos la ruta del login de usuario
    path('login/', views.MyTokenObtainPairView.as_view()),


    # Creamos la ruta del registro de usuario
    path('register/', views.register),
    
]