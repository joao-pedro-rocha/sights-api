from rest_framework.serializers import ModelSerializer
from rest_framework.fields import SerializerMethodField
from sights.models import Sight, DocumentOfIntent
from attractions.models import Attraction
from adresses.models import Adress
from attractions.api.serializers import AttractionSerializer
from adresses.api.serializers import AdressSerializer
from comments.api.serializers import CommentSerializer
from reviews.api.serializers import ReviewSerializer
import pprint


class DocumentOfIntentSerializer(ModelSerializer):

    class Meta:
        model = DocumentOfIntent
        fields = '__all__'


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
    document_of_intent = DocumentOfIntentSerializer()

    class Meta:
        model = Sight

        # complete_description_2 é uma forma de passar um método do model no
        # json. Basta usar @property em cima do método
        fields = ('id', 'name', 'description', 'approved', 'comments',
                  'reviews', 'image', 'attractions', 'adress',
                  'complete_description', 'complete_description_2',
                  'document_of_intent')
        
        # Permite que esses campos não sejam passados no payload
        read_only_fields = ('comments', 'reviews',)

    def create_attraction(self, attractions, sight):
        for attraction_data in attractions:
            attraction = Attraction.objects.create(**attraction_data)
            sight.attractions.add(attraction)

    def create(self, validated_data):
        attractions = validated_data['attractions']
        adress_data = validated_data['adress']
        document_of_intent_data = validated_data['document_of_intent']

        del validated_data['attractions']
        del validated_data['adress']
        del validated_data['document_of_intent']
        
        adress = Adress.objects.create(**adress_data)
        document_of_intent = DocumentOfIntent.objects.create(
            **document_of_intent_data
        )
        sight = Sight.objects.create(**validated_data)
        self.create_attraction(attractions, sight)

        sight.adress = adress
        sight.document_of_intent = document_of_intent
        sight.save()

        return sight
        
    def get_complete_description(self, obj):
        return f'{obj.name} - {obj.description}'
