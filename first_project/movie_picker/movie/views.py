import requests
from movie.models import Movie
from movie.serializers import MovieSerializer
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
# Create your views here.
# Import Model

def hello_world_response(request):
    api_key = "5f2b00a991eef055a54a22efc396872d"
    url = f'https://api.themoviedb.org/3/movie/2652?api_key={api_key}'
    response = requests.get(url)
    # Create new movie model with the title set look at model.objects.create
    return HttpResponse(response)


def movie_picker_list(request):
    if request.method == 'GET':
        data = Mvie.objects.all()
        serializer = MovieSerializer(data, many=True)
        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = MovieSerializer(data)
        if serializer.is_valid():
            serializer.save
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=404) 

    