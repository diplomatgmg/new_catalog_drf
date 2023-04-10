from rest_framework import serializers

from apps.product.models import Category, CPU, GPU


class CategorySerializer(serializers.ModelSerializer):
    url = serializers.SerializerMethodField()

    def get_url(self, category):
        return category.get_absolute_url()

    class Meta:
        model = Category
        fields = ("name", "slug", "url")


class BaseProductSerializer(serializers.ModelSerializer):

    url = serializers.SerializerMethodField()
    favorites_add_url = serializers.SerializerMethodField(
        method_name="get_favorites_add_url"
    )
    favorites_remove_url = serializers.SerializerMethodField(
        method_name="get_favorites_remove_url"
    )

    def get_url(self, obj):
        return obj.get_absolute_url()

    def get_favorites_add_url(self, obj):
        return obj.get_favorites_url()

    def get_favorites_remove_url(self, obj):
        return obj.get_favorites_url("remove")


class CPUSerializer(BaseProductSerializer):
    class Meta:
        model = CPU
        fields = (
            "id",
            "slug",
            "cores",
            "base_clock",
            "url",
            "favorites_add_url",
            "favorites_remove_url",
        )


class GPUSerializer(BaseProductSerializer):
    class Meta:
        model = GPU
        fields = (
            "id",
            "slug",
            "base_clock",
            "boost_clock",
            "url",
            "favorites_add_url",
            "favorites_remove_url",
        )
