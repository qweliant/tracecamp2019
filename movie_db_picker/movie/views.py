import requests
from movie.models import Movie, MovieApi
from movie.serializers import MovieSerializer, MovieAPISerializer
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http import HttpResponse, JsonResponse
from django.views.generic.edit import DeleteView
from django.urls import reverse_lazy
import random 
# Create your views here.
# Import Model

def hello_world_response(request):
    api_key = "5f2b00a991eef055a54a22efc396872d"
    url = f'https://api.themoviedb.org/3/movie/{8393}?api_key={api_key}'
    response = requests.get(url).json()
    call = {
    "title": response['original_title'],
    "rating": response['vote_average'],
    "genre": response['genres'],
        }
        
    return JsonResponse(call)

@csrf_exempt
def movie_api_list(request):
    if request.method == 'GET':
        snippets = MovieApi.objects.all()
        serializer = MovieAPISerializer(snippets, many=True)
        return JsonResponse(serializer.data, safe=False)
    
    elif request.method == 'POST':
        if request.body.decode('utf-8') == "":
            return HttpResponse('You need to pass in some data', status=400)
        data = JSONParser().parse(request)
        serializer = MovieAPISerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def movie_picker_list(request):
    if request.method == 'GET':
        snippets = Movie.objects.all()
        serializer = MovieSerializer(snippets, many=True)
        return JsonResponse(serializer.data, safe=False)
    
    elif request.method == 'POST':
        if request.body.decode('utf-8') == "":
            return HttpResponse('You need to pass in some data', status=400)
        data = JSONParser().parse(request)
        serializer = MovieSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt 
def movie_detail(request, id):
    snippet = Movie.objects.get(pk=id)
    if request.method =='GET':
        serializer = MovieSerializer(snippet)
        return JsonResponse(serializer.data)
    if request.method =='POST':
        if request.body.decode('utf-8') == "":
            return HttpResponse('You need to pass in some data', status=400)
        data = JSONParser().parse(request)
        serializer = MovieSerializer(snippet, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


class MovieDelete(DeleteView):
    model = Movie
    success_url = reverse_lazy('movie_list')
