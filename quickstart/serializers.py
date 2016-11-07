from models import Orden
from rest_framework import serializers


class OrdenSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Orden
        fields = ('cantidad', 'producto', 'mesa')