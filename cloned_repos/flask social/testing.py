import os
import unittest
from app import app

def add(x,y):
    return x + y

class TestCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testHomeStatusCode(self):
        result = self.app.get('/')
        self.assertEqual(result.status_code, 200)


if __name__ == '__main__':
    unittest.main()
