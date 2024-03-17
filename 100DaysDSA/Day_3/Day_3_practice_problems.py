# Practice Problems:

problem_1 = """Implement bubble sort, selection sort, and insertion sort in Python"""
problem_2 = """Analyze the time and space complexity of each sorting algorithm."""
problem_3 = """Compare the performance of the sorting algorithms on different input sizes and different initial orderings of the array."""
problem_4 = """Discuss the advantages and disadvantages of each sorting algorithm and when to use them."""


arrays = [64, 34, 25, 12, 22, 11, 90]

## 1. Bubble Sort

## What does Bubble Sort do?
    ## starts with first element, compares to element +1
    ## swaps if needed
    
def bubble_sort(arr):
    n = len(arr)

    for i in range(n-1):

        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
                arr[j+1], arr[j] = arr[j], arr[j+1]
            
    return arr

solution_1_bubble = bubble_sort(arrays)
print(f'Solution to 1 - bubble sort is: {solution_1_bubble}')

## Mnemonic = determine length of array; double-for loop; conditional and swap elements as needed
## Time Complexity = O(n^2) - 2 loops; O(n) if sorted
## Space Complexity = O(1) - sorts in place
### Would not perform well with large datasets based on quadratic time complexity
 
'------------------'


## 2. Selection Sort
    ## splits sorted vs unsorted; finds the minimum element in unsorted
    ## compares and swaps as needed


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


solution_2_selection = selection_sort(arrays)
print(f'Solution to 2 - selection sort is: {solution_2_selection}')

## Mnemonic = determine length of array; outer & inner-for loop; conditional to find min_index and swap as needed
## Time Complexity = O(n^2) - 2 loops; O(n) if sorted
## Space Complexity = O(1) - sorts in place


'---------------'

## 3. Insertion Sort

## What does Insertion Sort do?
    ## starts with first element, compares to element +1
    ## swaps if needed
    
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

solution_3_insertion = insertion_sort(arrays)
print(f'Solution to 3 - insertion sort is: {solution_3_insertion}')

## Mnemonic = douter for loop with i; instantiate key variable and j variable; while comparing to key; insert key
## Time Complexity = O(n^2) - 2 loops; O(n) if sorted
## Space Complexity = O(1) - sorts in place
### Would not perform well with large datasets based on quadratic time complexity
 