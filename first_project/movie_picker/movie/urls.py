from django.urls import path
from movie import views

urlpatterns = [
    path('', views.hello_world_response),
    path('list/', views.movie_picker_list)
]
