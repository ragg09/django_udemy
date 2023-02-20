# serializers map all values in a dictionary
# serializers eliminate the manually creating  a dictionary in the view
from app_watchlist.models import WatchList, StreamPlatforms, Review
from rest_framework import serializers

"""
    A `ModelSerializer` is just a regular `Serializer`, except that:
    * A set of default fields are automatically populated.
    * A set of default validators are automatically populated.
    * Default `.create()` and `.update()` implementations are provided.
    The process of automatically determining a set of serializer fields
    based on the model fields is reasonably complex, but you almost certainly
    don't need to dig into the implementation.
    If the `ModelSerializer` class *doesn't* generate the set of fields that
    you need you should either declare the extra/differing fields explicitly on
    the serializer class, or simply use a `Serializer` class.
"""
class ReviewSerializer(serializers.ModelSerializer):
    review_user = serializers.StringRelatedField(read_only=True)
    class Meta:
        model = Review
        exclude = ('watchlist',)
        # fields = "__all__"

class WatchListSerializer(serializers.ModelSerializer):
    
    # NESTED Serializers = Return all fields
    # since watchlist has a relationship in streamplatform (see in model for reference)
    # the varaible name here is very crucial, it must be the same to what you declared in the related_name in model
    # this code allow you to display all movies that is related to this platform
    # take note that this is a read only field, meaning, 
    # you dont need to actually pass it in your post request, but it will be visible in the get request
    reviews = ReviewSerializer(many=True, read_only=True)
    
    class Meta:
        model = WatchList
        fields = "__all__"
        
        # you can define field manually, it can be handy for selecting specific filed and excluduing other
        # by defining fields, you can implement inline validators
        # fields = [
        #     'id',
        #     'name',
        #     'description',
        #     'active'
        # ]
        
class StreamPlatformsSerializer(serializers.ModelSerializer):
    
    # NESTED Serializers = Return all fields
    # since watchlist has a relationship in streamplatform (see in model for reference)
    # the varaible name here is very crucial, it must be the same to what you declared in the related_name in model
    # this code allow you to display all movies that is related to this platform
    # take note that this is a read only field, meaning, 
    # you dont need to actually pass it in your post request, but it will be visible in the get request
    watchlist = WatchListSerializer(many=True, read_only=True)
    
    # # Serializer Relationships = return only the the string defined in the model
    # # other than defined field you can actually get just the ID, or a hyperlink
    # # see documentation for info: https://www.django-rest-framework.org/api-guide/relations/
    # watchlist = serializers.StringRelatedField(many=True, read_only=True)
    
    class Meta:
        model = StreamPlatforms
        fields = "__all__"
   
        
    
