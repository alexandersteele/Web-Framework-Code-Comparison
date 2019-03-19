import os


# Get Python Flask endpoints
def get_flask_endpoints(repo):
    endpoints_list = []

    files = os.listdir('./cloned_repos/' + repo)

    #Iterate through files
    for file in files:
        if os.path.isdir('./cloned_repos/' + repo + '/' + file):
            if file == "flask":
                break
            for endpoints in get_flask_endpoints(repo + '/' + file):
                if endpoints not in endpoints_list:
                    endpoints_list.append(endpoints)

        filename, file_ext = os.path.splitext('./cloned_repos/' + repo + '/' + file)
        if file_ext == '.py':
            f = open('./cloned_repos/' + repo + '/' + file, "r", errors='replace')

            # Iterate through file lines
            for line in f.readlines():
                line = line.rstrip()
                if "@app.route" in line: # Search for "@app.route" endpoints
                    endpoints_list.append(line)

    return endpoints_list

