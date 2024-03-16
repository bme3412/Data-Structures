import array

####### Problem 1:
problem_1 = """Find the maximum/minimum element in an array"""

list_1 =[1,2,3,4,5,6,7,8,9,10]

def find_min_max(list_num):
    max_int = 0
    min_int = 0
    for i in list_num:
        max_int=max(list_num)
        min_int = min(list_num)
    return max_int, min_int

answer_1_list= find_min_max(list_1)
print(f'Answer to problem 1a is: {answer_1_list}')


array_1 = [10,5,4,3,8]

def find_min_max_array(array_1):
    max_int = 0
    min_int = 0
    for i in array_1:
        max_int = max(array_1)
        min_int = min(array_1)
    return max_int, min_int
answer_1_array = find_min_max_array(array_1)
print(f'Answer to problem 1b is: {answer_1_array}')

######### Problem 2
problem_2="""Calculate the average of elements in an array"""

array_2 = [12, 750, 1, 30]

def find_average(array):
    length = len(array)
    average_array = sum(array)/length
    return average_array
answer_2 = find_average(array_2)
print(f'Answer to problem 2 is: {answer_2}')

####### Problem 3:
problem_3 = """Reverse an Array: Write a function that takes an array as input and returns the reversed array."""

list_of_num=[2,4,6,8,10,12,14,16,18,20]

## slicing
def reverse_array_slice(array):
    return array[::-1]
answer_3a = reverse_array_slice(list_of_num)
print(f'Answer to problem 3a is: {answer_3a}')


## in place
def reverse_array_slice(array):
    left_index = 0
    right_index = len(array)-1 ## zero-based indexing
    while left_index < right_index:
        array[left_index], array[right_index] = array[right_index], array[left_index]
        left_index +=1
        right_index -=1
    return array 
answer_3b = reverse_array_slice(list_of_num)
print(f'Answer to problem 3b is: {answer_3b}')


####### Problem 4:
problem_4 = """Find the Sum of Array Elements: Write a function that takes an array of numbers as input and returns the sum of all the elements."""

list_to_sum = [1,2,5,10, 15, 20, 25]
def sum_elements(array):
    return sum(list_to_sum)
summed_nums = sum_elements(list_to_sum)
print(f'Answer to problem 4 is: {summed_nums}')


####### Problem 5:
problem_5 = """Remove Duplicates from an Array: Write a function that takes an array as input and returns a new array with duplicates removed."""

list_duplicates = [11, 1, 11, 12, 13, 2, 2, 5]

def remove_duplicates(list_int):
    return list(set(list_int))

removed_duplicates = remove_duplicates(list_duplicates)
print(f'Answer to problem 5 is: {removed_duplicates}')



###### Problem 6:
problem_6 = """Find the Second Largest Element in an Array: Write a function that takes an array of numbers as input and returns the second largest element."""

second_largest = [1,5,7,8,14,78,15,25,34]

def find_second_largest(list_int):
    return sorted(list_int)[-2]

second_largest_array = find_second_largest(second_largest)
print(f'Answer to problem 6 is: {second_largest_array}')


###### Problem 7:
problem_7="""Merge Two Sorted Arrays: Write a function that takes two sorted arrays as input and returns a new sorted array containing elements from both arrays."""

sorted_array_1 = [1,3,5,7,9,11]
sorted_array_2= [0,2,4,6,8,10,12]

def merged_sorted(array1, array2):
    return sorted(array1+ array2)

merged_sorted_array = merged_sorted(sorted_array_1, sorted_array_2)
print(f'Answer to problem 7 is: {merged_sorted_array}')