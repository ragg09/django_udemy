from rest_framework.response import Response
from app_watchlist.models import WatchList, StreamPlatforms, Review
from app_watchlist.api.serializers import WatchListSerializer, StreamPlatformsSerializer, ReviewSerializer
from rest_framework import status
from rest_framework.views import APIView
# from rest_framework.decorators import api_view

# #for MIXIN
# from rest_framework import generics
# from rest_framework import mixins

#for Concrete View Class
from rest_framework import generics

#for viewset
from rest_framework import viewsets
from django.shortcuts import get_object_or_404

# CONCRETE CLASS VIEWS ONLY AHEAD =============================================================================================
# concret class view is almost the same with mixin, the only difference is that all the methods are already included in generics
# meaning, you dont need to define them manually
# just import the methods from generics and it will do the work
# it is shorter than mixin
# generic actually uses mixin too, but it is done behind the scenes

# non-overwritten queryset
# class ReviewList(generics.ListCreateAPIView):
#     queryset = Review.objects.all()
#     serializer_class = ReviewSerializer

# queryset overwrite
class ReviewList(generics.ListAPIView):
    serializer_class = ReviewSerializer
    
    def get_queryset(self):
        pk = self.kwargs['pk']
        return Review.objects.filter(watchlist=pk)
    
class ReviewCreate(generics.CreateAPIView):
    # queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    
    # since the url uses the watchlist ID, by creating this one, we will save the hassle of sending watchlist ID to the review
    # another thing about this, since we are now selecting directly the ID of watchlist, we dont need it to the request
    # it will be a conflict since in review, we require that ID,
    # to solve that, in the serialize, instead of using fields = "__all__", just use exclude('field_name',)
    def perform_create(self, serializer):
        pk = self.kwargs.get('pk')
        movie = WatchList.objects.get(pk=pk)
        
        # you can add logic here before saving the data
        
        serializer.save(watchlist=movie)

    
class ReviewDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
       
    
# CONCRETE CLASS VIEWS ONLY ABOVE =============================================================================================







# # GENERICAPIVIEW AND MIXIN VIEWS ONLY AHEAD =============================================================================================
# # in this example I only used ListModelMixin and CreateModelMixin it is used for retrieving and creating
# # but you can perform entire CRUD using this just see the documentation
# # https://www.django-rest-framework.org/api-guide/generic-views/#mixins
# # note! generics.GenericAPIView must always be the last argument
# class ReviewList(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
#     # these two variables are attribute name
#     # meaning, you cant change it to any variable based on the documentation
#     queryset = Review.objects.all()
#     serializer_class = ReviewSerializer

#     # this uses the ListModelMixin
#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)

#     # this uses the CreateModelMixin
#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)
    
# class ReviewDetail(mixins.RetrieveModelMixin, generics.GenericAPIView):
#     # these two variables are attribute name
#     # meaning, you cant change it to any variable based on the documentation
#     queryset = Review.objects.all()
#     serializer_class = ReviewSerializer

#     # this uses the RetriveModelMixin
#     def get(self, request, *args, **kwargs):
#         return self.retrieve(request, *args, **kwargs)
    
#     # you can add your update and delete methods here
#     #
#     #

# # GENERICAPIVIEW AND MIXIN VIEWS ONLY ABOVE =============================================================================================

# VIEWSET ONLY AHEAD =============================================================================================

class StreamPlatformVS(viewsets.ViewSet):
    """
    This viewset automatically provides `list` and `retrieve` actions.
    """
    queryset = StreamPlatforms.objects.all()
    serializer_class = StreamPlatformsSerializer    
    
    def list(self, request):
        queryset = StreamPlatforms.objects.all()
        serializer = StreamPlatformsSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = StreamPlatforms.objects.all()
        watchlist = get_object_or_404(queryset, pk=pk)
        serializer = StreamPlatformsSerializer(watchlist)
        return Response(serializer.data)
    

# VIEWSET ONLY ABOVE =============================================================================================


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