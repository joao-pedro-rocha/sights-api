from rest_framework.serializers import ModelSerializer
from adresses.models import Adress


class AdressSerializer(ModelSerializer):

    class Meta:
        model = Adress
        fields = ('id', 'line_1', 'line_2', 'city', 'state', 'country', 'latitude',
                  'longitude',)
