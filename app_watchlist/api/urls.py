from django.urls import path, include
from app_watchlist.api.views import movie_list, movie_details

urlpatterns = [
    path('list/', movie_list, name="movie-list"),
    path('<int:id>', movie_details, name="movie-details"),
]
