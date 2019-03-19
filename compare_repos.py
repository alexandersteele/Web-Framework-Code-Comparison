import os
from git_clone import build_org_repos
from identify_framework import get_frameworks
from identify_endpoints import get_flask_endpoints
from identify_models import get_flask_model_classes, get_flask_model_field_names

# Returns result of two list intersection (matching)
def intersect(l1, l2): 
    return list(set(l1) & set(l2)) 

# User Input
build = input("Clone Repos? (Y or N): ")
if build == "Y":
    org = input("Enter name of organisation: ")
    build_org_repos(org)

print(" ")
print(" -------------------------- ")
print(" ")

# 2-Layer Repository Comparison Iteration

endpoint_threshold = input("Enter endpoint threshold value: ")
endpoint_threshold = int(endpoint_threshold)
model_classes_threshold = input("Enter model threshold value: ")
model_classes_threshold = int(model_classes_threshold)

repos = os.listdir('./cloned_repos/')
for repo in repos:
    frameworks = get_frameworks(repo) # Get frameworks from outer loop repo
    endpoints = get_flask_endpoints(repo) # Get endpoints from outer loop repo
    model_classes = get_flask_model_classes(repo) # Get models from outer loop repo
    model_field_names = get_flask_model_field_names(repo) # Get models from outer loop repo

    for other_repo in repos:
        if other_repo != repo: # Avoids self comparison
            other_frameworks = get_frameworks(other_repo) # Get frameworks from inner loop repo
            other_endpoints = get_flask_endpoints(other_repo) # Get endpoints from inner loop repo
            other_model_classes = get_flask_model_classes(other_repo) # Get model classes from inner loop repo
            other_model_field_names = get_flask_model_field_names(other_repo) # Get model field names from inner loop repo

            frameworks_intersect = intersect(frameworks, other_frameworks) # Matching frameworks
            endpoints_intersect = intersect(endpoints, other_endpoints) # Matching endpoints
            model_classes_intersect = intersect(model_classes, other_model_classes) # Matching model classes
            model_field_names_intersect = intersect(model_field_names, other_model_field_names) # Matching model classes
            
            # Calculate matching endpoint percentage
            if len(endpoints_intersect) > 0:
                endpoints_percent = (len(endpoints_intersect) / len(other_endpoints)) * 100
            else:
                endpoints_percent = 0

            # Calculate matching model classes percentage
            if len(model_classes_intersect) > 0:
                model_classes_percent = (len(model_classes) / len(other_model_classes)) * 100
            else:
                model_classes_percent = 0

             # Calculate matching model field name percentage
            if len(model_field_names_intersect) > 0:
                model_field_names_percent = (len(model_field_names) / len(other_model_field_names)) * 100
            else:
                model_field_names_percent = 0

            # Output for repos with matching framework(s) and endpoints(s)      
            if len(frameworks_intersect) > 0 and endpoints_percent >= endpoint_threshold:

                print(" ")
                print(" --------- " + repo + " compared to " + other_repo + " ----------- ")
                print(" ")

                print("Matching frameworks : ", end=" ")
                for match in frameworks_intersect:
                    if match:
                        print(match, end=" ")
                print(" ")
                print(" ")
                print("-- Endpoint Matches --")
                print("Matching endpoints: " + str(endpoints_percent) + "%", end=" ")
                print(" ")
                print(" ")
                for match in endpoints_intersect:
                    if match:
                        print(match, end=" ")
                        print(" ")
                print(" ")
                print(" ")

                if (model_classes_percent >= model_classes_threshold):
                    print("-- Model Matches --")
                    print("Matching model classes: " + str(model_classes_percent) + "%", end=" ")
                    print(" ")
                    print(" ")
                    
                    for match in model_classes_intersect:
                        if match:
                            print(match, end=" ")
                            print(" ")
                    print(" ")


                    print("Matching model field names: " + str(model_field_names_percent) + "%", end=" ")
                    print(" ")
                    print(" ")
                    
                    for match in model_field_names_intersect:
                        if match:
                            print(match, end=" ")
                            print(" ")
                    print(" ")



                print(" ")
                print(" -------------------------- ")
                print(" ")
