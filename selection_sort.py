# Selection sort doesn't perform very well from a complexity standpoint, but it sorts in place sooooo it might be helpful if you are 
# doing systems level development against small hardware? 


def sort(array_to_sort):
    print(range(0, len(array_to_sort) - 1))
    


    # inspect each element in the array in order 
    for sort_index in range(0, len(array_to_sort) - 1):
        print("Current Pass")
        print(array_to_sort)
        print(f"Current Element is {array_to_sort[sort_index]}")
        index_of_current_min = sort_index

        print(range(sort_index + 1, len(array_to_sort)))
        # search all unsorted elements for an element smaller than the current element (at sort_index). 
        # I don't understand why we want the range to be 0 + 1 to n instead of 0 to n - 1.
        for search_index in range(sort_index + 1, len(array_to_sort)):
            print(f"Comparing {array_to_sort[search_index]} to {array_to_sort[index_of_current_min]}")
            
            # if we found a smaller value, save it as the new min
            if (array_to_sort[search_index] < array_to_sort[index_of_current_min]):
                print(f"Current Min is {array_to_sort[search_index]}")
                index_of_current_min = search_index

        # swap the smallest value we found with the current sort element
        print(f"Swapping {array_to_sort[sort_index]} and {array_to_sort[index_of_current_min]}")
        min_value = array_to_sort[index_of_current_min]
        array_to_sort[index_of_current_min] = array_to_sort[sort_index]
        array_to_sort[sort_index] = min_value
    
    return array_to_sort

