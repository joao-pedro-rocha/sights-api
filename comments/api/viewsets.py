from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.authentication import TokenAuthentication
from comments.models import Comment
from .serializers import CommentSerializer


class CommentViewSet(ModelViewSet):
    """
    Ver e editar comments
    """

    # A view conversa com o model. Todos os objetos são guardados na
    # variável queryset
    queryset = Comment.objects.all()

    # O serlializer possui os campos do models que serão exibidos no json
    serializer_class = CommentSerializer
    
    # Permite que usuários não autenticados possam fazer GET, mas não permite
    # que façam ações como DELETE, PUT ou PATCH
    permission_classes = (IsAuthenticatedOrReadOnly,)
    authentication_classes = (TokenAuthentication,)
