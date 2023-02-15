# serializers map all values in a dictionary
# serializers eliminate the manually creating  a dictionary in the view
from app_watchlist.models import WatchList, StreamPlatforms
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
class WatchListSerializer(serializers.ModelSerializer):
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
    class Meta:
        model = StreamPlatforms
        fields = "__all__"
   
        
    
