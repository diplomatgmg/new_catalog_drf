from rest_framework import serializers

from apps.favorites.models import Favorites
from apps.product.serializers import CPUSerializer, GPUSerializer


class FavoritesSerializer(serializers.ModelSerializer):
    cpu = CPUSerializer(read_only=True, many=True)
    gpu = GPUSerializer(read_only=True, many=True)
    class Meta:
        model = Favorites
        fields = ("cpu", "gpu")
