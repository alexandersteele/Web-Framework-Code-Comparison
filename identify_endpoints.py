import os

def get_flask_endpoints(repo):
    endpoints_list = []

    files = os.listdir('./cloned_repos/' + repo)
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

            for line in f.readlines():
                line = line.rstrip()
                if "@app.route" in line:
                    endpoints_list.append(line)

    return endpoints_list

