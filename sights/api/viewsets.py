from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import filters
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.authentication import TokenAuthentication
from sights.models import Sight
from .serializers import SightSerializer


class SightViewSet(ModelViewSet):
    """
    View para ver e editar apenas Sights aprovados
    """

    # O serlializer possui os campos do models que serão exibidos no json
    serializer_class = SightSerializer
    
    # Permissão apenas para admins
    permission_classes = (IsAdminUser,)
    authentication_classes = (TokenAuthentication,)
    
    # Fazer buscas em determinados campos
    filter_backends = [filters.SearchFilter]

    # Também é possível fazer buscas por fk, como no caso de adress, que é 
    # um campo de Sight com uma chave estrangeira para Adress
    search_fields = ('name', 'description', 'adress__line_1',)

    # Permite que seja feita uma busca pelo campo desejado no lugar do id do 
    # objeto. Mas se houver mais objetos com o mesmo valor no campo determinado 
    # levantará um erro 
    # lookup_field = 'name'

    # get_queryset serve para filtragens especificas de objetos
    def get_queryset(self):
        # Usando filtro por query parameter:
        # http://127.0.0.1:8000/sights/?description=fasfdaSfafS
        # É possível passar um ou todos os parâmetros
        id = self.request.query_params.get('id', None)
        name = self.request.query_params.get('name', None)
        description = self.request.query_params.get('description', None)
        queryset = Sight.objects.all()

        if id:
            queryset = Sight.objects.filter(pk=id)
        if name:
            queryset = queryset.filter(name__iexact=name)
        if description:
            queryset = queryset.filter(description__iexact=description)
        return queryset
    
    # É possível sobrescrever os métodos, que são reponsáveis pelos verbos 
    # http do endpoint. Com isso é possível fazer uma série de operações,
    # cálculos e validações

    # list() retorna um endpoint como um todo, uma lista de recursos
    def list(self, request, *args, **kwargs):
        return super(SightViewSet, self).list(request, *args, **kwargs)
    
    def create(self, request, *args, **kwargs):
        return super(SightViewSet, self).create(request, *args, **kwargs)

    def destroy(self, request,  *args, **kwargs):
        return super(SightViewSet, self).destroy(request, *args, **kwargs)

    # Retorna através de um get um recurso específico
    def retrieve(self, request, *args, **kwargs):
        return super(SightViewSet, self).retrieve(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        return super(SightViewSet, self).update(request, *args, **kwargs)

    def partial_update(self, request, *args, **kwargs):
        return super(SightViewSet, self).partial_update(request, *args,
                                                        **kwargs)

    # Action personalizada.
    # Uma action para quem quiser denunciar um endpoint
    # detail precisa ser True para dizer que se refere a um recurso do 
    # endpoint, e não ao endpoint como um todo.
    # É preciso passar o pk do recurso e depois o nome da action personalizada
    @action(methods=['get'], detail=True)
    def denounce(self, request, pk=None):
        pass

    # Action para o endpoint em geral
    @action(methods=['get'], detail=False)
    def teste(self, request):
        pass
