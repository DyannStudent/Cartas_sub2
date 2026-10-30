from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

# Datos de ejemplo para el recurso Vendedor (Paso 2)
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