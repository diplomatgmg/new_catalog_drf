from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import pagination, viewsets, mixins, filters as rest_filters

from apps.product.filters import CPUFilter
from apps.product.models import CPU, GPU
from apps.product.serializers import GPUSerializer, CPUSerializer


class ModelPagination(pagination.PageNumberPagination):
    page_size = 15


class BaseModelViewSet(
    mixins.RetrieveModelMixin, mixins.ListModelMixin, viewsets.GenericViewSet
):
    pagination_class = ModelPagination
    filter_backends = [
        DjangoFilterBackend,
    ]
    ordering_fields = ["slug", "year"]


class CPUModelViewSet(BaseModelViewSet):
    queryset = CPU.objects.all()
    serializer_class = CPUSerializer
    filterset_class = CPUFilter

class GPUModelViewSet(BaseModelViewSet):
    queryset = GPU.objects.all()
    serializer_class = GPUSerializer
