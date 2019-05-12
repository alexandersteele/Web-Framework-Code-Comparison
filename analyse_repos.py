import os
from identify_framework import get_frameworks
from identify_endpoints import get_django_endpoints, get_flask_endpoints, get_laravel_endpoints
from identify_models import (get_django_model_classes, get_django_model_field_names, get_flask_model_classes,
 get_flask_model_field_names, get_laravel_model_classes, get_laravel_model_field_names)


# Analysed repository class
class Repository:

    def __init__(self, name, frameworks, endpoints, models, model_fields):
        self.name = name
        self.frameworks = frameworks
        self.endpoints = endpoints
        self.models = models
        self.model_fields = model_fields


# Method to add analysis data into repository objects
def analyse_repositories():

    repositories = [] # List of repository objects

    # Loop through repositories in directory
    repos = os.listdir('./cloned_repos/')
    for repo in repos:

        print("Analysing: " + repo + " repository")

        frameworks = get_frameworks(repo) # Get frameworks of repository

        endpoints = [] # List of repository endpoints
        models = [] # List of repository classes
        model_fields = [] # List of repository fields

        #Flask repository analysis
        if "Flask" in frameworks:
            # Flask analysis
            endpoints.extend(get_flask_endpoints(repo)) # Add endpoints to list
            models.extend(get_flask_model_classes(repo)) # Add model classes to list
            model_fields.extend(get_flask_model_field_names(repo)) # Add model fields to list

        #Django repository analysis
        if "Django" in frameworks:
            #Django analysis
            endpoints.extend(get_django_endpoints(repo)) # Add endpoints to list
            models.extend(get_django_model_classes(repo)) # Add model classes to list
            model_fields.extend(get_django_model_field_names(repo)) # Add model fields to list

        #Laravel repository analysis     
        if "Laravel" in frameworks:
            # Laravel analysis
            endpoints.extend(get_laravel_endpoints(repo)) # Add endpoints to list
            models.extend(get_laravel_model_classes(repo)) # Add model classes to list
            model_fields.extend(get_laravel_model_field_names(repo)) # Add model fields to list

        # Create repository object from analysis data and add to repositories list
        repositories.append(Repository(repo, frameworks, endpoints, models, model_fields))

    return repositories # Return list of analysed repository objects