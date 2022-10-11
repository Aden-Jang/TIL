from django.db import models

# Create your models here.
class Question(models.Model):
    title = models.CharField(max_length=50)
    issue_a = models.CharField(max_length=50)
    issue_b = models.CharField(max_length=50)


class Comment(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    content = models.CharField(max_length=100)
    pick = models.BooleanField()
    # pick = models.IntegerField()
