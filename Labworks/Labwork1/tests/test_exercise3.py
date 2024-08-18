import unittest
from students.exercise3 import exercise3


class TestExercise3(unittest.TestCase):
    def test_empty_array(self):
        with self.assertRaises(ValueError):
            exercise3([])

    def test_single_element_array(self):
        self.assertEqual(exercise3([5]), (5, 5))

    def test_multiple_elements_array(self):
        self.assertEqual(exercise3([2, 4, 1, 6, 3]), (1, 6))

    def test_negative_numbers(self):
        self.assertEqual(exercise3([-2, 1, -3, 4]), (-3, 4))
