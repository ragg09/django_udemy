from django.urls import path, include
# from app_watchlist.api.views import movie_list, movie_details
from app_watchlist.api.views import MovieListAV, MovieDetailAV

urlpatterns = [
    # function-based urlpatterns
    # path('list/', movie_list, name="movie-list"),
    # path('<int:id>', movie_details, name="movie-details"),
    
    #class-based urlpatterns
    path('list/', MovieListAV.as_view(), name="movie-list"),
    path('<int:id>', MovieDetailAV.as_view(), name="movie-details"),
]
