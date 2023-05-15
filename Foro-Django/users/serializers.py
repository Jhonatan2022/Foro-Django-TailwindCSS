# Importamos serializers para poder usar los serializadores de Django REST Framework
from rest_framework import serializers

# Importamos RefreshToken para poder usar los tokens de Django REST Framework
from rest_framework_simplejwt.tokens import RefreshToken

# Importamos User para poder usar el modelo de usuario de Django
from django.contrib.auth.models import User
#--------------------------------------IMPORT LIBRARIES--------------------------------------#




#--------------------------------------SERIALIZERS--------------------------------------
# Definimos el serializador de usuario
class UserSerializer(serializers.ModelSerializer):

    # Definismo si el usuario es administrador
    # read_only=True: Indica que el campo no se puede modificar
    is_admin = serializers.SerializerMethodField(read_only=True)


    # Definimos los campos del serializador
    class Meta:

        # Definimos el modelo, que es el modelo de usuario de Django
        model = User

        # Definimos los campos que queremos que tenga el serializador
        fields = [

            # Indicamos el campo "id" del modelo
            "id",

            # Indicamos el campo "username" del modelo
            "user_name",

            # Indicamos el campo "email" del modelo
            "email",

            # Indicamos el campo "is_admin" del serializador
            "is_admin",

            # Indicamos el campo de bio
            "bio",

            # Indicamos el campo de avatar
            "avatar",

            # Indicamos el campo de first_name
            "first_name",
        ]


    # Definimos la función que nos indica si el usuario es administrador
    # obj: Es el objeto que se está serializando
    def get_is_admin(self, obj):

        # Devolvemos si el usuario es administrador
        return obj.is_staff




# Definimos el serializador de registro de usuario (certificación de usuario)
class UserSerializerWithToken (UserSerializer):

    # Incluimos el token de usuario
    # read_only=True: Indica que el campo no se puede modificar
    token = serializers.SerializerMethodField(read_only=True)


    # Definimos los campos del serializador
    class Meta:

        model = User

        fields = [

            # Indicamos el campo "id" del modelo
            "id",

            # Indicamos el campo "username" del modelo
            "user_name",

            # Indicamos el campo "email" del modelo
            "email",

            # Indicamos el campo "is_admin" del serializador
            "is_admin",

            # Indicamos el campo de bio
            "bio",

            # Indicamos el campo de avatar
            "avatar",

            # Indicamos el campo de first_name
            "first_name",

            # Indicamos el campo de token
            "token",
        ]


    # Definimos la función que nos indica el token de usuario
    # obj: Es el objeto que se está serializando
    def get_token(self, obj):

        # Definimos el token de usuario
        token = RefreshToken.for_user(obj)

        # Devolvemos el token de usuario
        # Convertimos el token a string para poder devolverlo en el serializador
        return str(token.access_token)
#--------------------------------------SERIALIZERS--------------------------------------