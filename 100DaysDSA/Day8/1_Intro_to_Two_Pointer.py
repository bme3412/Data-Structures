#################################
##     Intro to Two-Pointer    ##
#################################

### The two-pointer technique is a powerful and efficient approach used to solve a wide range of problems, particularly those involving arrays, strings, and linked lists. 
    ### It involves using two pointers to traverse the data structure in a specific manner, allowing for efficient searching, comparison, or manipulation of elements

### 1. Pointers: In the context of the two-pointer technique, pointers refer to variables that store the indices or references to elements in the data structure.

### 2. Pointer Movement: The two pointers can move in various ways depending on the problem requirements. 
    ### They can move towards each other (one from the beginning and one from the end), move in the same direction (both from the beginning), or move independently based on certain conditions

### 3. Pointer Comparison: The two-pointer technique often involves comparing the elements pointed to by the two pointers
    ### This comparison helps in making decisions on how to move the pointers or perform specific operations

### 4. In-place Modification: The two-pointer technique is often used to modify the data structure in-place, without using extra space. 
    ### This is achieved by carefully moving and updating elements using the pointers

### Advantages of the Two-Pointer Technique:

    ### 1. Efficiency: The two-pointer technique helps in reducing the time complexity of certain problems by avoiding unnecessary iterations and comparisons

    ### 2. Space Optimization: By modifying the data structure in-place using pointers, the two-pointer technique minimizes the need for extra space, making it space-efficient

    ### 3. Readability: The two-pointer technique often leads to cleaner and more readable code compared to alternative approaches.

### Common Applications:
    ### Sliding Window: The two-pointer technique is frequently used in sliding window problems, where a window of elements is maintained and processed efficiently.

    ### Pair Sum: Finding pairs of elements that satisfy a certain condition, such as a target sum, can be efficiently solved using the two-pointer technique on sorted arrays.

    ### Palindrome Validation: Checking if a string is a palindrome can be done using two pointers, one starting from the beginning and the other from the end, comparing characters until the pointers meet in the middle.

    ### Reversing Arrays or Strings: Two pointers can be used to efficiently reverse an array or string by swapping elements from both ends until the pointers meet in the middle.

    ### Removing Duplicates: The two-pointer technique can be used to remove duplicates from a sorted array or linked list efficiently.

def reverseString(s):
    left = 0
    right = len(s) - 1
    
    while left < right:
        # Swap characters at left and right pointers
        s[left], s[right] = s[right], s[left]
        left += 1
        right -= 1
    
    return ''.join(s)