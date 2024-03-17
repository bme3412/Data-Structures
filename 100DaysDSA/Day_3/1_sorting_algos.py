############################
##   Sorting Algorithms   ##
############################ 

### Sorting algorithms are used to arrange the elements of an array in a specific order, such as ascending or descending order
### There are various sorting algorithms available, each with its own characteristics and performance trade-offs

### 1. Bubble Sort:

    ### Bubble sort is a simple sorting algorithm that repeatedly steps through the array, compares adjacent elements, and swaps them if they are in the wrong order. 

    ### The process is repeated until the array is sorted.

def bubble_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

### 2. Selection Sort:
    
    ### Selection sort divides the array into two parts: the sorted portion and the unsorted portion. 
    
    ### It repeatedly selects the smallest element from the unsorted portion and adds it to the end of the sorted portion.

def selection_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr

### 3. Insertion Sort:

    ### Insertion sort builds the final sorted array one element at a time -  it takes each element from the unsorted portion and inserts it into its correct position in the sorted portion 

def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

### 4. Merge Sort:

    ### Merge sort is a divide-and-conquer algorithm that divides the array into smaller subarrays, sorts them recursively, and then merges the sorted subarrays back together to obtain the final sorted array.

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

### 5. Quick Sort:

    ### Quick sort is another divide-and-conquer algorithm that selects a pivot element and partitions the array around the pivot.
    ### The elements smaller than the pivot are placed before it, and the elements greater than the pivot are placed after it. 
    ### The process is recursively applied to the subarrays on either side of the pivot

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)


### Each algorithm has its own time and space complexity, and the choice of algorithm depends on factors such as the size of the array, the initial order of elements, and any specific requirements or constraints

## Python's built-in sorted() function and the sort() method of lists use highly optimized sorting algorithms (e.g., Timsort) under the hood, so in most cases, it's recommended to use these built-in methods instead of implementing sorting algorithms manually