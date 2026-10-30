from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

#recursos del ote
cartas = [
    {"id": 1, "nombre": "Omanyte", "rareza": "no comun", "precio": 10.00},
    {"id": 2, "nombre": "Goldeen", "rareza": "comun", "precio": 5.00},
    {"id": 3, "nombre": "Lapras", "rareza": "rara", "precio": 15.00}
    {"id": 3, "nombre": "Mewtwo", "rareza": "Legendario", "precio": 30.00}
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
