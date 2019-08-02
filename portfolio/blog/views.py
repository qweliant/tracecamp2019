import requests
from .models import Post, Comment
from .forms import PostCreateForm
from django.shortcuts import render
from django.views.generic import CreateView, DetailView, UpdateView,ListView, TemplateView, DeleteView
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.urls import reverse_lazy

# Create your views here.

class PostCreateView(CreateView):
    model = Post
    form_class = PostCreateForm
    success_url = reverse_lazy('post_list')

class PostUpdateView(UpdateView):
    model = Post
    form_class = PostCreateForm
    success_url = reverse_lazy('post_list')

class PostDetailView(DetailView):
    model = Post


class PostListView(ListView):
    model = Post

class PostDeleteView(DeleteView):
    model = Post
    form_class = PostCreateForm
    success_url = reverse_lazy('post_list')

class PostTemplateView(TemplateView):
    template_name= "home.html"  


class PostListView(ListView):
    model = Post