import unittest
from students.exercise1 import student1

class TestStudent1(unittest.TestCase):
    def test_value_found(self):
        self.assertEqual(student1([1, 2, 3, 4], 3), 2)

    def test_value_not_found(self):
        self.assertEqual(student1([1, 2, 3, 4], 5), -1)

    def test_empty_array(self):
        self.assertEqual(student1([], 42), -1)

if __name__ == '__main__':
    unittest.main()