from django.shortcuts import render
from rest_framework import generics

from rest_framework.generics import ListAPIView

from models import Orden, Line
from rest_framework import viewsets
from serializers import OrdenSerializer, LineSerializer

class LineViewSet(viewsets.ModelViewSet):
    """
    API endpoint que permite editar y ver Lineas
    """

    queryset = Line.objects.all().filter(id=5) # cambia el id por varibale o algo
    serializer_class = LineSerializer


class OrdenViewSet(viewsets.ModelViewSet):
    """
    API endpoint que permite editar y ver Ordenes
    """
    queryset = Orden.objects.all()
    serializer_class = OrdenSerializer



