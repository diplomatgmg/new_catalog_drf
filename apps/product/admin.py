from django.contrib import admin

from apps.product.models import Brand, Category, CPU, GPU


@admin.register(Brand)
class BrandModelAdmin(admin.ModelAdmin):
    list_display = ("name", "id")


@admin.register(Category)
class CategoryModelAdmin(admin.ModelAdmin):
    pass


class BaseProductModelAdmin(admin.ModelAdmin):
    search_fields = ("slug",)
    list_select_related = ("brand",)


@admin.register(CPU)
class CPUModelAdmin(BaseProductModelAdmin):
    pass


@admin.register(GPU)
class GPUModelAdmin(BaseProductModelAdmin):
    pass
