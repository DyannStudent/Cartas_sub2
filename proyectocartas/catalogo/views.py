from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from .models import cartas
from .serializers import cartaSerializer

vendedores = [
    {
        "id": 1,
        "nombre": "Ash PokéCenter",
        "reputacion": 4.9,
        "especialidad": "Primera Edición y Antiguas",
        "ventas_realizadas": 154
    },
    {
        "id": 2,
        "nombre": "Misty Cards Store",
        "reputacion": 4.7,
        "especialidad": "Cartas Tipo Agua y Holo",
        "ventas_realizadas": 89
    },
    {
        "id": 3,
        "nombre": "Brock Collectibles",
        "reputacion": 4.5,
        "especialidad": "Ediciones Japonesas y Selladas",
        "ventas_realizadas": 210
    }
]


@api_view(['GET'])
def listar_vendedores(request):
    return Response(vendedores)

@api_view(['POST'])
def crear_vendedor(request):
    datos = request.data
    
    nuevo_id = max([v["id"] for v in vendedores], default=0) + 1
    
    nuevo_vendedor = {
        "id": nuevo_id,
        "nombre": datos.get("nombre"),
        "reputacion": datos.get("reputacion"),
        "especialidad": datos.get("especialidad"),
        "ventas_realizadas": datos.get("ventas_realizadas", 0)
    }
    
    vendedores.append(nuevo_vendedor)
    return Response(nuevo_vendedor, status=status.HTTP_201_CREATED)
#recursos del ote
cartas = [
    {"id": 1, "nombre": "Omanyte", "rareza": "no comun", "precio": 10.00},
    {"id": 2, "nombre": "Goldeen", "rareza": "comun", "precio": 5.00},
    {"id": 3, "nombre": "Lapras", "rareza": "rara", "precio": 15.00},
    {"id": 3, "nombre": "Mewtwo", "rareza": "Legendario", "precio": 30.00},
]

class cartaList(APIView):
    def get(self, request):
        cartas = cartas.objects.all()
        serializer = cartasSerializer(cartas, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = cartasSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class cartaDetail(APIView):
    def get_object(self, pk):
        return get_object_or_404(cartas, pk=pk)

    def get(self, request, pk):
        cartas = self.get_object(pk)
        serializer = cartasSerializer(cartas)
        return Response(serializer.data)

    def put(self, request, pk):
        cartas = self.get_object(pk)
        serializer = cartasSerializer(cartas, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        cartas = self.get_object(pk)
        cartas.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


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
