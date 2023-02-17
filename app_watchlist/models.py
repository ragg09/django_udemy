from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.
class StreamPlatforms(models.Model):
    name = models.CharField(max_length=30)
    about = models.CharField(max_length=150)
    website = models.URLField(max_length=100)
    def __str__(self):
        return self.name

class WatchList(models.Model):
    title = models.CharField(max_length=50)
    storyline = models.CharField(max_length=200)
    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    # relationship | onet-to-one | watchlist has one streaming platform
    # the related_name must be used in the serializer as the variable name for the relationship
    platform = models.ForeignKey(StreamPlatforms, on_delete=models.CASCADE, related_name="watchlist")
    def __str__(self):
        return self.title
    
class Review(models.Model):
    rating = models.PositiveBigIntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    description = models.CharField(max_length=200, null=True)
    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    watchlist = models.ForeignKey(WatchList, on_delete=models.CASCADE, related_name="reviews")
    
    def __str__(self):
        return str(self.rating) + " | " + self.watchlist.title