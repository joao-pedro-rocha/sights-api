from rest_framework.viewsets import ModelViewSet
from adresses.models import Adress
from .serializers import AdressSerializer


class AdressViewSet(ModelViewSet):
    """
    Ver e editar adresses
    """

    # A view conversa com o model. Todos os objetos sights são guardados na
    # variável queryset
    queryset = Adress.objects.all()
    # O serlializer possui os campos do models que serão exibidos no json
    serializer_class = AdressSerializer
