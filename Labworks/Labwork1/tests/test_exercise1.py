import unittest
from students.exercise1 import exercise1

class TestExercise1(unittest.TestCase):
    def test_value_found(self):
        self.assertEqual(exercise1([1, 2, 3, 4], 3), 2)

    def test_value_not_found(self):
        self.assertEqual(exercise1([1, 2, 3, 4], 5), -1)

    def test_empty_array(self):
        self.assertEqual(exercise1([], 42), -1)
