from models import Orden, Line
from rest_framework import serializers


class LineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Line
        fields = ('cantidad', 'producto')

class OrdenSerializer(serializers.ModelSerializer):
    lines = LineSerializer(many=True)

    class Meta:
        model = Orden
        fields = ('mesa', 'lines')

    def create(self, validated_data):
        lines_data = validated_data.pop('lines')
        orden = Orden.objects.create(**validated_data)
        for line_data in lines_data:
            Line.objects.create(orden=orden, **line_data)
        return orden

