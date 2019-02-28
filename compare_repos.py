import os
from git_clone import build_org_repos
from identify_framework import get_languages, get_frameworks
from identify_endpoints import get_flask_endpoints

def intersect(lst1, lst2): 
    return list(set(lst1) & set(lst2)) 

build = input("Clone Repos? (Y or N): ")
if build == "Y":
    org = input("Enter name of organisation: ")
    build_org_repos(org)

print(" ")
print(" -------------------------- ")
print(" ")


repos = os.listdir('./cloned_repos/')
for repo in repos:
    frameworks = get_frameworks(repo)
    endpoints = get_flask_endpoints(repo)

    # other repo
    other_repos = os.listdir('./cloned_repos/')
    for other_repo in other_repos:

        if other_repo != repo:

            other_frameworks = get_frameworks(other_repo)
            other_endpoints = get_flask_endpoints(other_repo)


            frameworks_intersect = intersect(frameworks, other_frameworks)
            endpoints_intersect = intersect(endpoints, other_endpoints)
            
            if len(endpoints_intersect) > 0:
                endpoints_percent = (len(endpoints_intersect) / len(other_endpoints)) * 100
            else:
                endpoints_percent = 0
                    

            if len(frameworks_intersect) > 1 and endpoints_percent > 0:

                print(" ")
                print(" --------- " + repo + " compared to " + other_repo + " ----------- ")
                print(" ")

                print("Matching frameworks : ", end=" ")
                for match in frameworks_intersect:
                    if match:
                        print(match, end=" ")
                print(" ")

                
                print("Matching endpoints with: " + str(endpoints_percent) + "%", end=" ")
                print(" ")
                for match in endpoints_intersect:
                    if match:
                        print(match, end=" ")
                        print(" ")
                print(" ")

                print(" ")
                print(" -------------------------- ")
                print(" ")

