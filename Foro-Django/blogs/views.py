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
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getBlogs(request):
    blog = Blog.objects.filter().order_by('-date')
    serializer = BlogSerializer(blog, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getSoloBlog(request, pk):
    blog = Blog.objects.get(id=pk)
    serializer = BlogSerializer(blog, many=False)
    return Response(serializer.data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def postBlog(request):
    data = request.data
    blog = Blog.objects.create(
        user = request.user,
        body = data['body'],
    )
    serializer = BlogSerializer(blog, many=False)
    return Response(serializer.data)


@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def putBlog(request, pk):
    data = request.data
    blog = Blog.objects.get(id=pk)
    serializer = BlogSerializer(instance=blog, data=data)
    if blog.user == request.user:
        if serializer.is_valid():
            serializer.save()
    else:
        return Response({'Error': 'Unauthorized'}, status=status.HTTP_401_UNAUTHORIZED)
    return Response(serializer.data)


@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def deleteBlog(request, pk):
    blog = Blog.objects.get(id=pk)
    if blog.user == request.user:
        blog.delete()
        return Response('Blog Eliminado')
    else:
        return Response({'Error': 'Unauthorized'}, status=status.HTTP_401_UNAUTHORIZED)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def comment(request, pk):
    blog = Blog.objects.get(id=pk)
    user = request.user
    data = request.data
    comment = Comment.objects.create(
        user = user,
        blog = blog,
        text = data['text']
    )
    comments = blog.comment_set.all()
    blog.save()
    return Response('Comment added!!')

































