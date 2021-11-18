from rest_framework import serializers, status
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes

from django.shortcuts import get_object_or_404

from rest_framework.permissions import AllowAny, IsAuthenticated

from .serializers import MovieSerializer, ReviewSerializer
from .models import Movie, Review


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


@api_view(['GET'])
def movie_detail(request, movie_id):
    movie = get_object_or_404(Movie, pk=movie_id)
    serializer = MovieSerializer(movie)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def movie_review(request, movie_id):
    review = get_object_or_404(Review, pk=movie_id)
    serializer = ReviewSerializer(review, many=False)
    return Response(serializer.data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def movie_review_create(request, movie_id):
    movie = get_object_or_404(Movie, pk=movie_id)
    serializer = ReviewSerializer(data=request.data)

    if serializer.is_valid(raise_exception=True):
        serializer.movie = movie
        serializer.user = request.user
        serializer.save()
        return Response(serializer.data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def movie_review_update(request, movie_id, review_pk):
    movie = get_object_or_404(Movie, pk=movie_id)
    review = get_object_or_404(Review, pk=review_pk)
    serializer = ReviewSerializer(instance=review, data=request.data)

    if serializer.is_valid():
        serializer.movie = movie
        serializer.save()
        return Response(serializer.data)
    else:
        return Response(False)


@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def movie_review_delete(request, review_pk):
    review = get_object_or_404(Review, pk=review_pk)
    review.delete()
    return Response('DELETE SUCCESS!')