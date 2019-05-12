import unittest
from compare_repos import Repository, percentage
from git_clone import build_org_repos, connect_org_repos
from identify_framework import get_frameworks
from identify_endpoints import get_django_endpoints, get_flask_endpoints, get_laravel_endpoints
from identify_models import (get_django_model_classes, get_django_model_field_names, get_flask_model_classes,
get_flask_model_field_names, get_laravel_model_classes, get_laravel_model_field_names)
import identify_models


#
# Repository Analysis Unit tests
#
class TestAnalyseRepositories(unittest.TestCase):

    def test_name(self):
        self.assertEqual(Repository("r1", [], [], [], []).name,"r1")

    def test_framework(self):
        self.assertEqual(get_frameworks("laravelbasic1"), ["Laravel"])
        self.assertEqual(get_frameworks("angularsocial"), ["AngularJS1"])
        self.assertEqual(get_frameworks("djangonews"), ["Django"])
        self.assertEqual(get_frameworks("flasksocial"), ["Flask"])
        self.assertEqual(get_frameworks("flasktasks"), ["Flask", "AngularJS1"])
        self.assertEqual(get_frameworks("reactcalc"), ["ReactJS"])

    def test_endpoints(self):
        self.assertEqual(get_laravel_endpoints("laravelbasic1"), ["Route::get('/', function () {",
         "Route::post('/task', function (Request $request) {", "Route::delete('/task/{id}', function ($id) {"])

        self.assertEqual(get_django_endpoints("djangonews"), ["def user_login(request):", "def user_logout(request):",
         "def post_story(request):", "def delete_story (request):", "def get_stories(request):"])

        self.assertEqual(get_flask_endpoints("flasksocial"), ["@app.route('/', methods=['GET', 'POST'])",
         "@app.route('/register', methods=['GET', 'POST'])", "@app.route('/login', methods=['GET', 'POST'])", 
         "@app.route('/logout')", "@app.route('/settings', methods=['GET', 'POST'])"])

        self.assertEqual(get_flask_endpoints("flasktasks"), ["@app.route('/tasks', methods=['GET'])",
         "@app.route('/tasks/completed', methods=['GET'])", "@app.route('/tasks/uncompleted', methods=['GET'])",
          "@app.route('/task/<int:id>', methods=['GET'])", "@app.route('/task/<int:id>', methods=['DELETE'])",
           "@app.route('/task/<int:id>', methods=['PUT'])", "@app.route('/tasks', methods=['POST'])"])
    
    def test_model_classes(self):
        self.assertEqual(get_laravel_model_classes("laravelbasic1"), ["class Task extends Model",
         "class User extends Authenticatable"])

        self.assertEqual(get_django_model_classes("djangonews"), ["class Author (models.Model):",
         "class NewsStory (models.Model):"])
        
        self.assertEqual(get_flask_model_classes("flasksocial"), ["class FeedModel(db.Model):",
         "class RegisterModel(db.Model):"])

        self.assertEqual(get_flask_model_classes("flasktasks"), ["class Task(db.Model):"])

    def test_model_fields(self):
        self.assertEqual(get_laravel_model_field_names("laravelbasic1"), ["protected $fillable = [",
         "protected $hidden = ["])

        self.assertEqual(get_django_model_field_names("djangonews"), ["user = models.ForeignKey(User, on_delete=models.CASCADE)",
         "name = models.CharField(max_length=50)", "author = models.ForeignKey('Author', on_delete=models.CASCADE)",
          "key = models.AutoField(primary_key=True)", "headline = models.CharField(max_length=64)",
           "story_cat = models.CharField(max_length=50)", "story_region = models.CharField(max_length=10)",
            "story_date = models.DateField(auto_now_add=True)", "story_details = models.CharField(max_length=512)"])

        self.assertEqual(get_flask_model_field_names("flasksocial"), ["id = db.Column(db.Integer, primary_key=True)",
         "username = db.Column(db.String(500), index=True, unique=True)", "body = db.Column(db.String(500), index=True)",
          "date = db.Column(db.DateTime)", "password = db.Column(db.String(500), index=True, unique=True)"])

        self.assertEqual(get_flask_model_field_names("flasktasks"), ["id = db.Column(db.Integer, primary_key=True)",
         "title = db.Column(db.String(250), index=True)", "task = db.Column(db.String(5000),index=True)",
          "completed = db.Column(db.Boolean())", "owner = db.Column(db.String(500))"])


#   
# Percentage Function Unit Tests
#
class TestPercentage (unittest.TestCase):
    def test_percentage(self):
        self.assertEqual(percentage([1,2,3], [1,2,3,4,5]), 60)    
    
    def test_percentage_repo(self):
        # Repository set-up
        r1 = Repository("", ["f1", "f2"], [], [], [])
        r2 = Repository("", ["f1", "f2", "f3", "f4"], [], [], [])

        # Test repository r1 framework list against basic list
        self.assertEqual(percentage(r1.frameworks, [1,2,3,4]), 50)
        self.assertEqual(percentage([1,2,3,4], r1.frameworks), 100)

        # Test repository r2 framework list against basic list
        self.assertEqual(percentage(r2.frameworks, [1,2,3,4]), 100)
        self.assertEqual(percentage([1,2,3,4], r2.frameworks), 100)

        # Test repository r1 framework list against r2 framework list
        self.assertEqual(percentage(r2.frameworks, r1.frameworks), 100)
        self.assertEqual(percentage(r1.frameworks, r2.frameworks), 50)

    def test_percentage_boundaries(self):
        self.assertEqual(percentage([1,2,3,4,5], [1,2,3]), 100) # Upper boundary test (percentage <= 100)
        self.assertEqual(percentage([], [1,2,3,4,5]), 0) # Lower boundary test (percentage >= 0)
    
    def test_percentage_data_type(self):
        self.assertIsInstance(percentage([1,2,3,4], [1,2,3,4,5,6,7]), float) # Expected float = 57.142
        self.assertIsInstance(percentage([1,2,3], [1,2,3,4,5,6]), float) # Expected float = 50.0


#
# Git Cloning Unit Tests
#
class TestGitClone(unittest.TestCase):
    def setUp(self):
        self.repos = []
        for repo in connect_org_repos("DummyCorpv1"):
            self.repos.append(repo["name"])

    def test_connect_org_repos(self):
        self.assertEqual(self.repos[0], "student-1")
        self.assertEqual(self.repos[1], "student-2")
        self.assertEqual(self.repos[2], "student-3")

if __name__ == '__main__':
    unittest.main()
