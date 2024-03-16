#############################
## Linear Search on Arrays ##
############################# 



## Linear Search, also known as Sequential Search, is a simple searching algorithm that sequentially traverses an array or list, element by element, until the desired element is found or the end of the array is reached

def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

# Example usage
numbers = [5, 2, 9, 1, 7]
target = 7

index = linear_search(numbers, target)

if index != -1:
    print(f"Element {target} found at index {index}")
else:
    print(f"Element {target} not found in the array")


## Big O notation

### Linear Search has a time complexity of O(n) in the worst case, where n is the size of the array. 
    # This means that the time taken to search for an element increases linearly with the size of the array. 
    # In the worst case, when the target element is not present in the array or is located at the last position, Linear Search needs to compare the target element with every element in the array.

### Linear Search is simple to implement and understand, but it becomes inefficient for large arrays. 
    # In such cases, more efficient searching algorithms like Binary Search (which requires a sorted array) or Hash Table-based searches are preferred