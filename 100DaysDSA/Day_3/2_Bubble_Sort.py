############################
###     Bubble Sort      ###
############################ 

### Bubble sort is a simple and intuitive sorting algorithm that repeatedly steps through the array, compares adjacent elements, and swaps them if they are in the wrong order. 
    
    ### The process is repeated until the array is sorted

def bubble_sort(arr):
    n = len(arr) # determine length of array
    
    # Traverse through all array elements -- Outer Loop
    for i in range(n - 1):
        
        # Last i elements are already in place -- Inner Loop
        for j in range(n - i - 1):
            
            # Swap if the element found is greater than the next element
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    
    return arr

## uses 2 nested loops:
    ## i = Outer Loop; the # of loops required to iterate through the array
    ## i = length of the array less 1, because once it reaches the end of the array, there is no element to compare it to
    ## j = Inner Loop; compares adjacent elements and swaps if in the wrong order
    ## why is range == (n- i -1)? n = length of the array; i is the index of the outer loop - so it compares how many elemetns are left as the loop is in process, and -1 bc it goes up to the last element

arr = [64, 34, 25, 12, 22, 11, 90]
print("Unsorted array:", arr)

sorted_arr = bubble_sort(arr)
print("Sorted array:", sorted_arr)

### Time Complexity
    # worst case = O(n^2) == if array in reverse order and needs to perform max # of swaps
    # best case = O(n) == if array is already sorted, and there is only 1 pass w/o any swaps

### Space Complexity
    # O(1) - requires a constant array of memory space; the sorting is done in place

### not efficient for large datasets, due to the quadratic time complexity