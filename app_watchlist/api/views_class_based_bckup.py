from rest_framework.response import Response
from app_watchlist.models import Movie
from app_watchlist.api.serializers import MovieSerializer
from rest_framework import status
from rest_framework.views import APIView



# CLASS-BASED VIEWS ONLY AHEAD =============================================================================================
class MovieListAV(APIView):
    
    def get(self, request):
        movies = Movie.objects.all() # get complex data
        # when we are getting multiple objects, we need to define the many=true since it needs map every queryset
        serializer = MovieSerializer(movies, many=True) # serialized, map all data
        return Response(serializer.data)
    
    def post(self, request):
        serializer = MovieSerializer(data=request.data)
        # validator
        if serializer.is_valid():
            # .save() method is called referenced to the create method in the serializer since the request method is POST
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
        
        
class MovieDetailAV(APIView):
    # def validate_request(self, id):
    #     # try catch to check if id exists
    #     try:
    #         Movie.objects.get(id=id)
    #     except Movie.DoesNotExist:
    #         return Response({'error': 'Movie not found'}, status=status.HTTP_404_NOT_FOUND)    
    
    def get(self, request, id): 
        # self.validate_request(self, id=id)
        movie = Movie.objects.get(id=id)
        if request.method == 'GET':
            serializer = MovieSerializer(movie)
            return Response(serializer.data)
        
    def put(self, request, id):
        movie = Movie.objects.get(id=id)
        # take note that we also pass the selected data in the serializer since our update need that instance of the old data
        serializer = MovieSerializer(movie, data=request.data)
        if serializer.is_valid():
            # .save() method is called referenced to the update method in the serializer since the request method is PUT
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
        
    def delete(self, request, id):
        movie = Movie.objects.get(id=id)
        # this delete is a queryset method, it has nothing to do with serializer 
        movie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)      
# CLASS-BASED VIEWS ONLY ABOVE =============================================================================================        

