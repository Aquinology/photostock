from django.db import models
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill


class Picture(models.Model):
    title = models.CharField(max_length=125)
    picture = models.ImageField(upload_to="images/", null=True, blank=False)
    small_picture = ImageSpecField(source="picture", processors=[ResizeToFill(225, 350)],
                                   format="JPEG", options={"quality": 60})
    desc = models.TextField()

    def __str__(self):
        return self.title


picture = Picture.objects.all()[0]
print(picture.small_picture.url)
print(picture.small_picture.width)
