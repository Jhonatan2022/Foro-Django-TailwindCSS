# Importamos serializers para poder usar los serializers de Django Rest Framework
from rest_framework import serializers

# Importamos api_view para poder usar las vistas de Django Rest Framework
# Importamos permission_classes para poder usar los permisos de Django Rest Framework
from rest_framework.decorators import api_view, permission_classes

# Importamos IsAuthenticated para poder usar el permiso de autenticación de Django Rest Framework
from rest_framework.permissions import IsAuthenticated

# Importamos Response para poder usar las respuestas de Django Rest Framework
from rest_framework.response import Response

# Importamos status para poder usar los códigos de estado de Django Rest Framework
from rest_framework import status

# Importamos BlogSerializer para poder usar el serializer de Blog
from .serializers import BlogSerializer

# Importamos los modelos de Blog y Comment para poder usarlos
from .models import Blog, Comment

# Importamos User para poder usar el modelo de usuario
from users.models import User
#----------------------------IMPORT LIBRARIES-------------------------#




#--------------------------------------VIEWS--------------------------------------
# Creamos la vista para obtener todos los blogs
# Pasamos is_authenticated para que solo los usuarios autenticados puedan ver los blogs
@api_view(['GET'])
@permission_classes([IsAuthenticated])

# Creamos la función getBlogs
def getBlogs(request):

    # Filtramos los blogs y los ordenamos por fecha de creación
    # -date para ordenarlos de más reciente a más antiguo
    blog = Blog.objects.filter().order_by('-date')

    # Creamos el serializer de Blog y le pasamos los blogs
    # many=True para que pueda serializar varios blogs
    serializer = BlogSerializer(blog, many=True)

    # Retornamos el serializer con los blogs
    return Response(serializer.data)




# Creamos la vista para obtener los blogs de un usuario
# Pasamos is_authenticated para que solo los usuarios autenticados puedan ver los blogs
@api_view(['GET'])
@permission_classes([IsAuthenticated])

# Creamos la función getBlogsUser y le pasamos el request y el pk del usuario
def getSoloBlog(request, pk):

    # Obtenemos los blogs del usuario por medio del pk
    blog = Blog.objects.get(id=pk)

    # Creamos el serializer de Blog y le pasamos el blog
    # many=False para que pueda serializar un solo blog
    serializer = BlogSerializer(blog, many=False)

    # Retornamos el serializer con el blog del usuario
    return Response(serializer.data)




# Creamos la vista para poder crear un blog nuevo
# Pasamos is_authenticated para que solo los usuarios autenticados puedan ver los blogs
@api_view(['POST'])
@permission_classes([IsAuthenticated])

# Creamos la función postBlog y le pasamos el request del usuario
def postBlog(request):

    # Obtenemos los datos del request del usuario
    data = request.data

    # Creamos el blog y le pasamos los datos del request del usuario
    blog = Blog.objects.create(

        # Obtenemos el usuario que está creando el blog
        user = request.user,

        # Obtenemos el título del blog
        body = data['body'],
    )

    # Creamos el serializer de Blog y le pasamos el blog
    # many=False para que pueda serializar un solo blog
    serializer = BlogSerializer(blog, many=False)

    # Retornamos el serializer con el blog creado
    return Response(serializer.data)




# Creamos la vista para poder editar un blog nuevo
# Pasamos is_authenticated para que solo los usuarios autenticados puedan ver los blogs
# Usamos el método PUT para editar el blog
@api_view(['PUT'])
@permission_classes([IsAuthenticated])

# Creamos la función putBlog y le pasamos el request del usuario y el pk del blog
def putBlog(request, pk):

    # Obtenemos los datos del request del usuario
    data = request.data

    # Obtenemos el blog por medio del pk
    blog = Blog.objects.get(id=pk)

    # Creamos el serializer de Blog y le pasamos el blog y los datos del request del usuario
    serializer = BlogSerializer(instance=blog, data=data)

    # Verificamos si el usuario que está editando el blog es el mismo que lo creó
    if blog.user == request.user:

        # Verificamos si el serializer es válido
        if serializer.is_valid():

            # Guardamos el serializer
            serializer.save()
    # Si el usuario que está editando el blog no es el mismo que lo creó
    else:

        # Retornamos un error de no autorizado
        return Response({'Error': 'Unauthorized'}, status=status.HTTP_401_UNAUTHORIZED)
    
    # Retornamos el serializer con el blog editado
    return Response(serializer.data)





# Creamos la vista para poder eliminar un blog
# Pasamos is_authenticated para que solo los usuarios autenticados puedan ver los blogs
# Usamos el método DELETE para eliminar el blog
@api_view(['DELETE'])
@permission_classes([IsAuthenticated])

# Creamos la función deleteBlog y le pasamos el request del usuario y el pk del blog
def deleteBlog(request, pk):

    # Obtenemos el blog por medio del pk
    blog = Blog.objects.get(id=pk)

    # Verificamos si el usuario que está eliminando el blog es el mismo que lo creó
    if blog.user == request.user:

        # Eliminamos el blog
        blog.delete()

        # Retornamos un mensaje de blog eliminado
        return Response('Blog Eliminado')
    
    # Si el usuario que está eliminando el blog no es el mismo que lo creó
    else:

        # Retornamos un error de no autorizado
        return Response({'Error': 'Unauthorized'}, status=status.HTTP_401_UNAUTHORIZED)




# Creamos la vista para poder comentar un blog
# Pasamos is_authenticated para que solo los usuarios autenticados puedan ver los blogs
# Usamos el método POST para comentar el blog
@api_view(['POST'])
@permission_classes([IsAuthenticated])

# Creamos la función comment y le pasamos el request del usuario y el pk del blog
def comment(request, pk):

    # Obtenemos el blog por medio del pk del blog
    blog = Blog.objects.get(id=pk)

    # Obtenemos el usuario que está comentando el blog
    user = request.user

    # Obtenemos los datos del request del usuario
    data = request.data

    # Creamos el comentario y le pasamos el usuario, el blog y el texto del comentario
    comment = Comment.objects.create(
        user = user,
        blog = blog,
        text = data['text']
    )

    # Obtenemos todos los comentarios del blog
    comments = blog.comment_set.all()

    # Guardamos el blog
    blog.save()

    # Retornamos un mensaje de comentario agregado
    return Response('Comment added!!')
#--------------------------------------VIEWS--------------------------------------