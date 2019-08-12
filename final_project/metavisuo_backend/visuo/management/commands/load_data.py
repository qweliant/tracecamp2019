from django.core.management.base import BaseCommand, CommandError
import pytz
import csv
from visuo.models import MovieTest, MovieTrain
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
        
        #i am manually throtteling the range for MovieApi Data, some id val are not in there
       
        with open(options['path'][0]) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            print("loading data from: ", options['path'][0])
            line_count = 0
            for row in csv_reader:
                if line_count != 0:
                    
                    if row[13] != '':
                        MovieTrain.objects.create(
                            m_id = row[0],	
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
                            m_id = row[0],	
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
