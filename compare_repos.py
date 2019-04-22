import os
from git_clone import build_org_repos
from identify_framework import get_frameworks
from identify_endpoints import get_flask_endpoints, get_django_endpoints
from identify_models import get_flask_model_classes, get_flask_model_field_names, get_django_model_classes, get_django_model_field_names

repositories = []

class Repository:

    def __init__(self, name, frameworks, endpoints, models, model_fields):
        self.name = name
        self.frameworks = frameworks
        self.endpoints = endpoints
        self.models = models
        self.model_fields = model_fields


def percentage(l1, l2):
    if (len(l1) > 0):
        return (len(l1) / len(l2)) * 100
    else:
        return 0


# User Input
build = input("Clone Repos? (Y or N): ")
if build == "Y":
    org = input("Enter name of organisation: ")
    build_org_repos(org)

framework_threshold = int(input("Enter framework threshold value: "))
endpoint_threshold = int(input("Enter endpoint threshold value: "))
models_threshold = int(input("Enter model class threshold value: "))
model_fields_threshold = int(input("Enter model fields threshold value: "))

print(" ")
print(" -------------------------- ")
print(" ")

repos = os.listdir('./cloned_repos/')
for repo in repos:
    frameworks = get_frameworks(repo) # Get frameworks from outer loop repo

    endpoints = []
    models = []
    model_fields = []

    # Flask analysis
    endpoints.extend(get_flask_endpoints(repo)) # Get endpoints from outer loop repo
    models.extend(get_flask_model_classes(repo)) # Get model classes from outer loop repo
    model_fields.extend(get_flask_model_field_names(repo)) # Get models from outer loop repo

    #Django analysis
    endpoints.extend(get_django_endpoints(repo))
    models.extend(get_django_model_classes(repo)) 
    #print(get_django_model_field_names(repo))
    model_fields.extend(get_django_model_field_names(repo))


    #Laravel analysis

    #ReactJS analysis

    #AngularJS analysis





    repositories.append(Repository(repo, frameworks, endpoints, models, model_fields))


# 2-Layer Repository Comparison Iteration
for repo in repositories:
    for other_repo in repositories:
        if other_repo != repo:
            frameworks_intersect = list(set(repo.frameworks) & set(other_repo.frameworks)) # Matching frameworks
            endpoints_intersect = list(set(repo.endpoints) & set(other_repo.endpoints)) # Matching endpoints
            models_intersect = list(set(repo.models) & set(other_repo.models)) # Matching model classes
            model_fields_intersect = list(set(repo.model_fields) & set(other_repo.model_fields)) # Matching model fields

            frameworks_percent = percentage(frameworks_intersect, other_repo.frameworks)
            endpoints_percent = percentage(endpoints_intersect, other_repo.endpoints)
            models_percent = percentage(models_intersect, other_repo.models)
            model_fields_percent = percentage(model_fields_intersect, other_repo.model_fields)

            # Output for repos with matching framework(s) and endpoints(s)      
            if (frameworks_percent >= framework_threshold and len(frameworks_intersect) > 0):
                print("---- " + repo.name + " compared to " + other_repo.name + " ----")
                print("Matching frameworks:" + str(frameworks_percent) + "%")
                for match in frameworks_intersect:
                    if match:
                        print(match)
                print("\n")
                
                print("Matching endpoints:"  + str(endpoints_percent) + "%")
                if (endpoints_percent >= endpoint_threshold):
                    for match in endpoints_intersect:
                        if match:
                            print(match)
                print("\n")
                    
                print("Matching model classes: " + str(models_percent) + "%")
                if (models_percent >= models_threshold):
                    for match in models_intersect:
                        if match:
                            print(match)
                print("\n\n")

                print("Matching model fields: " + str(model_fields_percent) + "%")
                if (model_fields_percent >= model_fields_threshold):
                    for match in model_fields_intersect:
                        if match:
                            print(match)
                print("\n\n")