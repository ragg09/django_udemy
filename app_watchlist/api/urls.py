from django.urls import path, include
# from app_watchlist.api.views import movie_list, movie_details
from app_watchlist.api.views import (
    WatchListAV, WatchListDetailAV, 
    StreamPlatformVS,
    StreamPlatformAV, 
    StreamPlaformDetailAV, 
    ReviewCreate,
    ReviewList, 
    ReviewDetail
)

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('stream', StreamPlatformVS, basename='streamplatform')
 
urlpatterns = [
    # function-based urlpatterns
    # path('list/', movie_list, name="movie-list"),
    # path('<int:id>', movie_details, name="movie-details"),
    
    #class-based urlpatterns
    path('list/', WatchListAV.as_view(), name="movie-list"),
    path('<int:id>/', WatchListDetailAV.as_view(), name="movie-details"),
    
    path('', include(router.urls)),
    
    # commented due to router lesson
    # path('stream/', StreamPlatformAV.as_view(), name="stream"),
    # path('stream/<int:id>', StreamPlaformDetailAV.as_view(), name="stream-details"),
    
    
    # get all reviews for specific movie
    path('<int:pk>/review-create/', ReviewCreate.as_view(), name="stream-review-create"),
    # get all reviews for specific movie
    path('<int:pk>/reviews/', ReviewList.as_view(), name="stream-reviews"),
    # get specific review for specific movie
    path('review/<int:pk>/', ReviewDetail.as_view(), name="stream-reviews-detail"),
    
    # path('review/', ReviewList.as_view(), name="review-list"),
    # #take note this, I used PK since we are using mixin, and by default, ID is PK
    # path('review/<int:pk>', ReviewDetail.as_view(), name="review-detail")
]
