from django.shortcuts import render

from models import Orden
from rest_framework import viewsets
from serializers import OrdenSerializer


class OrdenViewSet(viewsets.ModelViewSet):
    """
    API endpoint que permite editar y ver Ordenes
    """
    queryset = Orden.objects.all()
    serializer_class = OrdenSerializer
