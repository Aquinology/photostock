from django.db import models
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill
from photostock.users.models import User
from django.utils import timezone


class TypePicture(models.Model):
    name = models.CharField(max_length=255, null=False, blank=False)

    def get_count_type_picture(self):
        return Picture.objects.filter(type=self.id).count()

    def __str__(self):
        return self.name


class Picture(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=125)
    type = models.ForeignKey(TypePicture, on_delete=models.CASCADE, default=1)
    created_date = models.DateTimeField(default=timezone.now)
    picture = models.ImageField(upload_to="images/", null=True, blank=False)
    small_picture = ImageSpecField(source="picture", processors=[ResizeToFill(225, 350)],
                                   format="JPEG", options={"quality": 100})

    def __str__(self):
        return self.title


# picture = Picture.objects.all()[0]
# print(picture.small_picture.url)
# print(picture.small_picture.width)
