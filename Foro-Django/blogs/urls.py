# Importamos path para las rutas y 
from django.urls import path

# Importamos views para las funciones que se ejecutaran en cada ruta
from . import views
#----------------------------IMPORT LIBRARIES-------------------------#




#--------------------------------------URLS--------------------------------------
# Definimos las rutas
urlpatterns = [


    # Incluimos la ruta para obtener todos los blogs o crear uno nuevo
    path('get/', views.getBlogs),


    # Incluimos la ruta para obtener un solo blog por medio del pk
    path('get/<int:pk>/', views.getSoloBlog),

 
    # Creamos la ruta para poder crear un blog nuevo
    path('post/', views.postBlog),


    # Creamos la ruta para poder editar un blog por medio del pk
    path('put/<int:pk>/', views.putBlog),
    path('delete/<int:pk>/', views.deleteBlog),
    path('comment/<int:pk>/', views.comment),
]
#--------------------------------------URLS--------------------------------------