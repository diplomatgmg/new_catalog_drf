from django.urls import path

from apps.favorites.views import (
    FavoritesListAPIView,
    favorites_add,
    favorites_remove,
)

app_name = "favorites"

urlpatterns = [
    path("", FavoritesListAPIView.as_view(), name="list"),
    path(
        "add/<slug:category_slug>/<slug:product_slug>",
        favorites_add,
        name="add",
    ),
    path(
        "remove/<slug:category_slug>/<slug:product_slug>",
        favorites_remove,
        name="remove",
    ),
]
