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
        if file_ext == '.css':
            if "CSS" not in languages:
                languages.append("CSS")

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

        # Check file extension for language, run framework detection method corresponding to language
        filename, file_ext = os.path.splitext('./cloned_repos/' + repo + '/' + file)
        filepath = './cloned_repos/' + repo + '/' + file
        if file_ext == '.py' or file_ext == '.pyc':
            get_pyframe = get_python_framework(filepath)
            if get_pyframe not in frameworks and get_pyframe is not None:
                frameworks.append(get_pyframe)
        if file_ext == '.js':
            get_jsframe = get_javascript_framework(filepath)
            if get_jsframe not in frameworks  and get_jsframe is not None:
                frameworks.append(get_jsframe)
    return frameworks


def get_python_framework(filepath):
    f = open(filepath, "r", errors='replace')

    # Loop through file lines searching for Python Framework indicator
    for line in f.readlines():
        line = line.lower().rstrip()
        if "import flask" in line:
            return "Flask"
        if "import django" in line:
            return "Django"


def get_javascript_framework(filepath):
    f = open(filepath, "r", errors='replace')

    # Loop through file lines searching for JS Framework indicator
    for line in f.readlines():
        # AngularJS1
        if "angular.module" in line:
            return "AngularJS1"
        
        # ReactJS
        if "import" in line and "react" in line:
            return "ReactJS"

    
