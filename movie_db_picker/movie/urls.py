from django.urls import path
from movie import views
from movie.views import MovieDelete


urlpatterns = [
    path('', views.hello_world_response),
    path('movie/list/', views.movie_picker_list, name = 'movie_list'),
    path('movieapi/list/', views.movie_api_list),
    path('movie/<int:pk>/', views.movie_detail),
    path('delete/<int:pk>/', MovieDelete.as_view(), name='movie_delete'),
]
