from rest_framework import serializers
from .models import NewsStory

class StorySerializer(serializers.ModelSerializer):

    author_name = serializers.CharField(source='author.name')
    class Meta:
        
        model = NewsStory
        fields = ('key', 'author_name','headline', 'story_cat','story_region', 'story_details', 'story_date')