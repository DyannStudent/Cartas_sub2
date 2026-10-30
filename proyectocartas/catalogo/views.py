from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

cartas_lista = [
    {"id": 1, "nombre": "Charizard ex", "tipo": "Fuego", "rareza": "Ultra Rara", "hp": 330},
    {"id": 2, "nombre": "Pikachu VMAX", "tipo": "Rayo", "rareza": "Secreta", "hp": 310},
    {"id": 3, "nombre": "Mewtwo V", "tipo": "Psíquico", "rareza": "Rara Holo", "hp": 220},
]

@api_view(['GET'])
def obtener_cartas(request):
    """Devuelve la lista completa de cartas Pokémon."""
    return Response(cartas_lista)

@api_view(['POST'])
def crear_carta(request):
    """Recibe los datos de una nueva carta, le asigna ID y la agrega a la lista."""
    nueva_carta = request.data.copy()

    # Asignar un ID automático basado en el último elemento
    nuevo_id = cartas_lista[-1]["id"] + 1 if cartas_lista else 1
    nueva_carta["id"] = nuevo_id

    # Agregar a la lista en memoria
    cartas_lista.append(nueva_carta)

    # Retornar el registro creado con código 201 CREATED
    return Response(nueva_carta, status=status.HTTP_201_CREATED)
