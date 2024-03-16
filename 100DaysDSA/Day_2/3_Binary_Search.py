#############################
## Binary Search on Arrays ##
############################# 

#### Binary Search - Binary Search is an efficient searching algorithm that works on sorted arrays. 
    ### It follows a divide-and-conquer approach to find the target element by repeatedly dividing the search space in half. 
    ### Binary Search compares the target element with the middle element of the array. 
        #### If they are not equal, the search space is reduced to either the left or right half of the array, depending on whether the target element is smaller or larger than the middle element

def binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1

# Example usage
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
target = 6

index = binary_search(numbers, target)

if index != -1:
    print(f"Element {target} found at index {index}")
else:
    print(f"Element {target} not found in the array")


##### Big O notation
    #### Binary Search has a time complexity of O(log n) in the worst case, where n is the size of the array. 
        ##### This means that the number of comparisons required to find the target element decreases logarithmically with each iteration. 
        ###### Binary Search is much more efficient than Linear Search for large sorted arrays

#### Binary Search is widely used in various scenarios
    ##### Searching for a specific value in a large sorted dataset
    ##### Implementing efficient dictionary lookups
    ##### Solving optimization problems where the search space can be reduced based on certain conditions