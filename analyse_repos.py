import os
from identify_framework import get_frameworks
from identify_endpoints import get_django_endpoints, get_flask_endpoints, get_laravel_endpoints
from identify_models import get_django_model_classes, get_django_model_field_names, get_flask_model_classes, get_flask_model_field_names, get_laravel_model_classes, get_laravel_model_field_names

class Repository:

    def __init__(self, name, frameworks, endpoints, models, model_fields):
        self.name = name
        self.frameworks = frameworks
        self.endpoints = endpoints
        self.models = models
        self.model_fields = model_fields

def analyse_repositories():

    repositories = []

    repos = os.listdir('./cloned_repos/')
    for repo in repos:

        print("Analysing: " + repo + " repository")

        frameworks = get_frameworks(repo) # Get frameworks from outer loop repo

        endpoints = []
        models = []
        model_fields = []

        if "Flask" in frameworks:
            # Flask analysis
            endpoints.extend(get_flask_endpoints(repo)) # Get endpoints from outer loop repo
            models.extend(get_flask_model_classes(repo)) # Get model classes from outer loop repo
            model_fields.extend(get_flask_model_field_names(repo)) # Get models from outer loop repo

        if "Django" in frameworks:
            #Django analysis
            endpoints.extend(get_django_endpoints(repo))
            models.extend(get_django_model_classes(repo)) 
            model_fields.extend(get_django_model_field_names(repo))
        
        if "Laravel" in frameworks:
            # Laravel analysis
            endpoints.extend(get_laravel_endpoints(repo))
            models.extend(get_laravel_model_classes(repo))
            model_fields.extend(get_laravel_model_field_names(repo))

        repositories.append(Repository(repo, frameworks, endpoints, models, model_fields))

    return repositories