import os


# Get Python Flask endpoints
def get_flask_endpoints(repo):
    endpoints_list = []

    files = os.listdir('./cloned_repos/' + repo)

    #Iterate through files and folders
    for file in files:
        if os.path.isdir('./cloned_repos/' + repo + '/' + file):
            if file == "flask":
                continue
            for endpoints in get_flask_endpoints(repo + '/' + file):
                if endpoints not in endpoints_list:
                    endpoints_list.append(endpoints)

        # Check file is Python
        file_ext = os.path.splitext('./cloned_repos/' + repo + '/' + file)[-1]
        if file_ext == '.py':
            f = open('./cloned_repos/' + repo + '/' + file, "r", errors='replace')

            # Iterate through file lines
            for line in f.readlines():
                line = line.strip()
                
                # Search for "@app.route" endpoints
                if "@app.route" in line: 
                    endpoints_list.append(line)
            f.close()

    return endpoints_list

# Get Python Django endpoints
def get_django_endpoints(repo):
    endpoints_list = []

    files = os.listdir('./cloned_repos/' + repo)

    #Iterate through files and folders
    for file in files:
        if os.path.isdir('./cloned_repos/' + repo + '/' + file):
            for endpoints in get_django_endpoints(repo + '/' + file):
                if endpoints not in endpoints_list:
                    endpoints_list.append(endpoints)

        # Check file is Python
        file_ext = os.path.splitext('./cloned_repos/' + repo + '/' + file)[-1]
        if file_ext == '.py':
            f = open('./cloned_repos/' + repo + '/' + file, "r", errors='replace')

            # Iterate through file lines
            for line in f.readlines():
                line = line.strip()

                # Search for function with request paramater for endpoints
                if "def" in line and "request" in line:
                    endpoints_list.append(line)
            f.close()
            
    return endpoints_list

# Get PHP Laravel endpoints
def get_laravel_endpoints(repo):
    endpoints_list = []

    files = os.listdir('./cloned_repos/' + repo)

    #Iterate through files and folders
    for file in files:
        if os.path.isdir('./cloned_repos/' + repo + '/' + file):
            for endpoints in get_laravel_endpoints(repo + '/' + file):
                if endpoints not in endpoints_list:
                    endpoints_list.append(endpoints)

        # Check file is PHP
        file_ext = os.path.splitext('./cloned_repos/' + repo + '/' + file)[-1]
        if file_ext == '.php':
            f = open('./cloned_repos/' + repo + '/' + file, "r", errors='replace')

            # Iterate through file lines
            for line in f.readlines():
                line = line.strip()

                # Search for routing
                if "Route::get" in line or "Route::post" in line or "Route::delete" in line: 
                    endpoints_list.append(line)
            f.close()
            
    return endpoints_list


