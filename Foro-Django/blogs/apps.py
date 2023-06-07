# Importamos AppConfig para poder configurar la app
from django.apps import AppConfig



# Configuración de la app blogs
class BlogsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'blogs'
