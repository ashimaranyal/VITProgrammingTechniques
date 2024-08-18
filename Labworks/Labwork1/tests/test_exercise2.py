import unittest
from students.exercise2 import exercise2  

class TestExercise2(unittest.TestCase):
    def test_empty_array(self):
        self.assertEqual(exercise2([]), 0)

    def test_single_element_array(self):
        self.assertEqual(exercise2([5]), 5)

    def test_multiple_elements_array(self):
        self.assertEqual(exercise2([2, 4, 6]), 4)

    def test_negative_numbers(self):
        self.assertEqual(exercise2([-2, 1, -3]), -4 / 3)
