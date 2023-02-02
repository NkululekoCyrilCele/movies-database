from django.db import models
from django.utils import timezone


class MovieGenre(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class MovieList(models.Model):
    title = models.CharField(max_length=255)
    year = models.IntegerField()
    in_stock = models.IntegerField()
    daily_rate = models.FloatField()
    genre = models.ForeignKey(MovieGenre, on_delete=models.CASCADE)
    date_created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title
