from rest_framework.response import Response

from models import Orden, Line
from rest_framework import viewsets
from serializers import OrdenSerializer, LineSerializer


# Orden views
class OrdenViewSet(viewsets.ModelViewSet):
    """
    API endpoint que permite editar y ver Ordenes
    """
    queryset = Orden.objects.all()
    serializer_class = OrdenSerializer


class OrdenLinesViewSet(viewsets.ModelViewSet):
    queryset = Line.objects.all()
    serializer_class = LineSerializer

    def list(self, request, orden_pk):
        orden_lines = Line.objects.filter(orden__pk = orden_pk)
        serializer = self.get_serializer(orden_lines, many=True)
        return Response(serializer.data)

    # hacer create

# Line views
class LineViewSet(viewsets.ModelViewSet):
    """
    API endpoint que permite editar y ver Ordenes
    """
    queryset = Line.objects.all()
    serializer_class = LineSerializer


