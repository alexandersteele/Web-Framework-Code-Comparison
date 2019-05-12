import os


# Get frameworks from identifed programming language
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

        # Check file extension for language and run framework detection method corresponding to language
        file_ext = os.path.splitext('./cloned_repos/' + repo + '/' + file)[-1]
        filepath = './cloned_repos/' + repo + '/' + file

        # Python
        if file_ext == '.py':
            get_pyframe = get_python_framework(filepath)
            if get_pyframe not in frameworks and get_pyframe is not None:
                frameworks.append(get_pyframe)
        
        # JavaScript
        if file_ext == '.js':
            get_jsframe = get_javascript_framework(filepath)
            if get_jsframe not in frameworks  and get_jsframe is not None:
                frameworks.append(get_jsframe)
        
        # PHP
        if file_ext == '.php':
            get_phpframe = get_php_framework(filepath)
            if get_phpframe not in frameworks  and get_phpframe is not None:
                frameworks.append(get_phpframe)
    return frameworks


# Get Python web frameworks
def get_python_framework(filepath):
    f = open(filepath, "r", errors='replace')

    # Loop through file lines searching for Python Framework indicator
    for line in f.readlines():
        line = line.lower().rstrip()

        # Flask
        if "import flask" in line:
            f.close()
            return "Flask"

        # Django
        if "import django" in line:
            f.close()
            return "Django"
    f.close()


# Get JavaScript web frameworks
def get_javascript_framework(filepath):
    f = open(filepath, "r", errors='replace')

    # Loop through file lines searching for JS Framework indicator
    for line in f.readlines():

        # AngularJS1
        if "angular.module" in line:
            f.close()
            return "AngularJS1"
        
        # ReactJS
        if "import" in line and "react" in line:
            f.close()
            return "ReactJS"
    f.close()


# Get PHP web frameworks
def get_php_framework(filepath):
    f = open(filepath, "r", errors='replace')

    # Loop through file lines searching for PHP Framework indicator
    for line in f.readlines():

        # Laravel
        if "Illuminate\\" in line:
            f.close()
            return "Laravel"
    f.close()