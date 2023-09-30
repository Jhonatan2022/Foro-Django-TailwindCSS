from django.urls import path
from . import views


# --------------------------------------URLS--------------------------------------
# Definimos las rutas
urlpatterns = [
    # Incluimos la ruta para obtener todos los blogs o crear uno nuevo
    path("get/", views.getBlogs),
    # Incluimos la ruta para obtener un solo blog por medio del pk
    path("get/<int:pk>/", views.getSoloBlog),
    # Creamos la ruta para poder crear un blog nuevo
    path("post/", views.postBlog),
    # Creamos la ruta para poder editar un blog por medio del pk
    path("put/<int:pk>/", views.putBlog),
    # Creamos la ruta para poder eliminar un blog por medio del pk
    path("delete/<int:pk>/", views.deleteBlog),
    # Creamos la ruta para poder comentar un blog por medio del pk
    path("comment/<int:pk>/", views.comment),
]
# --------------------------------------URLS--------------------------------------
