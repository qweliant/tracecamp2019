from django.urls import path
from movie import views
from . import views


urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
    path('movieapi/list/', views.MovieAPIListView.as_view(), name='movie_api_list'),
    path('movieapi/<int:pk>/', views.MovieAPIDetailView.as_view(), name = 'movie_api_detail'),
    path('movieapi/delete/<int:pk>/', views.MovieAPIDelete.as_view(), name='movie_delete'),
    path('movieapi/comment/<int:pk>', views.add_comment_to_post, name='add_comment_to_post'),
]
