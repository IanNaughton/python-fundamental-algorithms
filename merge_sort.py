# merge sort is probably the fastest sorting algorithm that 
# I'm aware of--DIVIDE AND CONQUOR BOII! 

# do the recursive part 
def sort(array_to_sort):

    # if the array elememts are completely split and the array only have one element, just return--no need for more recursion
    if len(array_to_sort) == 1:
        return array_to_sort

    # if the array has more than one element left, we need to split it 
    if len(array_to_sort) > 1:
        
        # important to note that integer division is happening here
        half = len(array_to_sort) // 2
        
        print("Split Arrays")
        print(array_to_sort[half:])
        print(array_to_sort[:half])

        # recursively call this method for each half of the array we split
        first_half = sort(array_to_sort[half:])
        second_half = sort(array_to_sort[:half])

        # merge the two halves of the arrays as the call stack unwinds 
        return _merge_arrays(first_half, second_half)

def _merge_arrays(first_half, second_half): 

    merged_list = []

    print("Merging Lists")
    print(first_half)
    print(second_half)

    total_length_of_first_and_second_half = len(first_half) + len(second_half)

    # sort by popping the first element off of one of the two lists that was passed in
    while len(merged_list) < total_length_of_first_and_second_half:
        
        if both_lists_have_elements(first_half, second_half):
        
            if (first_half[0] > second_half[0]): 
                print(f"Taking {first_half[0]}")
                merged_list.append(first_half.pop(0))
        
            else:
                print(f"Taking {second_half[0]}")
                merged_list.append(second_half.pop(0))
        
        elif only_first_list_has_elements(first_half, second_half) :
            print(f"Taking {first_half[0]}")
            merged_list.append(first_half.pop(0)) 
        
        elif only_second_list_has_elements(first_half, second_half) :
            print(f"Taking {second_half[0]}")
            merged_list.append(second_half.pop(0)) 

    print("Finished Merging Lists")
    print(merged_list)
    return merged_list


def both_lists_have_elements(first_half, second_half):
    return (len(first_half) > 0) and (len(second_half) > 0)

def only_first_list_has_elements(first_half, second_half):
    return (len(first_half) > 0) and (len(second_half) == 0)

def only_second_list_has_elements(first_half, second_half): 
    return (len(second_half) > 0) and (len(first_half) == 0)