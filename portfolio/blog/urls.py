from django.urls import path, include
from django.contrib import admin
from . import views

urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
    path('post/', views.CreatePostView, name='post_create'),
    path('post/list/', views.PostListView.as_view(), name='post_list'),
    path('post/<int:pk>/', views.PostDetailView.as_view(), name = 'post_detail'),
    path('post/delete/<int:pk>/', views.PostDelete.as_view(), name='post_delete'),
    #path('post/comment/<int:pk>', views.add_comment_to_post, name='add_comment_to_post'),


]
