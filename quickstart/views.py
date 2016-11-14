

from models import Orden, Line
from django.http import Http404
from rest_framework import viewsets
from rest_framework.response import Response
from serializers import OrdenSerializer, LineSerializer, LinePostSerializer
from rest_framework import status


# Orden views
class OrdenViewSet(viewsets.ModelViewSet):
    """
    API endpoint que permite editar y ver Ordenes
    """
    queryset = Orden.objects.all()
    serializer_class = OrdenSerializer


class OrdenLinesViewSet(viewsets.ModelViewSet):
    queryset = Line.objects.all()
    serializer_class = LinePostSerializer

    def list(self, request, orden_pk):

        orden_lines = Line.objects.filter(orden__pk = orden_pk)
        serializer = self.get_serializer(orden_lines, many=True)
        return Response(serializer.data)

    # hacer create
    def create(self, request, orden_pk):



        print orden_pk
        print request.data
        request.data['orden'] = orden_pk
        serializer = LinePostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Line views
class LineViewSet(viewsets.ModelViewSet):
    """
    API endpoint que permite editar y ver Ordenes
    """
    queryset = Line.objects.all()
    serializer_class = LineSerializer


