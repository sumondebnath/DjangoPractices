from django.db import models
from musician.models import Musicians

# Create your models here.
class Albums(models.Model):
    ratingChoices = [("1", "1"), ("2", "2"), ("3", "3"), ("4", "4"), ("5", "5")]
    album_name = models.CharField(max_length=50)
    release_date = models.DateTimeField(auto_now_add = True)
    # rating = models.PositiveSmallIntegerField(choices=ratingChoices)
    rating = models.CharField(max_length=10, choices=ratingChoices)

    musicians = models.ForeignKey(Musicians, on_delete=models.CASCADE)

    def __str__(self):
        return self.album_name