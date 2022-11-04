from django.db import models
from django.conf import settings
from movies.models import Movie

# Create your models here.

class Review(models.Model):

    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='likereviews')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='myreviews')
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='reviews')
    
    title=models.CharField(max_length=100)
    rank=models.IntegerField()
    content=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

class Comment(models.Model):

    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='likecomments')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='mycomments')
    review = models.ForeignKey(Review, on_delete=models.CASCADE, related_name='comments')

    content = models.TextField()