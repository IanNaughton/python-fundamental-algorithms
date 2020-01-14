# So bubble sort isn't really the greatest--but it might show up on an interview! 

def sort(numbers_to_sort):
    last_array_index = len(numbers_to_sort) - 1

    # make n-1 passes over the array--we want this number of passes specifically because we need at least the number of passes
    # it would take for the first element to make it to the end of the list or vice-versa 
    for current_pass in range(0, last_array_index):
        print(f"Pass #{current_pass}")

        # Compare each element in the array to it's neighbor to the right
        for index_to_compare in range(0, last_array_index):
            left_item = numbers_to_sort[index_to_compare]
            right_item = numbers_to_sort[index_to_compare + 1]

            # Swap the item we are comparing with it's neighbor to the right 
            if (left_item > right_item): 
                numbers_to_sort[index_to_compare] = right_item
                numbers_to_sort[index_to_compare + 1] = left_item
                print(f"Swapped {left_item} and {right_item}")

        print(f"Pass #{current_pass}: {numbers_to_sort}")
    
    return numbers_to_sort

    