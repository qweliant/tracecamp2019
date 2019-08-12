import requests
from .models import MovieTrain, MovieTest, MovieApi
from .serializers import MovieSerializer, MovieAPISerializer
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http import HttpResponse, JsonResponse
from django.views.generic import CreateView, DetailView, UpdateView,ListView, TemplateView, DeleteView
from .forms import CommentForm
from django.urls import reverse_lazy

class HomePageView(TemplateView):
    template_name = "home.html"

class MovieAPIListView(ListView):
    model = MovieApi

class MovieListView(ListView):
    model = MovieTrain

class MovieAPIDetailView(DetailView):
    model = MovieApi

class MovieAPIDelete(DeleteView):
    model = MovieApi
    success_url = reverse_lazy('movie_list')

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

''