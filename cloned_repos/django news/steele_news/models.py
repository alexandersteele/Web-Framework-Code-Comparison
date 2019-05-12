from time import timezone
from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

class Author (models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name

class NewsStory (models.Model):
    author = models.ForeignKey('Author', on_delete=models.CASCADE)
    key = models.AutoField(primary_key=True)
    headline = models.CharField(max_length=64)
    story_cat = models.CharField(max_length=50)
    story_region = models.CharField(max_length=10)
    story_date = models.DateField(auto_now_add=True)
    story_details = models.CharField(max_length=512)

    def __str__(self):
        return self.headline