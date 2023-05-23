# Importamos serializers para poder usar los serializadores de Django Rest Framework
from rest_framework import serializers

# Importamos Blog y Comment para poder usar los modelos
from .models import Blog, Comment
#----------------------------IMPORT LIBRARIES-------------------------#




#--------------------------------------SERIALIZERS--------------------------------------
# Definimos el serializador de Comment 
class CommentSerializer(serializers.ModelSerializer):

    # Definimos el campo "user" del serializador de Comment
    # source: Indica el campo del modelo que queremos serializar
    # read_only: Indica que el campo no se puede modificar
    user = serializers.CharField(source='user.user_name', read_only=True)


    # Definimos los campos del serializador
    class Meta:

        # Definimos el modelo, que es el modelo de Comment
        model = Comment

        # Definimos los campos que queremos que tenga el serializador
        # Usamos __all__ para indicar que queremos todos los campos
        fields = "__all__"




# Definimos el serializador de Blog 
class BlogSerializer(serializers.ModelSerializer):

    # Definimos el campo "user" del serializador de Blog
    # source: Indica el campo del modelo que queremos serializar
    # read_only: Indica que el campo no se puede modificar
    user = serializers.CharField(source='user.user_name', read_only=True)

    # Definimos el campo "comments" del serializador de Blog
    # read_only: Indica que el campo no se puede modificar
    comments = serializers.SerializerMethodField(read_only=True)


    # Definimos los campos del serializador
    class Meta:

        # Definimos el modelo, que es el modelo de Blog
        model = Blog

        # Definimos los campos que queremos que tenga el serializador
        fields = '__all__'


    # Definimos la función get_comments que nos permite obtener los comentarios de un blog
    # Pasamos como parámetro el objeto que estamos serializando (obj)
    def get_comments(self, obj):

        # Obtenemos los comentarios del blog que estamos serializando
        comments = obj.comment_set.all()

        # Serializamos los comentarios del blog
        # many=True: Indica que estamos serializando varios comentarios
        serializer = CommentSerializer(comments, many=True)

        # Retornamos los comentarios serializados del blog
        return serializer.data
#--------------------------------------SERIALIZERS--------------------------------------