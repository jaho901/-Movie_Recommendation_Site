import requests, re, random

from django.shortcuts import render
from rest_framework.viewsets import ReadOnlyModelViewSet

from movies.models import Movie
from movies.serializers import MovieSerializer, MovieListSerializer

from urllib.parse import quote_plus
from bs4 import BeautifulSoup
from selenium import webdriver

# Create your views here.

class MovieListViewSet(ReadOnlyModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieListSerializer

class MovieRecommendByDayViewSet(ReadOnlyModelViewSet):
    def week():
        base_url = 'https://www.google.com/search?q='
        plus_url = quote_plus('오늘의 요일')
        url = base_url + plus_url
        driver = webdriver.Chrome(executable_path='C:\\Users\\analysis\\Desktop\\SSAFY\\projects\\A_projects\\finalproject\\back-end\\chromedriver.exe')
        driver.get(url)
        html = driver.page_source
        soup = BeautifulSoup(html)
        week = soup.select_one('#rso > div.ULSxyf > div > div > div.vk_gy.vk_sh.card-section.sL6Rbf > div.vk_bk.dDoNo.FzvWSb').text
        if re.search(r'월요일', week):
            genre_by_week = [random.choice([0,1,2])]
        elif re.search(r'화요일', week):
            genre_by_week = [random.choice([3,4])]
        elif re.search(r'수요일', week):
            genre_by_week = [random.choice([5,6,7])]
        elif re.search(r'목요일', week):
            genre_by_week = [random.choice([8,9])]
        elif re.search(r'금요일', week):
            genre_by_week = [random.choice([10,11,12])]
        elif re.search(r'토요일', week):
            genre_by_week = [random.choice([13,14])]
        else:
            genre_by_week = [random.choice([15,16,17])]
        return Movie.objects.filter(genre__in = genre_by_week)[:20]
    queryset = week()
    serializer_class = MovieListSerializer