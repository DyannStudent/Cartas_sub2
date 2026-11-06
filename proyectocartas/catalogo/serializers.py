from rest_framework import serializers

from .models import Cliente


# ---------------- Recurso Cliente (Andrés) ----------------
class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'
