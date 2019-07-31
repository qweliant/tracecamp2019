from django.db import models
from django.core.validators import URLValidator
from django.utils import timezone 
# Create your models here.


class Movie(models.Model):
    title = models.CharField(max_length=125)
    


class MovieApi(models.Model):
    title = models.CharField(max_length=200)
    rating = models.CharField(max_length=6)
    genre = models.CharField(max_length=300)
    image = models.TextField(blank=True)
    tag = models.TextField(blank=True)
    description = models.TextField(blank=True)


    def __str__(self): 
        return self.title 

    def approved_comments(self):
        return self.comments.filter(approved_comment=True)

class Comment(models.Model):
    movie = models.ForeignKey('MovieApi', on_delete=models.CASCADE, related_name='comments')
    author = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.text
