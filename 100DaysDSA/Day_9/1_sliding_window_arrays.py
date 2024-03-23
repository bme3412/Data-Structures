#################################
##  Intro to Sliding Window    ##
#################################

### The sliding window technique is a powerful algorithmic approach commonly used to solve problems involving arrays or strings. 

    ### It involves moving a fixed-size window or a variable-size window over the elements of the array or string to perform certain operations or calculations

    ### The sliding window technique is particularly useful when you need to find subarrays or substrings that satisfy certain conditions or when you need to efficiently calculate some metric or result based on a sliding window of elements

    ### The key idea behind the sliding window technique is to maintain a window of elements and adjust the window's boundaries based on the problem's constraints. 

    ### By sliding the window and updating the relevant information, we can avoid unnecessary calculations and optimize the algorithm's time complexity.

## 1. Fixed-size sliding window
"""Problem: Given an array of integers and a window size k, find the maximum sum of any contiguous subarray of size k"""

def max_sum_subarray(arr, k):
    if len(arr) < k:
        return None
    
    max_sum = sum(arr[:k])
    current_sum = max_sum
    
    for i in range(k, len(arr)):
        current_sum = current_sum - arr[i - k] + arr[i]
        max_sum = max(max_sum, current_sum)
    
    return max_sum

# Example usage
arr = [1, 4, 2, 10, 23, 3, 1, 0, 20]
k = 4
result = max_sum_subarray(arr, k)
print(result)  # Output: 39

### 2. Variable-size sliding window
"""Given a string s, find the length of the longest substring without repeating characters"""

def length_of_longest_substring(s):
    char_set = set()
    left = right = max_length = 0
    
    while right < len(s):
        if s[right] not in char_set:
            char_set.add(s[right])
            max_length = max(max_length, right - left + 1)
            right += 1
        else:
            char_set.remove(s[left])
            left += 1
    
    return max_length

# Example usage
s = "abcabcbb"
result = length_of_longest_substring(s)
print(result)  # Output: 3