from django.urls import include, path
from .views import PictureList, PictureDetail, PictureCreate, \
    PictureDelete, PictureUpdate, PictureOwnerList, TypePictureList


urlpatterns = [
    path("", PictureList.as_view(), name="picture_list"),
    path("mypicturelist/", PictureOwnerList.as_view(), name="my_picture_list"),
    path("type/<int:pk>/", TypePictureList.as_view(), name="type_picture"),
    path("<int:pk>/", PictureDetail.as_view(), name="picture_detail"),
    path("delete/<int:pk>/", PictureDelete.as_view(), name="picture_delete"),
    path("update/<int:pk>/", PictureUpdate.as_view(), name="picture_update"),
    path("new/", PictureCreate.as_view(), name="picture_new"),
]
