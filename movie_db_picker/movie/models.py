from django.db import models

# Create your models here.


class Movie(models.Model):
    title = models.CharField(max_length=125)
    


class MovieApi(models.Model):
    title = models.CharField(max_length=200)
    rating = models.CharField(max_length=6)
    genre = models.CharField(max_length=300)
