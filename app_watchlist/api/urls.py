from django.urls import path, include
# from app_watchlist.api.views import movie_list, movie_details
from app_watchlist.api.views import WatchListAV, WatchListDetailAV, StreamPlatformAV, StreamPlaformDetailAV

urlpatterns = [
    # function-based urlpatterns
    # path('list/', movie_list, name="movie-list"),
    # path('<int:id>', movie_details, name="movie-details"),
    
    #class-based urlpatterns
    path('list/', WatchListAV.as_view(), name="movie-list"),
    path('<int:id>', WatchListDetailAV.as_view(), name="movie-details"),
    path('stream/', StreamPlatformAV.as_view(), name="stream"),
    path('stream/<int:id>', StreamPlaformDetailAV.as_view(), name="stream-details")
]
