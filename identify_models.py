import os


# Get Python Flask model classes
def get_flask_model_classes(repo):
    model_classes_list = []

    files = os.listdir('./cloned_repos/' + repo)

    #Iterate through files
    for file in files:
        if os.path.isdir('./cloned_repos/' + repo + '/' + file):
            if file == "flask":
                break
            for models in get_flask_model_classes(repo + '/' + file):
                if models not in model_classes_list:
                    model_classes_list.append(models)

        filename, file_ext = os.path.splitext('./cloned_repos/' + repo + '/' + file)
        if file_ext == '.py':
            f = open('./cloned_repos/' + repo + '/' + file, "r", errors='replace')

            # Iterate through file lines
            for line in f.readlines():
                line = line.rstrip()
                if "db.Model" in line: # Search for "db.Model" models
                    model_classes_list.append(line)

    return model_classes_list

# Get Python Flask model field names
def get_flask_model_field_names(repo):
    model_fields_list = []

    files = os.listdir('./cloned_repos/' + repo)

    #Iterate through files
    for file in files:
        if os.path.isdir('./cloned_repos/' + repo + '/' + file):
            if file == "flask":
                break
            for models in get_flask_model_field_names(repo + '/' + file):
                if models not in model_fields_list:
                    model_fields_list.append(models)

        filename, file_ext = os.path.splitext('./cloned_repos/' + repo + '/' + file)
        if file_ext == '.py':
            f = open('./cloned_repos/' + repo + '/' + file, "r", errors='replace')

            model_file = False
            # Iterate through file lines
            for line in f.readlines():
                line = line.rstrip()
                if "db.Model" in line: # Search for "db.Model" models
                    model_file = True

            # Iterate through file lines
            if (model_file):
                for line in f.readlines():
                    line = line.rstrip()
                    if "db.Model" not in line: # Search for "db.Model" models
                        model_fields_list.append(line)
                        

    return model_fields_list