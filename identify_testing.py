import unittest
from compare_repos import Repository, percentage

# Unit tests
class TestRepository (unittest.TestCase):
    def test_name(self):
        self.assertEqual(Repository("r1", [], [], [], []).name,"r1")

#class TestCompareRepositories(self):
    

class TestPercentage (unittest.TestCase):
    def test_percentage(self):
        self.assertEqual(percentage([1,2,3], [1,2,3,4,5]), 60)    
    
    def test_percentage_repo(self):
        r1 = Repository("", ["f1", "f2"], [], [], [])
        r2 = Repository("", ["f1", "f2", "f3", "f4"], [], [], [])

        self.assertEqual(percentage(r1.frameworks, [1,2,3,4]), 50)
        self.assertEqual(percentage([1,2,3,4], r1.frameworks), 100)

        self.assertEqual(percentage(r2.frameworks, [1,2,3,4]), 100)
        self.assertEqual(percentage([1,2,3,4], r2.frameworks), 100)

        self.assertEqual(percentage(r2.frameworks, r1.frameworks), 100)
        self.assertEqual(percentage(r1.frameworks, r2.frameworks), 50)

    def test_percentage_boundaries(self):
        self.assertEqual(percentage([1,2,3,4,5], [1,2,3]), 100) # upper
        self.assertEqual(percentage([], [1,2,3,4,5]), 0) #lower
    
    def test_percentage_data_type(self):
        self.assertIsInstance(percentage([1,2,3,4], [1,2,3,4,5,6,7]), float) #57.142
        self.assertIsInstance(percentage([1,2,3], [1,2,3,4,5,6]), float) # 50.0



if __name__ == '__main__':
    unittest.main()
# Test individual Repository objects


# Integration tests