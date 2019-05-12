from django.shortcuts import render
from django.contrib.auth import authenticate, login
from rest_framework import viewsets
from .models import NewsStory, Author, User
from .serializers import StorySerializer
import requests
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
import json

## Serialize story data
class StoryView(viewsets.ModelViewSet):
    queryset = NewsStory.objects.all()
    serializer_class = StorySerializer


## API login handling
@csrf_exempt
def user_login(request):

    if (request.method == 'POST'):
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if (user is not None):
            login(request, user)
            if (user.is_authenticated):

                return HttpResponse("Welcome " + username, status=200, content_type="text/plain")
            else:
                return HttpResponse("Failed authentication", status=400, content_type="text/plain")
        else:
            return HttpResponse("User not found", status=400, content_type="text/plain")


## API logout handling
@csrf_exempt
def user_logout(request):
    if (request.method == 'POST'):
        return HttpResponse("Goodbye", status=200, content_type="text/plain")
    else:
        return HttpResponse("Error logging out", status=400, content_type="text/plain")


## API post story to DB
@csrf_exempt
def post_story(request):

    if (request.method == 'POST'):

        data = json.loads(request.body)

        headline = data['headline']
        category = data['category']
        region = data['region']
        details = data['details']

        if (request.user.is_authenticated):
            
            user = User.objects.get(username=request.user)
            author = Author.objects.get(user = user)

            story = NewsStory(author=author, headline=headline, story_cat=category, story_region=region, story_details=details)
            story.save()
            return HttpResponse("Success", status=201, content_type="text/plain")
        else:
            return HttpResponse("Story could not be created", status=503, content_type="text/plain")


## API delete story from DB
@csrf_exempt
def delete_story (request):
    if (request.method == 'POST'):

        id = request.POST.get('id')

        if (request.user.is_authenticated):
            story = NewsStory.objects.get(key=id)
            story.delete()
            return HttpResponse("Story deleted", status=201, content_type="text/plain")
        else:
            return HttpResponse("Story could not be deleted", status=503, content_type="text/plain")    


## API get stories from DB
@csrf_exempt
def get_stories(request):
    if (request.method == 'GET'):

        # Handle get request data
        category = request.GET.get('story_cat')
        region = request.GET.get('story_region')
        date = request.GET.get('story_date')


        stories = NewsStory.objects.all() # Fetch stories

        # Filter by category, region and date
        if (category != "*"):
            stories = stories.filter(story_cat=category)
        if (region != "*"):
            stories = stories.filter(story_region=region)
        if (date != "*"):
            stories = stories.filter(story_date=date) 

        # Validation and serialization
        if (stories):
            serializer = StorySerializer(stories, many=True)
            output = json.dumps(serializer.data)
            return HttpResponse(output, status=200, content_type="application/json")
        else:
            return HttpResponse(stories, status=404, content_type="text/plain")
