from django.shortcuts import render
from app_watchlist.models import Movie
from django.http import JsonResponse

# Create your views here.
# view in this context is a request handler and not an actual HTML template 

def movie_list(request):
   
    movies = Movie.objects.all() #queryset
    print(movies.values())
    
    data = {
        'movies': list(movies.values()),
        'tests': 'norem'
    }
    
    return JsonResponse(data) #convert dictionary to json
    
    
def movie_details(request, id):
    movie = Movie.objects.get(id=id)
    print(movie)
    
    data = {
        'name': movie.name,
        'description': movie.description,
        'active': movie.active,
    }
    
    return JsonResponse(data) #convert dictionary to json
