from git import Repo
import requests
import json
import os

# Connect to GitHub organisation
def connect_org_repos(org):
    r = requests.get('https://api.github.com/orgs/' + org + '/repos?type=all')
    if (r.ok):
        return json.loads(r.text or r.content)
    else:
        print("Unable to connect to organisation repositories")

# Clone repositories from GitHub organisation
def build_org_repos(org):
    for repo in connect_org_repos(org):
        if (os.path.isdir("cloned_repos/" + repo["name"])):
            g = Repo("cloned_repos/" + repo["name"])
            g.remotes.origin.pull()
        else:
            Repo.clone_from(repo["git_url"], 'cloned_repos/' + (repo["name"]))
