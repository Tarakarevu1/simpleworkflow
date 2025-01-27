import unittest
from search import search_ele

class TestSearchEle(unittest.TestCase):
    def test_element_found(self):
        self.assertEqual(search_ele([5, 6, 8, 10, 1, 2, 3, 7], 3), 6)
        self.assertEqual(search_ele([5, 6, 8, 10, 1, 2, 3, 7], 5), 0)
        self.assertEqual(search_ele([5, 6, 8, 10, 1, 2, 3, 7], 7), 7)

    def test_element_not_found(self):
        self.assertEqual(search_ele([5, 6, 8, 10, 1, 2, 3, 7], 4), -1)
        self.assertEqual(search_ele([], 1), -1)

    def test_single_element_array(self):
        self.assertEqual(search_ele([1], 1), 0)
        self.assertEqual(search_ele([1], 2), -1)

    def test_multiple_occurrences(self):
        self.assertEqual(search_ele([1, 2, 3, 2, 1], 2), 1)
        self.assertEqual(search_ele([1, 2, 3, 2, 1], 1), 0)

if __name__ == '__main__':
    unittest.main()
