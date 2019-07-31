from django.urls import path
from movie import views
from movie.views import MovieDelete, HomePageView, MovieAPIListView


urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('movie/list/', views.movie_picker_list, name = 'movie_list'),
    path('movieapi/list/', MovieAPIListView.as_view(), name='movie_api_list'),
    path('movie/<int:pk>/', views.movie_detail),
    path('delete/<int:pk>/', MovieDelete.as_view(), name='movie_delete'),
]
