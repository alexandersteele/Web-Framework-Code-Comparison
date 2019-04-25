import os


# Get Python Flask endpoints
def get_flask_endpoints(repo):
    endpoints_list = []

    files = os.listdir('./cloned_repos/' + repo)

    #Iterate through files
    for file in files:
        if os.path.isdir('./cloned_repos/' + repo + '/' + file):
            if file == "flask":
                continue
            for endpoints in get_flask_endpoints(repo + '/' + file):
                if endpoints not in endpoints_list:
                    endpoints_list.append(endpoints)

        filename, file_ext = os.path.splitext('./cloned_repos/' + repo + '/' + file)
        if file_ext == '.py':
            f = open('./cloned_repos/' + repo + '/' + file, "r", errors='replace')

            # Iterate through file lines
            for line in f.readlines():
                line = line.strip()
                if "@app.route" in line: # Search for "@app.route" endpoints
                    endpoints_list.append(line)

    return endpoints_list

# Get Python Flask endpoints
def get_django_endpoints(repo):
    endpoints_list = []

    files = os.listdir('./cloned_repos/' + repo)

    #Iterate through files
    for file in files:
        if os.path.isdir('./cloned_repos/' + repo + '/' + file):
            for endpoints in get_django_endpoints(repo + '/' + file):
                if endpoints not in endpoints_list:
                    endpoints_list.append(endpoints)

        filename, file_ext = os.path.splitext('./cloned_repos/' + repo + '/' + file)
        if file_ext == '.py':
            f = open('./cloned_repos/' + repo + '/' + file, "r", errors='replace')

            # Iterate through file lines
            for line in f.readlines():
                line = line.strip()
                if "def" in line and "request" in line: # Search for function with request paramater for endpoints
                    endpoints_list.append(line)

    return endpoints_list

# Get Python Flask endpoints
def get_laravel_endpoints(repo):
    endpoints_list = []

    files = os.listdir('./cloned_repos/' + repo)

    #Iterate through files
    for file in files:
        if os.path.isdir('./cloned_repos/' + repo + '/' + file):
            for endpoints in get_laravel_endpoints(repo + '/' + file):
                if endpoints not in endpoints_list:
                    endpoints_list.append(endpoints)

        filename, file_ext = os.path.splitext('./cloned_repos/' + repo + '/' + file)
        if file_ext == '.php':
            f = open('./cloned_repos/' + repo + '/' + file, "r", errors='replace')

            # Iterate through file lines
            for line in f.readlines():
                line = line.strip()
                if "Route::get" in line or "Route::post" in line or "Route::delete" in line: # Search for function with request paramater for endpoints
                    endpoints_list.append(line)

    return endpoints_list
