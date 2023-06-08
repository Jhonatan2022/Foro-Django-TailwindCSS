# Importaciones necesarias para la configuración de la app users
from django.apps import AppConfig



# Configuración de la app users
class UsersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'users'
