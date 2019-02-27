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


repo = input("Enter a repo to evaluate: ")
print(" ")

# main repo
print(" ")
print(" --------- " + repo + " ----------- ")
print(" ")

print("Language(s):  ", end=" ")
for language in get_languages(repo):
    if language:
        print(language, end=" ")
print(" ")

frameworks = get_frameworks(repo)

print("Framework(s): ", end=" ")
for framework in frameworks:
    if framework:
        print(framework, end=" ")

if "Flask" in frameworks:
    print("")
    print("Identifying Flask Endpoint(s):")

    for endpoints in get_flask_endpoints(repo):
        print(endpoints)
        
print(" ")

contine = input("Press enter to continue")

print(" ")
print(" -------------------------- ")
print(" ")


# other repo
other_repos = os.listdir('./cloned_repos/')
for other_repo in other_repos:
    print(" ")
    print(" --------- " + other_repo + " ----------- ")
    print(" ")
    
    print("Language(s):  ", end=" ")
    for language in get_languages(other_repo):
        if language:
            print(language, end=" ")
    print(" ")

    other_frameworks = get_frameworks(other_repo)

    print("Framework(s): ", end=" ")
    for framework in other_frameworks:
        if framework:
            print(framework, end=" ")

    print(" ")

    if "Flask" in other_frameworks:
        print("")
        print("Identifying Flask Endpoint(s):")

        for endpoints in get_flask_endpoints(other_repo):
            print(endpoints)
        print(" ")

    frameworks_intersect = intersect(frameworks, other_frameworks)

    print("Matching frameworks: ", end=" ")
    for match in frameworks_intersect:
        if match:
            print(match, end=" ")
    print(" ")

    print(" ")
    print(" -------------------------- ")
    print(" ")











