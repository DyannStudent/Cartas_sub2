from rest_framework import serializers
from .models import cartas

from .models import Cliente

from .models import Vendedor

class cartasSerializer(serializers.ModelSerializer):
    class Meta:
        model = cartas
        fields = '__all__'  
        

class VendedorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vendedor


# ---------------- Recurso Cliente (Andrés) ----------------
class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'
