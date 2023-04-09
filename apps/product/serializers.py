from rest_framework import serializers

from apps.product.models import Category, CPU, GPU


class CategorySerializer(serializers.ModelSerializer):
    url = serializers.SerializerMethodField()

    def get_url(self, category):
        return category.get_absolute_url()

    class Meta:
        model = Category
        fields = ("name", "slug", "url")


class CPUSerializer(serializers.ModelSerializer):
    class Meta:
        model = CPU
        fields = ("id", "slug")


class GPUSerializer(serializers.ModelSerializer):
    class Meta:
        model = GPU
        fields = ("id", "slug")
