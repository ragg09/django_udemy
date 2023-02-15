# serializers map all values in a dictionary
# serializers eliminate the manually creating  a dictionary in the view
from app_watchlist.models import Movie
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
class MovieSerializer(serializers.ModelSerializer):
    # custom field, it is not in the model itself but this create a field in the serializer
    # the json response will now have a field named len_name
    # you can use custom fields via creating a get method, get_len_name(self, object)
    name_len = serializers.SerializerMethodField()
    
    class Meta:
        model = Movie
        fields = "__all__"
        
        # you can define field manually, it can be handy for selecting specific filed and excluduing other
        # by defining fields, you can implement inline validators
        # fields = [
        #     'id',
        #     'name',
        #     'description',
        #     'active'
        # ]
    
    # this return a value for a custom field declared above
    # note ~ the function name must be 'get_<custom_field_name>(self, obj)'    
    def get_name_len(self, obj):
        return len(obj.name)
        
    # Field-level validation
    # take note that you are refenrencing a field via using the proper field name you declared
    # see example below, validate_fieldName 
    def validate_name(self, value):
        if len(value) < 2:
            raise serializers.ValidationError("Name is too short")
        return value
        
    # Object-level validation
    # it check all of the field properties of your object
    def validate(self, data):
        if data['name'] == data['description']:
            raise serializers.ValidationError("Title and Description Cannot Be The Same")
        return data
        
    


# # for convention, if you are creating serializer for a model simpley do this format, ModelNameSerializer
# class MovieSerializer(serializers.Serializer):
#     # mapping the values should be like this.
#     # if the porperty is not editable, make sure to define the readonly
#     id = serializers.IntegerField(read_only=True)
#     name = serializers.CharField()
#     description = serializers.CharField()
#     active = serializers.BooleanField()
    
#     # create function, it receives validated data only, you can see the implementation in the views.py->POST method
#     def create(self, validated_data):
#         return Movie.objects.create(**validated_data)
    
#     # instance has the old value of a particular ID
#     # validated data is now carrying the new and updated values
#     def update(self, instance, validated_data):
#         # updating data 
#         instance.name = validated_data.get('name', instance.name)
#         instance.description = validated_data.get('description', instance.description)
#         instance.active = validated_data.get('active', instance.active)
#         instance.save()
#         return instance
    
#     # Field-level validation
#     # take note that you are refenrencing a field via using the proper field name you declared
#     # see example below, validate_fieldName 
#     def validate_name(self, value):
#         if len(value) < 2:
#             raise serializers.ValidationError("Name is too short")
#         return value
    
#     # Object-level validation
#     # it check all of the field properties of your object
#     def validate(self, data):
#         if data['name'] == data['description']:
#             raise serializers.ValidationError("Title and Description Cannot Be The Same")
#         return data
    
