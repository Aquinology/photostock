from django.urls import include, path
from .views import PictureList, PictureDetail


urlpatterns = [
    path("", PictureList.as_view(), name="picture_list"),
    path("<int:pk>/", PictureDetail.as_view(), name="picture_detail"),
]
