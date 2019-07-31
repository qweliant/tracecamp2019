from django.core.management.base import BaseCommand, CommandError
import pytz
import csv
import pandas as pd
from movie.models import Movie, MovieApi
import requests
import random


class Command(BaseCommand):
    help = 'Overwrites titles in database'

    def add_arguments(self, parser):
        parser.add_argument('path', type=str)

    def handle(self, *args, **options):
        print("loading data from: ", options['path'])
        Movie.objects.all().delete()
        MovieApi.objects.all().delete()
        #i am manually throtteling the range for MovieApi Data, some id val are not in there
        with open(options['path']) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            line_count = 0
            for row in csv_reader:
                if line_count != 0:
                    Movie.objects.create(
                        title = row[7],
                    )
                    #print (row[7],"\n")
                line_count += 1
            print("loading data from tmdb api... ")
            
            
            api_key = "5f2b00a991eef055a54a22efc396872d"
            for i  in random.sample(range(2, 500000), 80):
                url = f'https://api.themoviedb.org/3/movie/{i}?api_key={api_key}'
                response = requests.get(url)
                #print(response.content)
                if response.status_code == 200:
                    #print("https://image.tmdb.org/t/p/w500"+str(response.json()['poster_path']))

                    MovieApi.objects.create(
                        title= response.json()['original_title'],
                        rating= response.json()['vote_average'],
                        genre= response.json()['genres'],
                        image= "https://image.tmdb.org/t/p/w500"+str(response.json()['poster_path']),
                        tag = response.json()['tagline'],
                        description = response.json()['overview'],
                    )
