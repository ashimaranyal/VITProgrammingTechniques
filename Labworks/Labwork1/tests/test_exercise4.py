import unittest
from students.exercise4 import exercise4


class TestExercise4(unittest.TestCase):
    def test_empty_array(self):
        self.assertEqual(exercise4([], 1), [])

    def test_value_not_found(self):
        self.assertEqual(exercise4([1, 2, 3], 4), [])

    def test_value_found_once(self):
        self.assertEqual(exercise4([1, 2, 3, 2, 4], 3), [2])

    def test_value_found_multiple_times(self):
        self.assertEqual(exercise4([1, 2, 3, 2, 4, 2], 2), [1, 3, 5])
