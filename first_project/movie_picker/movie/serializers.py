from rest_framework import serializers
from movie.models import Movie


class MovieSerializer(serializers.Serializer):
    class Meta:
        model = Movie
        fields = ['title']

