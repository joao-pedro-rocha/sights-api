from rest_framework.viewsets import ModelViewSet
from reviews.models import Review
from .serializers import ReviewSerializer


class ReviewViewSet(ModelViewSet):
    """
    Ver e editar reviews
    """

    # A view conversa com o model. Todos os objetos são guardados na
    # variável queryset
    queryset = Review.objects.all()
    # O serlializer possui os campos do models que serão exibidos no json
    serializer_class = ReviewSerializer
