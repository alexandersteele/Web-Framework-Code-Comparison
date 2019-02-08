import os


def get_languages(repo):
    languages = []  # Create list of languages

    # Loop through files
    files = os.listdir('./cloned_repos/' + repo)
    for file in files:
        
        # Recursively add languages from directories
        if os.path.isdir('./cloned_repos/' + repo + '/' + file):
            for language in get_languages(repo + '/' + file):
                if language not in languages:
                    languages.append(language)


        # File extension language checking
        filename, file_ext = os.path.splitext('./cloned_repos/' + repo + '/' + file)
        if file_ext == '.py' or file_ext == '.pyc':
            if "Python" not in languages:
                languages.append("Python")
        if file_ext == '.js':
            if "JavaScript" not in languages:
                languages.append("JavaScript")
        if file_ext == '.html':
            if "HTML" not in languages:
                languages.append("HTML")

    return languages  # return repo languages


def get_frameworks(repo):
    frameworks = []
    # Loop through files
    files = os.listdir('./cloned_repos/' + repo)
    for file in files:

        # Recursively add frameworks from directories
        if os.path.isdir('./cloned_repos/' + repo + '/' + file):
            for framework in get_frameworks(repo + '/' + file):
                if framework not in frameworks:
                    frameworks.append(framework)

        filename, file_ext = os.path.splitext('./cloned_repos/' + repo + '/' + file)
        filepath = './cloned_repos/' + repo + '/' + file
        if file_ext == '.py' or file_ext == '.pyc':
            if get_python_framework(filepath) not in frameworks:
                frameworks.append(get_python_framework(filepath))
        if file_ext == '.js':
            if get_python_framework(filepath) not in frameworks:
                frameworks.append(get_javascript_framework(filepath))
    return frameworks


def get_python_framework(filepath):

    python_framework = ""
    f = open(filepath, "r", errors='replace')

    for line in f.readlines():
        line = line.lower().rstrip()
        if "hello world" in line:
            python_framework = "n00b"
            break
        if "import flask" in line:
            python_framework = "Flask"
            break
        if "import django" in line:
            python_framework = "Django"

    return python_framework


def get_javascript_framework(filepath):
    javascript_framework = ""
    return javascript_framework
