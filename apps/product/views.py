import django_filters
from rest_framework import pagination
from rest_framework.viewsets import ModelViewSet

from apps.product.filters import CPUFilter
from apps.product.models import CPU, GPU
from apps.product.serializers import GPUSerializer, CPUSerializer


class ModelPagination(pagination.PageNumberPagination):
    page_size = 15


class BaseModelViewSet(ModelViewSet):
    pagination_class = ModelPagination


class CPUModelViewSet(BaseModelViewSet):
    queryset = CPU.objects.all()
    serializer_class = CPUSerializer
    filterset_class = CPUFilter


class GPUModelViewSet(BaseModelViewSet):
    queryset = GPU.objects.all()
    serializer_class = GPUSerializer
