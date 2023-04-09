from rest_framework import generics

from apps.product.models import Category
from apps.product.serializers import CategorySerializer


class IndexListAPIView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
