from django.urls import path
from . import views

app_name="movies"

urlpatterns = [
    path('', views.movie_all),
    path('movie_list/', views.movie_list),
    path('recent/', views.movie_list_recent),
    path('<int:movie_id>/', views.movie_detail),
    path('<int:movie_id>/review/', views.movie_review),
    path('<int:movie_id>/review/create/', views.movie_review_create),
    path('<int:movie_id>/review/<int:review_pk>/update/', views.movie_review_update),
    path('<int:movie_id>/review/<int:review_pk>/delete/', views.movie_review_delete),
    path('genre_list/', views.genre_list),
]
