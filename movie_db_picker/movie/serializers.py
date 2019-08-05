from rest_framework import serializers
from .models import MovieTrain, MovieApi


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = MovieTrain
        fields = ['title', 'id']
        read_only_fields = ['id']


class MovieAPISerializer(serializers.ModelSerializer):
    class Meta:
        model = MovieApi
        fields = ['id','title', 'rating', 'genre']