from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import DjangoModelPermissions
from rest_framework.authentication import TokenAuthentication
from attractions.models import Attraction
from .serializers import AttractionSerializer


class AttractionViewSet(ModelViewSet):
    """
    Visualizar e editar attractions
    """
    
    # A view conversa com o model. Todos os objetos são guardados na
    # variável queryset
    queryset = Attraction.objects.all()

    # O serlializer possui os campos do models que serão exibidos no json
    serializer_class = AttractionSerializer

    # Utiliza as permissões dos usuário do Django Admin para realizar as ações
    # da API
    permission_classes = (DjangoModelPermissions,)
    authentication_classes = (TokenAuthentication,)
    
    # Facilita a criação de filtros por query string. Com isso o endpoint já 
    # captura a query string
    filterset_fields = ('name', 'description')
