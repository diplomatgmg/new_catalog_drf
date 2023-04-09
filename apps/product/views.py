from rest_framework import pagination, viewsets, mixins

from apps.product.models import CPU, GPU
from apps.product.serializers import CPUSerializer, GPUSerializer


class ModelPagination(pagination.PageNumberPagination):
    page_size = 15


class CPUModelViewSet(
    mixins.RetrieveModelMixin,
    mixins.ListModelMixin,
    viewsets.GenericViewSet,
):
    queryset = CPU.objects.all()
    serializer_class = CPUSerializer
    pagination_class = ModelPagination


class GPUModelViewSet(
    mixins.RetrieveModelMixin,
    mixins.ListModelMixin,
    viewsets.GenericViewSet,
):
    queryset = GPU.objects.all()
    serializer_class = GPUSerializer
    pagination_class = ModelPagination
