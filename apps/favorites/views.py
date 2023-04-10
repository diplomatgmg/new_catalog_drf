from django.http import HttpResponse
from rest_framework.generics import ListAPIView

from apps.favorites.favorites import Favorites
from apps.favorites.models import Favorites as FavoritesModel
from apps.favorites.serializers import FavoritesSerializer


#
# class FavoritesListView(ListViewMixin, TemplateViewMixin):
#     template_name = "favorites/favorites-list.html"
#     model = FavoritesModel
#     context_object_name = "favorites"
#
#     def get_queryset(self):
#         if self.request.user.is_authenticated:
#             user_favorites = self.model.objects.filter(
#                 user=self.request.user
#             ).last()
#         else:
#             user_favorites = self.model.objects.filter(
#                 temp_user=self.request.session.session_key
#             ).last()
#         return user_favorites.get_favorites() if user_favorites else []
#
#

#
#


class FavoritesListAPIView(ListAPIView):
    serializer_class = FavoritesSerializer

    def get_queryset(self):
        if self.request.user.is_authenticated:
            user_favorites = FavoritesModel.objects.filter(user=self.request.user)
        else:
            session_key = self.request.session.session_key
            if session_key:
                user_favorites = FavoritesModel.objects.filter(temp_user=session_key)
            else:
                return []
        return user_favorites


def favorites_add(request, category_slug, product_slug):
    favorites = Favorites(request, category_slug)
    favorites.update(product_slug)


def favorites_remove(request, category_slug, product_slug):
    favorites = Favorites(request, category_slug)
    favorites.update(product_slug, "remove")
    return HttpResponse({"success": True})
