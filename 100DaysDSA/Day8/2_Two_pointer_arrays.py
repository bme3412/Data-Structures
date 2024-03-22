#################################
## Intro to Two-Pointer Arrays ##
#################################

#### The two-pointer technique is an efficient approach to solve certain problems involving arrays or strings. 
    ### It involves using two pointers to traverse the array or string in a specific manner, often from both ends or in a synchronized way. 
    ### The two pointers can move towards each other, move in the same direction, or move independently based on certain conditions.

### The two-pointer technique is particularly useful in scenarios where you need to find pairs of elements that satisfy a certain condition, or when you need to modify the array in-place based on specific criteria

### The two-pointer technique can be applied to various other problems, such as:
    ### Finding the pair of elements with a given sum in a sorted array
    ### Reversing an array or string
    ### Sliding window problems
    ### Merging two sorted arrays
    ### Manipulating linked lists


### Problem: Remove Duplicates from a Sorted Array
"""Given a sorted array, remove the duplicates in-place such that each element appears only once and returns the new length."""

def removeDuplicates(arr):
    if len(arr) == 0:
        return 0
    
    # Initialize two pointers
    i = 0  # Slow pointer
    j = 1  # Fast pointer
    
    while j < len(arr):
        if arr[i] != arr[j]:
            # Move the distinct element to the next position
            i += 1
            arr[i] = arr[j]
        j += 1
    
    return i + 1

### We initialize two pointers, i (slow pointer) and j (fast pointer), starting from the first and second elements of the array, respectively.

### We compare the elements at positions i and j. If they are different, we move the distinct element to the next position  by incrementing i and updating arr[i] with arr[j].

### If the elements are the same, we only increment j to skip the duplicate element.

### At the end, i represents the index of the last distinct element, so we return i + 1 as the new length of the array.
