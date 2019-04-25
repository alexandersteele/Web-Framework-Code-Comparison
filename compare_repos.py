import os
import sys
from git_clone import build_org_repos
from analyse_repos import analyse_repositories, Repository

def percentage(l1, l2):
    if (len(l1) > len(l2)):
        return 100.0
    elif (len(l1) > 0):
        return (len(l1) / len(l2)) * 100
    else:
        return 0.0

if __name__ == '__main__':
    
    # Flag input
    if len(sys.argv) == 1:
        framework_threshold = endpoint_threshold = models_threshold = model_fields_threshold = 0
    elif len(sys.argv) != 5:
        print("threshold values for: framework, endpoint, model class and model fields must either all be included, or not at all")
        exit(1)
    else:
        framework_threshold = int(sys.argv[1])
        endpoint_threshold = int(sys.argv[2])
        models_threshold = int(sys.argv[3])
        model_fields_threshold = int(sys.argv[4])

    # User Input
    build = input("Clone Repos? (Y or N): ")
    if build == "Y":
        org = input("Enter name of organisation: ")
        build_org_repos(org)



    print(" ")
    print(" -------------------------- ")
    print(" ")

    repositories = analyse_repositories()
    
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
                    
                    
                    if (endpoints_percent >= endpoint_threshold):
                        print("Matching endpoints:"  + str(endpoints_percent) + "%")
                        for match in endpoints_intersect:
                            if match:
                                print(match)
                        print("\n")
                        
                    
                    if (models_percent >= models_threshold):
                        print("Matching model classes: " + str(models_percent) + "%")
                        for match in models_intersect:
                            if match:
                                print(match)
                        print("\n\n")

                    
                    if (model_fields_percent >= model_fields_threshold):
                        print("Matching model fields: " + str(model_fields_percent) + "%")
                        for match in model_fields_intersect:
                            if match:
                                print(match)
                        print("\n\n")
                    
