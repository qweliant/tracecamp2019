from django.contrib import admin
from .models import MovieApi, Comment 


# Register your models here.
admin.site.register(MovieApi) 
admin.site.register(Comment)