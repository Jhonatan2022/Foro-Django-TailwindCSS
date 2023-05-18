# Importamos serializers para poder usar los serializadores
from rest_framework import serializers

# Importamos api_view para poder usar las vistas de Django REST Framework
# Importamos permission_classes para poder usar los permisos de Django REST Framework
from rest_framework.decorators import api_view, permission_classes

# Importamos is_authenticated para poder usar la función que nos indica si el usuario está autenticado
from rest_framework.permissions import IsAuthenticated

# Importamos Response para poder usar las respuestas de Django REST Framework
from rest_framework.response import Response

# Importamos make_password para poder usar la función que nos permite encriptar contraseñas
from django.contrib.auth.hashers import make_password

# Importamso status para poder usar los códigos de estado de HTTP
from rest_framework import status

# Importamos tokenobtainpairserializer para poder usar el serializador de tokens de Django REST Framework
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

# Importamos tokenobtainpairview para poder usar la vista de tokens de Django REST Framework
from rest_framework_simplejwt.views import TokenObtainPairView

# Importamos nuestro modelo de usuario
from .models import User

# Importamos nuestro serializador de usuario y de usuario con token
from .serializers import  UserSerializer, UserSerializerWithToken
#--------------------------------------IMPORT LIBRARIES--------------------------------------#




#--------------------------------------VIEWS--------------------------------------
# Creamos la vista de login de usuario
class MyTokenObtainPairSerializer(TokenObtainPairSerializer):

    # Creamos una funsión que nos permite sobreescribir la función de validación de datos
    def validate(self, attrs):

        # Creamos una variable que almacena el valor de la función validate de la clase padre
        data = super().validate(attrs)

        # Creamos una variable que almacena el valor del usuario
        serializers = UserSerializerWithToken(self.user).data


        # Creamos un bucle que recorre el token y el usuario
        for token, user in serializers.items():

            # Añadimos el token y el usuario a la variable data
            data[token] = user

        # Devolvemos la variable data
        return data




# Creamos la vista para obtener el usuario autenticado
class MyTokenObtainPairView(TokenObtainPairView):

    # Definimos el serializador de la vista de tokens, que es el que hemos creado
    serializer_class = MyTokenObtainPairSerializer




# Creamos la vista para poder registrar usuarios
@api_view(['POST'])
def register(request):

    # Creamos una variable que almacena el valor de la función data
    data = request.data

    # Creamos una variable que almacena el valor del usuario
    try:

        # Creamos una variable que almacena el valor del usuario
        user = User.objects.create(

            # Definimos el nombre de usuario
            user_name = data['user_name'],

            # Definimos el correo electrónico
            email = data['email'],

            # Definimos la contraseña
            # Make_password nos permite encriptar la contraseña
            password = make_password(data['password'])
        )

        # Creamos una variable que almacena el valor del serializador de usuario
        # many=False indica que solo se va a serializar un objeto
        serializer = UserSerializerWithToken(user, many=False)

        # Devolvemos la variable serializer
        return Response(serializer.data)

    # Si no se puede crear el usuario
    except:

        # Creamos una variable que almacena el valor del mensaje de error
        message = {'detail': 'User with this email already exists'}

        # Devolvemos la variable message y el código de estado
        # http_400_bad_request indica que la solicitud no se pudo procesar debido a un error del cliente
        return Response(message, status=status.HTTP_400_BAD_REQUEST)