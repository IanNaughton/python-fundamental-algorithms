import unittest
import merge_sort

class MergeSortTests(unittest.TestCase):

    def test_sort_results_are_in_order(self):
        array_to_sort = [7, 1, 11, 3, 5, 2, 9, 10, 8, 4, 6]
        sorted_array = merge_sort.sort(array_to_sort)
        expected_sort_results = [11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
        
        self.assertEqual(expected_sort_results, sorted_array)

if __name__ == '__main__':
    unittest.main()
