from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

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