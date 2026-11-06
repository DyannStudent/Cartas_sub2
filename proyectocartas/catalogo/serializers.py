from rest_framework import serializers
from .models import Cliente

from .models import Vendedor


class VendedorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vendedor


# ---------------- Recurso Cliente (Andrés) ----------------
class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'
