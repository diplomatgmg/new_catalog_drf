import django_filters

from apps.product.models import CPU


class CPUFilter(django_filters.FilterSet):
    class Meta:
        model = CPU
        fields = '__all__'
