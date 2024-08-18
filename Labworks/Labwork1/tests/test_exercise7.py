import numpy as np
import unittest
from students.exercise7 import exercise7



class TestExercise7(unittest.TestCase):
        
    @staticmethod
    def generate_random_array_numpy(length, lower_bound, upper_bound):
        return np.random.randint(low=lower_bound, high=upper_bound+1, size=length)
    
    @staticmethod
    def is_sorted(array):
        if len(array) == 0: return True
        
        last = array[0]
        
        for value in array[1:]:
            if last > value: return False
            last = value
            
        return True
        

    def setUp(self):
        self.big_array = TestExercise7.generate_random_array_numpy(100, 1, 500)

    def test_empty_array(self):
        self.assertEqual(exercise7([]), [])

    def test_single_element_array(self):
        self.assertEqual(exercise7([5]), [5])

    def test_sorted_array(self):
        self.assertEqual(exercise7([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5])

    def test_unsorted_array(self):
        self.assertEqual(exercise7([5, 2, 4, 1, 3]), [1, 2, 3, 4, 5])

    def test_duplicate_elements(self):
        self.assertEqual(exercise7([3, 2, 3, 1, 2, 4]), [1, 2, 2, 3, 3, 4])
        
    def test_big_array(self):
        self.assertTrue(self.is_sorted(exercise7(self.big_array)))
