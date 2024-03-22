## 1. Squaring a Sorted Array: Given a sorted array of integers, square each element and return the resulting array in non-decreasing order.

arr_1 = [-6,-4,0,1,3,5]
arr_2 = [1,2,3,4,5]

def square_sorted_array(arr):
    return sorted([i**2 for i in arr])

solution_1a = square_sorted_array(arr_1)
solution_1b = square_sorted_array(arr_2)
print(solution_1a)
print(solution_1b)

### 2. Valid Palindrome: Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring case sensitivity.

string_1 = 'racecar'
string_2 = 'racecar42'

def valid_palindrome(string):
    return True if string==string[::-1] else False

solution_2a = valid_palindrome(string_1)
solution_2b = valid_palindrome(string_2)

print(solution_2a)
print(solution_2b)

### 3. Move Zeroes: Given an array of integers, move all zeroes to the end of the array while maintaining the relative order of non-zero elements.
arr_int = [0,0,1,2,3,5]

def zeros_to_end(arr):
    i = 0
    j = arr[-1]
    for i in arr:
        if arr[i] == 0 and arr[j] != 0:
            arr[i], arr[j] = arr[j], arr[i]
            i+=1
            j-=1
            arr.sort()
    while i < len(arr):
        if arr[i] !=0:
            arr[i], arr[j] = arr[j], arr[i]
            i+=1
        j+=1
    return arr[::-1]

solution_3 = zeros_to_end(arr_int)
print(solution_3)

### 4. Reverse Words in a String: Given a string, reverse the order of words in the string while preserving whitespace and initial word order.

### 5. Intersection of Two Arrays: Given two sorted arrays, find the intersection of the arrays (elements that appear in both arrays).

### 6. Three Sum: Given an array of integers, find all unique triplets that sum up to a target value.

### 7. Container With Most Water: Given an array of heights, find the maximum amount of water that can be contained between any two vertical lines.

### 8. Minimum Window Substring: Given a string and a target substring, find the minimum window in the string that contains all the characters of the target substring.

### 9. Partition Labels: Given a string, partition it into as many parts as possible so that each letter appears in at most one part, and return the sizes of these parts.

### 10. Merge Sorted Array: Given two sorted arrays and the number of elements in each array, merge the arrays into a single sorted array.

### 11. Trapping Rain Water: Given an array representing the heights of walls, calculate the amount of water that can be trapped between the walls.

### 12. Longest Substring Without Repeating Characters: Given a string, find the length of the longest substring that contains no repeating characters.