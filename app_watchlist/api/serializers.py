# serializers map all values in a dictionary
# serializers eliminate the manually creating  a dictionary in the view
from app_watchlist.models import Movie
from rest_framework import serializers

# for convention, if you are creating serializer for a model simpley do this format, ModelNameSerializer
class MovieSerializer(serializers.Serializer):
    # mapping the values should be like this.
    # if the porperty is not editable, make sure to define the readonly
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField()
    description = serializers.CharField()
    active = serializers.BooleanField()
    
    # create function, it receives validated data only, you can see the implementation in the views.py->POST method
    def create(self, validated_data):
        return Movie.objects.create(**validated_data)
    
    # instance has the old value of a particular ID
    # validated data is now carrying the new and updated values
    def update(self, instance, validated_data):
        # updating data 
        instance.name = validated_data.get('name', instance.name)
        instance.description = validated_data.get('description', instance.description)
        instance.active = validated_data.get('active', instance.active)
        instance.save()
        return instance
    
