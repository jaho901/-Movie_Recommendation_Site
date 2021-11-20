from rest_framework import serializers, status
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes

from django.shortcuts import get_object_or_404

from rest_framework.permissions import AllowAny, IsAuthenticated

from .serializers import MovieSerializer, ReviewSerializer, GenreSerializer
from .models import Movie, Review, Genre


@api_view(['GET'])
def movie_all(request):
    movies = Movie.objects.all()
    serializer = MovieSerializer(movies, many=True)
    return Response(serializer.data)


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
def movie_like(request, movie_id):
    movie = get_object_or_404(Movie, pk=movie_id)
    if movie.like_users.filter(pk=request.user.pk).exists():
        movie.like_users.remove(request.user)
    else:
        movie.like_users.add(request.user)
    serializer = MovieSerializer(movie)
    return Response(serializer.data)


@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def review_list_create(request, movie_id):
    if request.method == 'GET':
        reviews = Review.objects.filter(movie=movie_id)
        serializer = ReviewSerializer(reviews, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        movie = get_object_or_404(Movie, pk=movie_id)
        serializer = ReviewSerializer(data=request.data)

        if serializer.is_valid(raise_exception=True):
            serializer.movie = movie
            serializer.user = request.user
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)


# @api_view(['GET'])
# # @permission_classes([IsAuthenticated])
# def movie_review(request):
#     reviews = Review.objects.all()
#     serializer = ReviewSerializer(reviews, many=False)
#     return Response(serializer.data)


# @api_view(['POST'])
# @permission_classes([IsAuthenticated])
# def movie_review_create(request, movie_id):
#     movie = get_object_or_404(Movie, pk=movie_id)
#     serializer = ReviewSerializer(data=request.data)

#     if serializer.is_valid(raise_exception=True):
#         serializer.movie = movie
#         serializer.save(user=request.user)
#         return Response(serializer.data)


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
def movie_review_delete(request, movie_id, review_pk):
    review = get_object_or_404(Review, pk=review_pk)
    review.delete()
    return Response('DELETE SUCCESS!')


@api_view(['GET'])
def genre_list(request):
    genres = Genre.objects.all()
    serializer = GenreSerializer(genres, many=True)
    return Response(serializer.data)
