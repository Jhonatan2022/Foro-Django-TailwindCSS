# Importamos path para poder usar las rutas
from django.urls import path

# Importamos las vistas de usuarios
from users import views
#--------------------------------------IMPORT LIBRARIES--------------------------------------#




#--------------------------------------RUTAS--------------------------------------
# Definimos las rutas
urlpatterns = [

    # Creamos la ruta del login de usuario
    path('login/', views.MyTokenObtainPairView.as_view()),


    # Creamos la ruta del registro de usuario
    path('register/', views.register),

]