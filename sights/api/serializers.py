from rest_framework.serializers import ModelSerializer
from rest_framework.fields import SerializerMethodField
from sights.models import Sight
from attractions.api.serializers import AttractionSerializer
from adresses.api.serializers import AdressSerializer


class SightSerializer(ModelSerializer):
    # Quando um serializer retornar um json apenas com o id de um id em um
    # campo que tem ralacionamento com outro objeto, é possível usar o
    # serializer do objeto relacionado ao atributo e trazer mais informações
    # do objeto, no lugar de trazer apenas seu id
    adress = AdressSerializer()

    # Quando um relacionamento for many to many, usar o parâmetro many=True
    attractions = AttractionSerializer(many=True)

    # Pode-se criar métodos dentro do serializer e retorná-los no json
    complete_description = SerializerMethodField()

    class Meta:
        model = Sight

        # complete_description_2 é uma forma de passar um método do model no
        # json. Basta usar @property em cima do método
        fields = ('id', 'name', 'description', 'approved', 'image',
                  'attractions', 'adress', 'complete_description',
                  'complete_description_2')
        
    def get_complete_description(self, obj):
        return f'{obj.name} - {obj.description}'
