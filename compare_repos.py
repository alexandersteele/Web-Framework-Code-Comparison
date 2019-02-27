from git_clone import build_org_repos
from identify_framework import get_languages, get_frameworks
from identify_endpoints import get_flask_endpoints

build = input("Clone Repos? (Y or N): ")
if build == "Y":
    org = input("Enter name of organisation: ")
    build_org_repos(org)

repo = input("Enter a repo to evaluate: ")

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
print(" ")

if "Flask" in frameworks:
    print("")
    print("Identifying Flask Endpoint(s):")

    for endpoints in get_flask_endpoints(repo):
        print(endpoints)




