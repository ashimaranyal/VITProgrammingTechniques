import unittest
from students.exercise5 import exercise5

class TestExercise5(unittest.TestCase):
    def test_value_found(self):
        res, _ = exercise5([1, 2, 3, 4], 3)
        self.assertEqual(res, 2)

    def test_value_not_found(self):
        res, _ = exercise5([1, 2, 3, 4], 5)
        self.assertEqual(res, -1)

    def test_empty_array(self):
        res, _ = exercise5([], 42)
        self.assertEqual(res, -1)
        
    def test_complexity_8(self):
        res, nb = exercise5([1, 1, 1, 1, 1, 1, 1, 1], 42)
        self.assertEqual(res, -1)
        self.assertLessEqual(nb, 4)

    def test_complexity_16(self):
        res, nb = exercise5([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 42)
        self.assertEqual(res, -1)
        self.assertLessEqual(nb, 5)
