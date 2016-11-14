from models import Orden, Line
from rest_framework.serializers import ModelSerializer, HiddenField


class LineSerializer(ModelSerializer):
    class Meta:
        model = Line
        fields = ('id','cantidad', 'producto','orden')

class LinePostSerializer(ModelSerializer):
    class Meta:
        model = Line
        fields = ('id','cantidad', 'producto', 'orden')
        modified = HiddenField(default=Line.orden) #esto es caca

class OrdenSerializer(ModelSerializer):
    lines = LineSerializer(many=True, read_only=True)

    class Meta:
        model = Orden
        fields = ('id','mesa', 'lines')


