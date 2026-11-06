from django.shortcuts import render
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

from .models import Vendedor
from .serializers import VendedorSerializer


@api_view(['GET'])
def listar_vendedores(request):
    vendedores = Vendedor.objects.all()
    serializer = VendedorSerializer(vendedores, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def crear_vendedor(request):
    serializer = VendedorSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(serializer.data, status=status.HTTP_201_CREATED)


class VendedorDetail(APIView):
    def get_object(self, pk):
        return get_object_or_404(Vendedor, pk=pk)

    def get(self, request, pk):
        vendedor = self.get_object(pk)
        serializer = VendedorSerializer(vendedor)
        return Response(serializer.data)

    def put(self, request, pk):
        vendedor = self.get_object(pk)
        serializer = VendedorSerializer(vendedor, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def delete(self, request, pk):
        vendedor = self.get_object(pk)
        vendedor.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

#recursos del ote
cartas = [
    {"id": 1, "nombre": "Omanyte", "rareza": "no comun", "precio": 10.00},
    {"id": 2, "nombre": "Goldeen", "rareza": "comun", "precio": 5.00},
    {"id": 3, "nombre": "Lapras", "rareza": "rara", "precio": 15.00},
    {"id": 3, "nombre": "Mewtwo", "rareza": "Legendario", "precio": 30.00},
]

@api_view(['GET'])
def obtener_cartas(request):
    return Response(cartas)

@api_view(['POST'])
def crear_cartas(request):
    nuevo_registro = request.data
    
    nuevo_id = len(cartas) + 1 if cartas else 1
    nuevo_registro["id"] = nuevo_id
    
    cartas.append(nuevo_registro)
    
    return Response(nuevo_registro, status=status.HTTP_201_CREATED)


# ---------------- Recurso Cliente (Andrés) ----------------
clientes = [
    {"id": 1, "nombre": "Gary Oak", "email": "gary@pallet.cl", "ciudad": "Santiago", "cartas_compradas": 12},
    {"id": 2, "nombre": "Serena Kalos", "email": "serena@kalos.cl", "ciudad": "Valparaíso", "cartas_compradas": 7},
    {"id": 3, "nombre": "Dawn Berlitz", "email": "dawn@sinnoh.cl", "ciudad": "Concepción", "cartas_compradas": 20},
]


@api_view(['GET'])
def listar_clientes(request):
    """Devuelve la lista completa de clientes de la tienda."""
    return Response(clientes)


@api_view(['POST'])
def crear_cliente(request):
    """Recibe un cliente nuevo desde request.data, le asigna id y lo agrega a la lista."""
    datos = request.data
    nuevo_id = max([c["id"] for c in clientes], default=0) + 1

    nuevo_cliente = {
        "id": nuevo_id,
        "nombre": datos.get("nombre"),
        "email": datos.get("email"),
        "ciudad": datos.get("ciudad"),
        "cartas_compradas": datos.get("cartas_compradas", 0),
    }

    clientes.append(nuevo_cliente)
    return Response(nuevo_cliente, status=status.HTTP_201_CREATED)
