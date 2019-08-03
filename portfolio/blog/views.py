import requests
from .models import Post, Comment
from .forms import PostCreateForm, CommentForm
from django.shortcuts import render, redirect, get_object_or_404
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

def add_comment_to_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = CommentForm()
    return render(request, 'blog/add_comment_to_post.html', {'form': form})