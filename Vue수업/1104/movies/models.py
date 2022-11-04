from django.db import models

# Create your models here.


class Genre(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Movie(models.Model):
    genres = models.ManyToManyField(Genre, related_name="movies")

    title = models.CharField(max_length=100)
    release_date = models.DateTimeField(auto_now_add = True)
    popularity = models.FloatField()
    vote_count = models.IntegerField()
    vote_average = models.FloatField()
    overview = models.TextField()
    poster_path = models.CharField(max_length=200)

    def __str__(self):
        return self.title
