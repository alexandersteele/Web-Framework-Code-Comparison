import os
import sys
from git_clone import build_org_repos
from analyse_repos import analyse_repositories, Repository
import time


# Method to calculate percentage of list1 in list2
def percentage(l1, l2):
    if (len(l1) > len(l2)):
        return 100.0
    elif (len(l1) > 0):
        return (len(l1) / len(l2)) * 100
    else:
        return 0.0


if __name__ == '__main__':
    
    # CLI Flags
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

    # Get list of analysed repositories
    repositories = analyse_repositories() 

    print(" ")
    print(" -------------------------- ")
    print(" ")

    compare_count = 0

    # 2-Layer Repository Comparison
    for repo in repositories:
        for other_repo in repositories:
            if other_repo != repo:
                frameworks_intersect = list(set(repo.frameworks) & set(other_repo.frameworks)) # Matching frameworks
                endpoints_intersect = list(set(repo.endpoints) & set(other_repo.endpoints)) # Matching endpoints
                models_intersect = list(set(repo.models) & set(other_repo.models)) # Matching model classes
                model_fields_intersect = list(set(repo.model_fields) & set(other_repo.model_fields)) # Matching model fields

                # Matching fundamental feature percentages
                frameworks_percent = percentage(frameworks_intersect, repo.frameworks) 
                endpoints_percent = percentage(endpoints_intersect, repo.endpoints)
                models_percent = percentage(models_intersect, repo.models)
                model_fields_percent = percentage(model_fields_intersect, repo.model_fields)

                # Output results if matching frameworks found     
                if (len(frameworks_intersect) > 0):
                    
                    # Output results if all matching results are within threshold values
                    if (frameworks_percent >= framework_threshold and endpoints_percent >= endpoint_threshold and 
                    models_percent >= models_threshold and model_fields_percent >= model_fields_threshold):

                        compare_count += 1

                        # Print matching frameworks
                        print("---- " + repo.name + " compared to " + other_repo.name + " ----")
                        print("Matching frameworks:" + str(frameworks_percent) + "%")
                        for match in frameworks_intersect:
                            if match:
                                print(match)
                        print("\n")

                        # Print matching endpoints
                        if (endpoints_percent >= endpoint_threshold):
                            print("Matching endpoints:"  + str(endpoints_percent) + "%")
                            for match in endpoints_intersect:
                                if match:
                                    print(match)
                            print("\n")
                        
                        # Print matching model classes
                        if (models_percent >= models_threshold):
                            print("Matching model classes: " + str(models_percent) + "%")
                            for match in models_intersect:
                                if match:
                                    print(match)
                            print("\n\n")
                        
                        # Print matching model fields
                        if (model_fields_percent >= model_fields_threshold):
                            print("Matching model fields: " + str(model_fields_percent) + "%")
                            for match in model_fields_intersect:
                                if match:
                                    print(match)
                            print("\n\n")
    
    print(" ")
    print(" -------------------------- ")
    print("Comparisons Output: " + str(compare_count))
    print(" -------------------------- ")
    print(" ")
