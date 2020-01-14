import unittest
import selection_sort

class SelectionSortTests(unittest.TestCase):

    def test_numbers_are_sorted_correctly(self): 
        numbers_to_sort = [11,2,7,3,8,4,5,6,10,9,1]
        expected_sorted_numbers = [1,2,3,4,5,6,7,8,9,10,11]
        actual_sorted_numbers = selection_sort.sort(numbers_to_sort)

        self.assertEquals(expected_sorted_numbers, actual_sorted_numbers)


if __name__ == '__main__':
    unittest.main()
