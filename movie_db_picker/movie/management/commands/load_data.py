from django.core.management.base import BaseCommand, CommandError
import pytz
import csv
from movie.models import MovieTest, MovieTrain, MovieApi, Comment
import requests
import random
import datetime



class Command(BaseCommand):
    help = 'Overwrites titles in database'

    def add_arguments(self, parser):
        parser.add_argument('path', nargs=2, type=str)

    def handle(self, *args, **options):
        
        MovieTest.objects.all().delete()
        MovieTrain.objects.all().delete()
        MovieApi.objects.all().delete()
        Comment.objects.all().delete()
        #i am manually throtteling the range for MovieApi Data, some id val are not in there
       
        with open(options['path'][0]) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            print("loading data from: ", options['path'][0])
            line_count = 0
            for row in csv_reader:
                if line_count != 0:
                    
                    if row[13] != '':
                        MovieTrain.objects.create(
                            Mid = row[0],	
                            belongs_to_collection=row[1],	
                            budget=row[2],
                            genres=row[3],
                            homepage=row[4],
                            imdb_id=row[5],
                            original_language=row[6],
                            original_title=row[7],
                            overview=row[8],
                            popularity=row[9],
                            poster_path="https://image.tmdb.org/t/p/w500"+str(row[10]),	
                            production_companies=row[11],
                            production_countries=row[12],
                            release_date=datetime.datetime.strptime(str(row[13]), "%Y/%m/%d").strftime("%Y-%m-%d"),
                            runtime=row[14], #could not import as integer for some reason
                            spoken_languages=row[15],
                            status=row[16],
                            tagline=row[17],
                            title=row[18],
                            Keywords=row[19],
                            cast=row[20],
                            crew=row[21],
                            revenue=row[22]
                        )
                        
                line_count += 1
        
        
        with open(options['path'][1]) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            print("loading data from: ", options['path'][1])
            line_count = 0
            for row in csv_reader:
                if line_count != 0:
                    
                    if row[13] != '':
                        MovieTest.objects.create(
                            Mid = row[0],	
                            belongs_to_collection=row[1],	
                            budget=row[2],
                            genres=row[3],
                            homepage=row[4],
                            imdb_id=row[5],
                            original_language=row[6],
                            original_title=row[7],
                            overview=row[8],
                            popularity=row[9],
                            poster_path= "https://image.tmdb.org/t/p/w500"+str(row[10]),	
                            production_companies=row[11],
                            production_countries=row[12],
                            release_date=datetime.datetime.strptime(str(row[13]), "%Y/%m/%d").strftime("%Y-%m-%d"),
                            runtime=row[14], #could not import as integer for some reason
                            spoken_languages=row[15],
                            status=row[16],
                            tagline=row[17],
                            title=row[18],
                            Keywords=row[19],
                            cast=row[20],
                            crew=row[21]
                        )
                        
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
