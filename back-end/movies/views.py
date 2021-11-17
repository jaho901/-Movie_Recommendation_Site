from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from django.shortcuts import get_object_or_404

from .serializers import MovieSerializer
from .models import Movie


@api_view(['GET'])
def movie_list(request):
    movies = Movie.objects.all()
    # movies = request.user.movie_set.all()
    serializer = MovieSerializer(movies, many=True)
    return Response(serializer.data)
