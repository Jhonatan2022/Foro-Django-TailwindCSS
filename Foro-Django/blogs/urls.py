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
    path('get/<int:pk>/', views.getSoloBlog),
    path('post/', views.postBlog),
    path('put/<int:pk>/', views.putBlog),
    path('delete/<int:pk>/', views.deleteBlog),
    path('comment/<int:pk>/', views.comment),
]
#--------------------------------------URLS--------------------------------------