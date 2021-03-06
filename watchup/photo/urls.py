from django.conf.urls import url
from django.urls import path
from django.urls.resolvers import URLPattern
from .views import *
from . import views

app_name = "photo"

urlpatterns = [
    path("mylist/",PhotoMyList.as_view(),name='mylist'),
    path("create/",PhotoCreate.as_view(),name='create'),
    path("like/<int:photo_id>/", PhotoLike.as_view(), name='like'),
    path("favorite/<int:photo_id>/",  PhotoFavorite.as_view(), name='favorite'),
    path("delete/<int:pk>/",PhotoDelete.as_view(),name='delete'),
    path("update/<int:pk>/",PhotoUpdate.as_view(),name='update'),
    path("detail/<int:pk>/",PhotoDetail.as_view(),name='detail'),
    path("like/",PhotoLikeList.as_view(), name="like_list"),
    path("favorite/",PhotoFavoriteList.as_view(), name="favorite_list"),
    path("home/",PhotoList.as_view(),name='index'),
    path("search/",SearchFormView.as_view(),name="search"),
    path("recent/",PhotoRecent.as_view(),name="recent"),
    path("start/",views.start,name="start"),
    ]

from django.conf.urls.static import static
from django.conf import settings

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)