import unittest
from sort import bubble_sort

class TestBubbleSort(unittest.TestCase):
    def test_sorted_array(self):
        self.assertEqual(bubble_sort([5, 6, 8, 10, 1, 2, 3, 7]), [1, 2, 3, 5, 6, 7, 8, 10])
    
    def test_empty_array(self):
        self.assertEqual(bubble_sort([]), [])
    
    def test_single_element_array(self):
        self.assertEqual(bubble_sort([1]), [1])
    
    def test_already_sorted_array(self):
        self.assertEqual(bubble_sort([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5])
    
    def test_reverse_sorted_array(self):
        self.assertEqual(bubble_sort([5, 4, 3, 2, 1]), [1, 2, 3, 4, 5])
    
    def test_duplicate_elements_array(self):
        self.assertEqual(bubble_sort([3, 1, 2, 3, 1]), [1, 1, 2, 3, 3])

if __name__ == '__main__':
    unittest.main()
