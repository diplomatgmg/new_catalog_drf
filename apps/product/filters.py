import django_filters

from apps.product.models import CPU


class BaseFilter(django_filters.FilterSet):
    multiple_choices = []
    range_choices = []

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name in self.multiple_choices:
            self.filters[field_name] = django_filters.MultipleChoiceFilter(
                field_name=field_name
            )
            self.filters[field_name].extra["choices"] = self.get_multiple_choices(
                field_name
            )
        for field_name in self.range_choices:
            self.filters[field_name] = django_filters.RangeFilter(field_name=field_name)

    def get_multiple_choices(self, field):
        values_list = (
            getattr(model, field)
            for model in self.queryset
            if getattr(model, field) or getattr(model, field) is False
        )
        return ((value, value) for value in sorted(set(values_list)))


class CPUFilter(BaseFilter):
    class Meta:
        model = CPU
        fields = "__all__"
        exclude = ["category", "slug"]

    multiple_choices = [
        "family",
        "model",
        "year",
        "segment",
        "socket",
        "unlocked_multiplier",
        "architecture",
        "technology",
        "integrated_graphics",
        "memory_controller",
        "pcie",
    ]

    range_choices = [
        "cores",
        "threads",
        "base_clock",
        "boost_clock",
        "tdp",
        "max_temperature",
        "l1_cache",
        "l2_cache",
        "l3_cache",
    ]
