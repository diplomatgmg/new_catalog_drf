from django.urls import path, include
from rest_framework import routers

from apps.product import views

router = routers.SimpleRouter()
router.register("cpu", views.CPUModelViewSet)
router.register("gpu", views.GPUModelViewSet)

app_name = "product"

urlpatterns = [
    path("", include(router.urls)),
]
