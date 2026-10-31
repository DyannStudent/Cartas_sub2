from django.shortcuts import render
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
