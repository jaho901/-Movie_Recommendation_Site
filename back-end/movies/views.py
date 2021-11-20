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

    # 같은 장르의 영화 최신순 10개 받아오기
    genre = movie.genre.all().values_list('id', flat=True)
    similar_movies = Movie.objects.filter(genre__id__in=genre).prefetch_related('genre').distinct()[:15]
    for i in range(15):
        if movie == similar_movies[i]:
            de_id = similar_movies[i].pk
    # print(similar_movies.id)

    similar_serializer = MovieSerializer(similar_movies, many=True)
    context = {
        "movie": serializer.data,
        "similar_movies": similar_serializer.data,
    }
    return Response(context)


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


@api_view(['GET'])
def movie_by_genre(request):
    adventure_movies = Movie.objects.filter(genre=0)
    war_movies = Movie.objects.filter(genre=1)
    musical_movies = Movie.objects.filter(genre=2)
    action_movies = Movie.objects.filter(genre=3)
    animation_movies = Movie.objects.filter(genre=4)
    criminal_movies = Movie.objects.filter(genre=5)
    comedy_movies = Movie.objects.filter(genre=6)
    drama_movies = Movie.objects.filter(genre=7)
    suspense_movies = Movie.objects.filter(genre=8)
    fantasy_movies = Movie.objects.filter(genre=9)
    romance_movies = Movie.objects.filter(genre=10)
    thriller_movies = Movie.objects.filter(genre=11)
    mystery_movies = Movie.objects.filter(genre=12)
    sf_movies = Movie.objects.filter(genre=13)
    horror_movies = Movie.objects.filter(genre=14)
    documentary_movies = Movie.objects.filter(genre=15)
    family_movies = Movie.objects.filter(genre=16)
    concert_movies = Movie.objects.filter(genre=17)
    adventure_serializer = MovieSerializer(adventure_movies, many=True)
    war_serializer = MovieSerializer(war_movies, many=True)
    musical_serializer = MovieSerializer(musical_movies, many=True)
    action_serializer = MovieSerializer(action_movies, many=True)
    animation_serializer = MovieSerializer(animation_movies, many=True)
    criminal_serializer = MovieSerializer(criminal_movies, many=True)
    comedy_serializer = MovieSerializer(comedy_movies, many=True)
    drama_serializer = MovieSerializer(drama_movies, many=True)
    suspense_serializer = MovieSerializer(suspense_movies, many=True)
    fantasy_serializer = MovieSerializer(fantasy_movies, many=True)
    romance_serializer = MovieSerializer(romance_movies, many=True)
    thriller_serializer = MovieSerializer(thriller_movies, many=True)
    mystery_serializer = MovieSerializer(mystery_movies, many=True)
    sf_serializer = MovieSerializer(sf_movies, many=True)
    horror_serializer = MovieSerializer(horror_movies, many=True)
    documentary_serializer = MovieSerializer(documentary_movies, many=True)
    family_serializer = MovieSerializer(family_movies, many=True)
    concert_serializer = MovieSerializer(concert_movies, many=True)
    context = {
        'adventureMovies': adventure_serializer.data,
        'warMovies': war_serializer.data,
        'musicalMovies': musical_serializer.data,
        'actionMovies': action_serializer.data,
        'animationMovies': animation_serializer.data,
        'criminalMovies': criminal_serializer.data,
        'comedyMovies': comedy_serializer.data,
        'dramaMovies': drama_serializer.data,
        'suspenseMovies': suspense_serializer.data,
        'fantasyMovies': fantasy_serializer.data,
        'romanceMovies': romance_serializer.data,
        'thrillerMovies': thriller_serializer.data,
        'mysteryMovies': mystery_serializer.data,
        'sfMovies': sf_serializer.data,
        'horrorMovies': horror_serializer.data,
        'documentaryMovies': documentary_serializer.data,
        'familyMovies': family_serializer.data,
        'concertMovies': concert_serializer.data,
    }
    return Response(context)