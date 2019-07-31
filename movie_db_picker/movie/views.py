import requests
from .models import Movie, MovieApi
from .serializers import MovieSerializer, MovieAPISerializer
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http import HttpResponse, JsonResponse
from django.views.generic import CreateView, DetailView, UpdateView,ListView, TemplateView, DeleteView
from .forms import CommentForm
from django.urls import reverse_lazy

# Create your views here.
# Import Model

class HomePageView(TemplateView):
    template_name = "home.html"

class MovieAPIListView(ListView):
    model = MovieApi


class MovieAPIDetailView(DetailView):
    model = MovieApi

class MovieAPIDelete(DeleteView):
    model = MovieApi
    success_url = reverse_lazy('movie_list')

'''@csrf_exempt
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
        return JsonResponse(serializer.errors, status=400)'''

'''@csrf_exempt
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
        return JsonResponse(serializer.errors, status=400)'''

'''@csrf_exempt 
def movie_api_detail(request, pk):
    snippet = MovieApi.objects.get(pk=pk)
    if request.method =='GET':
        serializer = MovieAPISerializer(snippet)
        return JsonResponse(serializer.data)
    if request.method =='POST':
        if request.body.decode('utf-8') == "":
            return HttpResponse('You need to pass in some data', status=400)
        data = JSONParser().parse(request)
        serializer = MovieAPISerializer(snippet, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)'''

def add_comment_to_post(request, pk):
    movie = get_object_or_404(MovieApi, pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = movie
            comment.save()
            return redirect('movie_api_detail', pk=movie.pk)
    else:
        form = CommentForm()
    return render(request, 'movie/movie_comment.html', {'form': form})

