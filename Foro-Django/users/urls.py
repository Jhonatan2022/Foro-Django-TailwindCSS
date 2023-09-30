from django.urls import path
from . import views


# ------------------------------URLS-----------------------------#
# Definimos las rutas de la app de usuarios
urlpatterns = [
    # Creamos la ruta del login de usuario
    path("login/", views.MyTokenObtainPairView.as_view()),
    # Creamos la ruta del registro de usuario
    path("register/", views.register),
    # Creamos la ruta para actualizar el perfil de usuario
    # No pasamos id porque el usuario que se va a actualizar es el que está autenticado
    path("put/", views.putUser),
    # Creamos la ruta para poder actualizar la imagen de perfil de usuario
    # No pasamos id porque el usuario que se va a actualizar es el que está autenticado
    path("image/", views.uploadImage),
    # Creamos la ruta para obtener el perfil de usuario
    path("userProfile/", views.getUserProfile),
    # Creamos la ruta para obtener un solo usuario
    path("soloUser/<int:pk>/", views.getSoloUser),
    # Creamos la ruta para obtener todos los usuarios
    path("getUsers/", views.getUsers),
]
# ------------------------------URLS-----------------------------#
