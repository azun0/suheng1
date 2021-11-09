from django.urls import path
from django.urls.resolvers import URLPattern
from .views import PhotoList, PhotoDetail, PhotoUpdate, PhotoCreate, PhotoDelete, PhotoLike, PhotoFavorite

app_name = "photo"

urlpatterns = [
    path("create/",PhotoCreate.as_view(),name='create'),
    path("like/<int:photo_id>/", PhotoLike.as_view(), name='like'),
    path("favorite/<int:photo_id>/",  PhotoFavorite.as_view(), naem='favorite'),
    path("delete/<int:pk>/",PhotoDelete.as_view(),name='delete'),
    path("update/<int:pk>/",PhotoUpdate.as_view(),name='update'),
    path("detail/<int:pk>/",PhotoDetail.as_view(),name='detail'),
    path("",PhotoList.as_view(),name='index'),
]

from django.conf.urls.static import static
from django.conf import settings

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)