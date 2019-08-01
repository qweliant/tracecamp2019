import requests
from .models import Post, Comment
from django.shortcuts import render
from django.views.generic import CreateView, DetailView, UpdateView,ListView, TemplateView, DeleteView
#from .forms import CommentForm
from django.urls import reverse_lazy

# Create your views here.
# Import Model

class HomePageView(TemplateView):
    template_name = "home.html"

class CreatePostView(CreateView):
    model = Post
 
class PostListView(ListView):
    model = Post

class PostDetailView(DetailView):
    model = Post

class PostDelete(DeleteView):
    model = Post
    success_url = reverse_lazy('movie_list')