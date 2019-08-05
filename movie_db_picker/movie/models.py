from django.db import models
from django.core.validators import URLValidator
from django.utils import timezone 
# Create your models here.


class Movie(models.Model):

    Mid = models.IntegerField(default=0)
    belongs_to_collection=models.CharField(max_length=50000,default=" ")
    budget=models.IntegerField(default=0)
    genres= models.CharField(max_length=50000,default=" ")
    homepage=models.CharField(max_length=50000,default=" ")	
    imdb_id=models.CharField(max_length=5000,default=" ")
    original_language=models.CharField(max_length=50000,default=" ")
    original_title=models.CharField(max_length=50000,default=" ")
    overview=models.CharField(max_length=50000,default=" ")
    popularity=models.DecimalField(max_digits=8, decimal_places=2, default=0.00)
    poster_path=models.CharField(max_length=50000,default=" ")
    production_companies=models.CharField(max_length=50000,default=" ")
    production_countries=models.CharField(max_length=50000,default=" ")
    release_date=models.DateField(default=timezone.now)
    runtime=models.TextField(default="")
    spoken_languages=models.CharField(max_length=50000,default=" ")
    status=models.CharField(max_length=50000,default=" ")
    tagline=models.CharField(max_length=50000,default=" ")
    title=models.CharField(max_length=50000,default=" ")
    Keywords=models.CharField(max_length=50000, default=" ")
    cast=models.CharField(max_length=50000,default=" ")
    crew=models.CharField(max_length=50000,default=" ")
    revenue=models.IntegerField(default=0)


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
