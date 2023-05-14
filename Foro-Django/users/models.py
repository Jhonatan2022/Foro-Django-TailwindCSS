# Importamos models para poder usar los modelos de la base de datos
from django.db import models

# Importamos timezone para poder usar la zona horaria de la base de datos
from django.utils import timezone

# Importamos gettext_lazy para poder usar los textos en varios idiomas de la base de datos
from django.utils.translation import gettext_lazy as _ # Le asignamos un alias para poder usarlo más fácilmente

# Importamos AbstractBaseUser para poder usar el modelo de usuario personalizado
# Importamos BaseUserManager para poder usar el modelo de usuario personalizado
# Importamos PermissionsMixin para poder usar el modelo de usuario personalizado
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
#--------------------------------------IMPORT LIBRARIES--------------------------------------#




#--------------------------------------MODELS--------------------------------------
# Creamos una clase CustomAccountManager que hereda de BaseUserManager para poder crear usuarios y superusuarios
class CustomAccountManager(BaseUserManager):

    # Creamos una variable que nos permite crear usuarios
    # Definimos los campos que queremos que tenga el usuario
    # **other_fields nos permite añadir más campos si queremos
    def create_user(self, email, user_name, first_name, password, **other_fields):

        # Si no se ha introducido el email, lanzamos un error
        if not email:

            # Raise nos permite lanzar un error si no se cumple la condición
            raise ValueError(_('Debes introducir un email válido'))
        
        # Normalizamos el email para que sea todo en minúsculas
        email = self.normalize_email(email)

        # Creamos un objeto usuario
        user = self.model(email=email, user_name=user_name, first_name=first_name, **other_fields)

        # Establecemos la contraseña
        user.set_password(password)

        # Guardamos el usuario
        user.save()

        # Devolvemos el usuario
        return user
    

    # Creamos una variable que nos permite crear superusuarios
    # Definimos los campos que queremos que tenga el superusuario
    # **other_fields nos permite añadir más campos si queremos
    def create_superuser(self, email, user_name, first_name, password, **other_fields):

        # Establecemos que el superusuario tiene que tener el campo is_staff a True
        # is_staff nos permite acceder al panel de administración
        other_fields.setdefault('is_staff', True)

        # Establecemos que el superusuario tiene que tener el campo is_superuser a True
        # is_superuser nos permite acceder al panel de administración
        other_fields.setdefault('is_superuser', True)

        # Establecemos que el superusuario tiene que tener el campo is_active a True
        # is_active nos permite acceder al panel de administración
        other_fields.setdefault('is_active', True)

        # Si el superusuario no tiene el campo is_staff a True, lanzamos un error
        if other_fields.get('is_staff') is not True:

            # Raise nos permite lanzar un error si no se cumple la condición
            raise ValueError(_('El superusuario debe tener is_staff=True'))
        
        # Si el superusuario no tiene el campo is_superuser a True, lanzamos un error
        if other_fields.get('is_superuser') is not True:

            # Raise nos permite lanzar un error si no se cumple la condición
            raise ValueError(_('El superusuario debe tener is_superuser=True'))
        
        # Retornamos el usuario
        return self.create_user(email, user_name, first_name, password, **other_fields)
    



# Creamos una clase User que hereda de AbstractBaseUser y PermissionsMixin para poder crear un modelo de usuario personalizado
class User(AbstractBaseUser, PermissionsMixin):


    # Definimos el campo de email que es único y no puede estar vacío
    # unique nos permite definir que el campo es único
    # EmailField nos permite definir que el campo es un email
    email = models.EmailField(_('email address'), unique=True)


    # Definimos el campo de user_name que es único y no puede estar vacío
    # unique nos permite definir que el campo es único
    # max_length nos permite definir la longitud máxima del campo
    user_name = models.CharField(max_length=150, unique=True)


    # Definimos el campo de first_name que no puede estar vacío
    # max_length nos permite definir la longitud máxima del campo
    first_name = models.CharField(max_length=150)

