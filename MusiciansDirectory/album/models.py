from django.db import models
from musician.models import Musician

# Create your models here.
class Album(models.Model):
    Choice = [("1", "1"), ("2", "2"),("3", "3"),("4", "4"), ("5", "5")]
    album_name = models.CharField(max_length=50)
    album_release_date = models.DateTimeField(auto_now_add=True)
    rating = models.CharField(max_length=10,choices=Choice)
    musicians = models.ForeignKey(Musician, on_delete=models.CASCADE)
