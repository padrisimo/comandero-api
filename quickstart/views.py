from django.shortcuts import render

from models import Orden, Line
from rest_framework import viewsets
from serializers import OrdenSerializer, LineSerializer

class LineViewSet(viewsets.ModelViewSet):
    """
    API endpoint que permite editar y ver Lineas
    """
    queryset = Line.objects.all()
    serializer_class = LineSerializer


class OrdenViewSet(viewsets.ModelViewSet):
    """
    API endpoint que permite editar y ver Ordenes
    """
    queryset = Orden.objects.all()
    serializer_class = OrdenSerializer

