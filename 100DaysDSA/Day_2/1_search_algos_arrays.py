############################
## Search Algos on Arrays ##
############################ 

# Searching is the process of finding a specific element or value in an array

### 1. Linear Search - also known as Sequential Search
    ## simple searching algorithm that sequentially traverses through an array, comparing each element with the target value until a match is found or the end of the array is reached

def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

numbers_linear_search = [5, 2, 9, 1, 7] #### unsorted
target_linear_search = 5
index_linear_search = linear_search(numbers_linear_search, target_linear_search)

if index_linear_search != -1:
    print(f"Linear Search: Element {target_linear_search} found at index {index_linear_search}")
else:
    print(f"Linear Search: Element {target_linear_search} not found in the array")

## Big O
## Linear Search has a time complexity of O(n) in the worst case, where n is the size of the array


### 2. Binary Search - more efficient searching algorithm that works on sorted arrays
    ##  It repeatedly divides the search interval in half by comparing the middle element with the target value until the target is found or the search interval is empty

def binary_search(arr, target):
    low = 0
    high = len(arr)-1

    while low <= high:
        mid = (low + high) // 2
        if round(arr[mid],0) == target:
            return mid
        elif round(arr[mid]) < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1

numbers_binary_search = [1, 2, 5, 7, 9]   ## needs to be sorted
target_binary_search = 7
index_binary_search = binary_search(numbers_binary_search, target_binary_search)

if index_binary_search != -1:
    print(f"Linear Search: Element {target_binary_search} found at index {index_binary_search}")
else:
    print(f"Linear Search: Element {target_binary_search} not found in the array")


###### Linear Search is simple but inefficient for large arrays, while Binary Search is more efficient but requires a sorted array