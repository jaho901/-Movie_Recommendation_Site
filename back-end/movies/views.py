from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from django.shortcuts import get_object_or_404

from .serializers import MovieSerializer
from .models import Movie


@api_view(['GET'])
def movie_list(request):
    movies = Movie.objects.all().order_by('-id')[723:]
    # movies = request.user.movie_set.all()
    serializer = MovieSerializer(movies, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def movie_list_recent(request):
    movies_recent = Movie.objects.all().order_by('-id')[623:723]
    # movies = request.user.movie_set.all()
    serializer = MovieSerializer(movies_recent, many=True)
    return Response(serializer.data)


