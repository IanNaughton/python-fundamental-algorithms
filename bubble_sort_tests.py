import unittest
import bubble_sort

class BubbleSortTests(unittest.TestCase):

    def test_array_sort_results_are_in_order(self):
        array_to_sort = [11,2,4,9,5,3,1,6,8,10,7]
        sorted_array = bubble_sort.sort(array_to_sort)
        expected_array = [1,2,3,4,5,6,7,8,9,10,11]

        self.assertEqual(expected_array, sorted_array)

if __name__ == '__main__':
    unittest.main()