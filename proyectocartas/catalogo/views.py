from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from .models import cartas
from .serializers import cartaSerializer
from rest_framework import viewsets

from .models import Cliente
from .serializers import ClienteSerializer

from .models import Vendedor
from .serializers import VendedorSerializer


class VendedorViewSet(viewsets.ModelViewSet):
    queryset = Vendedor.objects.all()
    serializer_class = VendedorSerializer

#recursos del ote
cartas = [
    {"id": 1, "nombre": "Omanyte", "rareza": "no comun", "precio": 10.00},
    {"id": 2, "nombre": "Goldeen", "rareza": "comun", "precio": 5.00},
    {"id": 3, "nombre": "Lapras", "rareza": "rara", "precio": 15.00},
    {"id": 3, "nombre": "Mewtwo", "rareza": "Legendario", "precio": 30.00},
]

#class cartaList(APIView):
#    def get(self, request):
#        cartas = cartas.objects.all()
#        serializer = cartasSerializer(cartas, many=True)
#        return Response(serializer.data)
#
#    def post(self, request):
#        serializer = cartasSerializer(data=request.data)
#        if serializer.is_valid():
#            serializer.save()
#            return Response(serializer.data, status=status.HTTP_201_CREATED)
#        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#class cartaDetail(APIView):
#    def get_object(self, pk):
#        return get_object_or_404(cartas, pk=pk)
#
#    def get(self, request, pk):
#        cartas = self.get_object(pk)
#        serializer = cartasSerializer(cartas)
#        return Response(serializer.data)
#
#    def put(self, request, pk):
#        cartas = self.get_object(pk)
#        serializer = cartasSerializer(cartas, data=request.data)
#        if serializer.is_valid():
#            serializer.save()
#            return Response(serializer.data)
#        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#    def delete(self, request, pk):
#        cartas = self.get_object(pk)
#        cartas.delete()
#        return Response(status=status.HTTP_204_NO_CONTENT)

class cartasViewSet(viewsets.ModelViewSet):
    queryset = cartas.objects.all()
    serializer_class = cartasSerializer


# ---------------- Recurso Cliente (Andrés) ----------------
class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer
