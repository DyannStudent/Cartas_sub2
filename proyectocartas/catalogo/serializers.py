from rest_framework import serializers
from .models import cartas

class cartasSerializer(serializers.ModelSerializer):
    class Meta:
        model = cartas
        fields = '__all__'  