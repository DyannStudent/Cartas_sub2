from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

cartas_lista = [
    {"id": 1, "nombre": "Charizard ex", "tipo": "Fuego", "rareza": "Ultra Rara", "hp": 330},
    {"id": 2, "nombre": "Pikachu VMAX", "tipo": "Rayo", "rareza": "Secreta", "hp": 310},
    {"id": 3, "nombre": "Mewtwo V", "tipo": "Psíquico", "rareza": "Rara Holo", "hp": 220},
]