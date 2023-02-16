from rest_framework.response import Response
from app_watchlist.models import WatchList, StreamPlatforms
from app_watchlist.api.serializers import WatchListSerializer, StreamPlatformsSerializer
from rest_framework import status
from rest_framework.views import APIView
# from rest_framework.decorators import api_view



# CLASS-BASED VIEWS ONLY AHEAD =============================================================================================
class WatchListAV(APIView):
    
    def get(self, request):
        movies = WatchList.objects.all() # get complex data
        # when we are getting multiple objects, we need to define the many=true since it needs map every queryset
        serializer = WatchListSerializer(movies, many=True) # serialized, map all data
        return Response(serializer.data)
    
    def post(self, request):
        serializer = WatchListSerializer(data=request.data)
        # validator
        if serializer.is_valid():
            # .save() method is called referenced to the create method in the serializer since the request method is POST
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
        
        
class WatchListDetailAV(APIView):
    # def validate_request(self, id):
    #     # try catch to check if id exists
    #     try:
    #         WatchList.objects.get(id=id)
    #     except WatchList.DoesNotExist:
    #         return Response({'error': 'Movie not found'}, status=status.HTTP_404_NOT_FOUND)    
    
    def get(self, request, id): 
        # self.validate_request(self, id=id)
        movie = WatchList.objects.get(id=id)
        if request.method == 'GET':
            serializer = WatchListSerializer(movie)
            return Response(serializer.data)
        
    def put(self, request, id):
        movie = WatchList.objects.get(id=id)
        # take note that we also pass the selected data in the serializer since our update need that instance of the old data
        serializer = WatchListSerializer(movie, data=request.data)
        if serializer.is_valid():
            # .save() method is called referenced to the update method in the serializer since the request method is PUT
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
        
    def delete(self, request, id):
        movie = WatchList.objects.get(id=id)
        # this delete is a queryset method, it has nothing to do with serializer 
        WatchList.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    
    
class StreamPlatformAV(APIView):
    
    def get(self, request):
        platform = StreamPlatforms.objects.all()
        serializer = StreamPlatformsSerializer(platform, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = StreamPlatformsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
        
class StreamPlaformDetailAV(APIView):
  
    def get(self, request, id): 
        stream = StreamPlatforms.objects.get(id=id)
        if request.method == 'GET':
            serializer = StreamPlatformsSerializer(stream)
            return Response(serializer.data)
        
    def put(self, request, id):
        stream = StreamPlatforms.objects.get(id=id)
        # take note that we also pass the selected data in the serializer since our update need that instance of the old data
        serializer = StreamPlatformsSerializer(stream, data=request.data)
        if serializer.is_valid():
            # .save() method is called referenced to the update method in the serializer since the request method is PUT
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
        
    def delete(self, request, id):
        movie = StreamPlatforms.objects.get(id=id)
        # this delete is a queryset method, it has nothing to do with serializer 
        StreamPlatforms.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
        
      
# CLASS-BASED VIEWS ONLY ABOVE =============================================================================================        








# # FUNCTION-BASED VIEWS ONLY AHEAD =============================================================================================

# #NOTE: every request requires a request method, 
# # the decorato @api_view provides that for us

# # @api_view(['GET']) # by defaul, api_view decorator is GET method you can actually leave it blank
# # def movie_list(request):
# #     movies = WatchList.objects.all() # get complex data
# #     # when we are getting multiple objects, we need to define the many=true since it needs map every queryset
# #     serializer = WatchListSerializer(movies, many=True) # serialized, map all data
# #     return Response(serializer.data)


# @api_view(['GET', 'POST']) # by defaul, api_view decorator is GET method you can actually leave it blank
# def movie_list(request):
#     if request.method == 'GET':
#         movies = WatchList.objects.all() # get complex data
#         # when we are getting multiple objects, we need to define the many=true since it needs map every queryset
#         serializer = WatchListSerializer(movies, many=True) # serialized, map all data
#         return Response(serializer.data)
    
#         # return Response({
#         #     'message': 'Get Data Successfully',
#         #     'data': serializer.data
#         # })
    
#     if request.method == 'POST':
#         # get data from clientside
        
#         serializer = WatchListSerializer(data=request.data)
        
#         # validator
#         if serializer.is_valid():
#             # .save() method is called referenced to the create method in the serializer since the request method is POST
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors)


# # since these methods are using ID, to make the code cleaner, we can just merge it all in one function
# @api_view(['GET', 'PUT', 'DELETE']) 
# def movie_details(request, id):
#     # try catch to check if id exists
#     try:
#         movie = WatchList.objects.get(id=id)
#     except WatchList.DoesNotExist:
#         return Response({'error': 'Movie not found'}, status=status.HTTP_404_NOT_FOUND)
    
#     if request.method == 'GET':
#         serializer = WatchListSerializer(movie)
#         return Response(serializer.data)
    
#     if request.method == 'PUT':
#         # take note that we also pass the selected data in the serializer since our update need that instance of the old data
#         serializer = WatchListSerializer(movie, data=request.data)
#         if serializer.is_valid():
#             # .save() method is called referenced to the update method in the serializer since the request method is PUT
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors)
            
#     if request.method == 'DELETE': 
#         movie = WatchList.objects.get(id=id)
#         # this delete is a queryset method, it has nothing to do with serializer 
#         WatchList.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
    
# # FUNCTION-BASED VIEWS ONLY ABOVE =============================================================================================