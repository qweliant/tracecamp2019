from django.db import models

# Create your models here.


class Movie(models.Model):
    title = models.CharField(max_length=125)
    
    @classmethod
    def create(cls, title):
        movie = cls(title=title)
        # do something with the book
        return movie