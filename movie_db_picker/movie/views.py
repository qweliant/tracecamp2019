import requests
from .models import Movie, MovieApi
from .serializers import MovieSerializer, MovieAPISerializer
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http import HttpResponse, JsonResponse
from django.views.generic import CreateView, DetailView, UpdateView,ListView, TemplateView, DeleteView
from .forms import CommentForm
from django.urls import reverse_lazy

import numpy
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import mean_absolute_error
# Create your views here.
# Import Model

from django_pandas.io import read_frame
qs = Movie.objects.all()
df = read_frame(qs)
#print(df.describe())
#print(df.original_language.unique())
lang ={
    'ja': 0,
    'en': 1,
    'fr': 2,
    'de': 3,
    'he': 4,
    'hi': 5,
    'ru': 6,
    'ka': 7,
    'zh': 8, 
    'th': 9,
    'it': 10,
    'es': 11,
    'bn': 12,
    'sv': 13,
    'ko': 14,
    'sr': 15,
    'da': 16,
    'ta': 17,
    'cs': 18,
    'cn': 19,
    'ro': 20,
    'ca': 21,
    'no': 22,
    'nl': 23,
    'te': 24,
    'tr': 25,
    'bm': 26,
    'ml': 27,
    'pt': 28, 'af': 29, 'fi': 30, 'ur': 31, 'el': 32, 'id': 33, 'xx': 34, 'pl':35, 'kn':36, 'is': 37, 'hu': 38}
    
    
df.replace(lang, inplace=True)
#print(df['original_language'])
train = train_test_split(df.copy(), random_state=0)
train.shape#, test.shape



features = ['budget', 'popularity', 'original_language']
target = 'revenue'
model = DecisionTreeRegressor()
model.fit(train[features], train[target])

y = train[target]
y_pred = model.predict(train[features])
train_error = mean_absolute_error(y, y_pred)

'''y = test[target]
y_pred = model.predict(test[features])
test_error = mean_absolute_error(y, y_pred)'''


print('train error', train_error)
print('test error', test_error)

class HomePageView(TemplateView):
    template_name = "home.html"

class MovieAPIListView(ListView):
    model = MovieApi

class MovieListView(ListView):
    model = Movie


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

