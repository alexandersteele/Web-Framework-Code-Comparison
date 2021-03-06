import os


# Get Python Flask model classes
def get_flask_model_classes(repo):
    model_classes_list = []

    files = os.listdir('./cloned_repos/' + repo)

    #Iterate through files and folders
    for file in files:
        if os.path.isdir('./cloned_repos/' + repo + '/' + file):
            if file == "flask":
                continue
            for models in get_flask_model_classes(repo + '/' + file):
                if models not in model_classes_list:
                    model_classes_list.append(models)

        # Check file is Python
        file_ext = os.path.splitext('./cloned_repos/' + repo + '/' + file)[-1]
        if file_ext == '.py':
            f = open('./cloned_repos/' + repo + '/' + file, "r", errors='replace')

            # Iterate through file lines
            for line in f.readlines():
                line = line.strip()
                if "db.Model" in line: # Search for "db.Model" model classes
                    model_classes_list.append(line)
            f.close()

    return model_classes_list


# Get Python Flask model field names
def get_flask_model_field_names(repo):
    model_fields_list = []

    files = os.listdir('./cloned_repos/' + repo)

    #Iterate through files and folders
    for file in files:
        if os.path.isdir('./cloned_repos/' + repo + '/' + file):
            if file == "flask":
                continue
                
            for models in get_flask_model_field_names(repo + '/' + file):
                if models not in model_fields_list:
                    model_fields_list.append(models)

        # Check file is Python
        file_ext = os.path.splitext('./cloned_repos/' + repo + '/' + file)[-1]
        if file_ext == '.py':
            f = open('./cloned_repos/' + repo + '/' + file, "r", errors='replace')

            # Iterate through file lines
            for line in f.readlines():
                line = line.strip()
                if "db.Column" in line: # Search for "db.Column" fields
                    model_fields_list.append(line)
            f.close()

    return model_fields_list


# Get Python Django model classes
def get_django_model_classes(repo):
    model_classes_list = []

    files = os.listdir('./cloned_repos/' + repo)

    #Iterate through files and folders
    for file in files:
        if os.path.isdir('./cloned_repos/' + repo + '/' + file):
            for models in get_django_model_classes(repo + '/' + file):
                if models not in model_classes_list:
                    model_classes_list.append(models)

        # Check file is Python
        file_ext = os.path.splitext('./cloned_repos/' + repo + '/' + file)[-1]
        if file_ext == '.py':
            f = open('./cloned_repos/' + repo + '/' + file, "r", errors='replace')

            # Iterate through file lines
            for line in f.readlines():
                line = line.strip()
                if "class" in line and "models.Model" in line: # Search for model classes
                    model_classes_list.append(line)
            f.close()

    return model_classes_list


# Get Python Django model field names
def get_django_model_field_names(repo):
    model_fields_list = []

    files = os.listdir('./cloned_repos/' + repo)

    #Iterate through files and folders
    for file in files:
        if os.path.isdir('./cloned_repos/' + repo + '/' + file):
            if file == "migrations":
                continue
            for models in get_django_model_field_names(repo + '/' + file):
                if models not in model_fields_list:
                    model_fields_list.append(models)

        # Check file is Python
        file_ext = os.path.splitext('./cloned_repos/' + repo + '/' + file)[-1]
        if file_ext == '.py':
            f = open('./cloned_repos/' + repo + '/' + file, "r", errors='replace')

            # Iterate through file lines
            for line in f.readlines():
                line = line.strip()
                if "models." in line and "class" not in line: # Search for model fields
                     model_fields_list.append(line)
            f.close()
    
    return model_fields_list


# get PHP Laravel model classes
def get_laravel_model_classes(repo):
    model_classes_list = []

    files = os.listdir('./cloned_repos/' + repo)

    #Iterate through files and folders
    for file in files:
        if os.path.isdir('./cloned_repos/' + repo + '/' + file):
            for models in get_laravel_model_classes(repo + '/' + file):
                if models not in model_classes_list:
                    model_classes_list.append(models)

        # Check file is PHP
        file_ext = os.path.splitext('./cloned_repos/' + repo + '/' + file)[-1]
        if file_ext == '.php':
            f = open('./cloned_repos/' + repo + '/' + file, "r", errors='replace')

            # Iterate through file lines
            for line in f.readlines():
                line = line.strip()
                if "extends Model" in line: # Search for model classes
                    model_classes_list.append(line)
            f.close()

    return model_classes_list


# Get PHP Laravel model field names
def get_laravel_model_field_names(repo):
    model_fields_list = []

    files = os.listdir('./cloned_repos/' + repo)

    #Iterate through files and folders
    for file in files:
        if os.path.isdir('./cloned_repos/' + repo + '/' + file):
            for models in get_laravel_model_field_names(repo + '/' + file):
                if models not in model_fields_list:
                    model_fields_list.append(models)

        # Check file is PHP
        file_ext = os.path.splitext('./cloned_repos/' + repo + '/' + file)[-1]
        if file_ext == '.php':
            f = open('./cloned_repos/' + repo + '/' + file, "r", errors='replace')

            # Iterate through file lines to find model class
            for line in f.readlines():
                line = line.strip()
                if "extends Model" in line:

                    # If model class found, restart and search for model fields
                    f.seek(0)

                    # Iterate through file lines
                    for line in f.readlines():
                        line = line.strip()
                        if "protected $" in line: # Search for model fields
                            model_fields_list.append(line)
            f.close()
    
    return model_fields_list