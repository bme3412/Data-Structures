############################
###    Selection Sort    ###
############################ 


### Selection sort is a simple sorting algorithm that divides the array into two parts: the sorted portion and the unsorted portion

### It repeatedly selects the smallest element from the unsorted portion and adds it to the end of the sorted portion until the entire array is sorted

    ### Start with an unsorted array

    ### Find the minimum element in the unsorted portion of the array

    ### Swap the minimum element with the first element of the unsorted portion

    ### Move the boundary between the sorted and unsorted portions one element to the right

    ### Repeat until sorted

def selection_sort(arr):
    n = len(arr) ## determine length of the array
    
    # Traverse through all array elements - Outer Loop; represents the boundary between sorted v unsorted
    for i in range(n - 1):
        
        # Find the minimum element in the unsorted portion
        min_index = i
        for j in range(i + 1, n): ## Inner Loop - finds the min element in unsorted
            if arr[j] < arr[min_index]:  # conditional logic
                min_index = j
        
        # Swap the minimum element with the first element of the unsorted portion
        arr[i], arr[min_index] = arr[min_index], arr[i]
    
    return arr

array_example = [1,5,2,3,12,9]
print(selection_sort(array_example))

arr_2 = [64, 34, 25, 12, 22, 11, 90]
print("Unsorted array:", arr_2)

sorted_arr_2 = selection_sort(arr_2)
print("Sorted array:", sorted_arr_2)


### Time Complexity
    # O(n^2)
    ### The number of swaps is always O(n) because each element is swapped only once

### Space Complexity
    # O(1) because it requires only a constant amount of additional memory space; 
    ## The sorting is done in-place