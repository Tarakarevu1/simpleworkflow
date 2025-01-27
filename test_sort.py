import unittest
from sort import bubble_sort

class TestBubbleSort(unittest.TestCase):
    def test_sorted_array(self):
        self.assertEqual(bubble_sort([5, 6, 8, 10, 1, 2, 3, 7]), [1, 2, 3, 5, 6, 7, 8, 10])
    
    def test_empty_array(self):
        self.assertEqual(bubble_sort([]), [])
    
    def test_reverse_sorted_array(self):
        self.assertEqual(bubble_sort([10, 9, 8, 7, 6, 5]), [5, 6, 7, 8, 9, 10])

    def test_already_sorted_array(self):
        self.assertEqual(bubble_sort([1, 2, 3, 7]), [1, 2, 3, 7])
        
    def test_duplicate_elements_array(self):
        self.assertEqual(bubble_sort([3, 1, 2, 3, 1]), [1, 1, 2, 3, 3])

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestBubbleSort)
    result = unittest.TextTestRunner(verbosity=2).run(suite)
    print(f"\nTotal tests run: {result.testsRun}")
    print(f"Total tests failed: {len(result.failures)}")
    print(f"Total tests errors: {len(result.errors)}")
    print(f"Total tests skipped: {len(result.skipped)}")
