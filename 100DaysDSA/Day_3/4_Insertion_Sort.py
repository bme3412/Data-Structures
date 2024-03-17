### Insertion sort is a simple sorting algorithm that builds the final sorted array one element at a time.

############################
###    Insertion Sort    ###
############################ 
    ### It divides the array into two parts: the sorted portion and the unsorted portion

    ### The algorithm iterates through the unsorted portion, taking one element at a time, and inserts it into its correct position in the sorted portion

def insertion_sort(arr):
    n = len(arr)
    
    # Traverse through all array elements
    for i in range(1, n):
        key = arr[i]    ### key = unsorted portion
        j = i - 1   ### j = last element in the sorted position
        
        # Move elements of sorted portion that are greater than key
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        
        # Insert the key into its correct position
        arr[j + 1] = key
    
    return arr

arr = [64, 34, 25, 12, 22, 11, 90]
print("Unsorted array:", arr)

sorted_arr = insertion_sort(arr)
print("Sorted array:", sorted_arr)


### Time Complexity
    ## worst/average cases = O(n^2)
    ## best cases = O(n) -- already sorted

### Space Complexity
    ## O(1) because it requires only a constant amount of additional memory space; the sorting is done in-place