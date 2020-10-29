from django.urls import include, path
from .views import PictureList


urlpatterns = [
    path("", PictureList.as_view(), name="picture_list"),
]
