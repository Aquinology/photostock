from django.db import models
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill
from photostock.users.models import User
from django.utils import timezone


class Picture(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=125)
    created_date = models.DateTimeField(default=timezone.now)
    picture = models.ImageField(upload_to="images/", null=True, blank=False)
    small_picture = ImageSpecField(source="picture", processors=[ResizeToFill(225, 350)],
                                   format="JPEG", options={"quality": 60})
    desc = models.TextField()

    def __str__(self):
        return self.title


# picture = Picture.objects.all()[0]
# print(picture.small_picture.url)
# print(picture.small_picture.width)
