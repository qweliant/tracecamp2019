from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('post/create/', views.PostCreateView.as_view(), name='post_create'),
    path('post/update/<int:pk>', views.PostUpdateView.as_view(), name='post_update'),
    path('post/detail/<int:pk>', views.PostDetailView.as_view(), name='post_detail'),
    path('post/list/', views.PostListView.as_view(), name='post_list'),
    path('post/delete/<int:pk>', views.PostDeleteView.as_view(), name='post_delete'),
    path('post/', views.PostTemplateView.as_view(), name='home'),
    path('post/comment/<int:pk>/', views.add_comment_to_post, name='add_comment_to_post'),

]
