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

repo1 = input("Enter a repo to evaluate: ")
repo2 = input("Enter another repo to evaluate and compare: ")

print(" ")



#main repo
print(" ")
print(" --------- " + repo1 + " ----------- ")
print(" ")

print("Language(s):  ", end=" ")
for language in get_languages(repo1):
    if language:
        print(language, end=" ")
print(" ")

frameworks = get_frameworks(repo1)

print("Framework(s): ", end=" ")
for framework in frameworks:
    if framework:
        print(framework, end=" ")
        
print(" ")

if "Flask" in frameworks:
    print("")
    print("Identifying Flask Endpoint(s):")

    for endpoints in get_flask_endpoints(repo1):
        print(endpoints)

print(" ")



# other repo
print(" ")
print(" --------- " + repo2 + " ----------- ")
print(" ")

print("Language(s):  ", end=" ")
for language in get_languages(repo2):
    if language:
        print(language, end=" ")
print(" ")

other_frameworks = get_frameworks(repo2)

print("Framework(s): ", end=" ")
for framework in other_frameworks:
    if framework:
        print(framework, end=" ")

if "Flask" in other_frameworks:
    print("")
    print("Identifying Flask Endpoint(s):")

    for endpoints in get_flask_endpoints(repo2):
        print(endpoints)
        
print(" ")

print(" ")
print(" -------------------------- ")
print(" ")


# compare

frameworks_intersect = intersect(frameworks, other_frameworks)

print("Matching frameworks: ", end=" ")
for match in frameworks_intersect:
    if match:
        print(match, end=" ")
print(" ")

print(" ")
print(" -------------------------- ")
print(" ")




