#####################
## Intro to Arrays ##
##################### 


##### 1. What are arrays and why are they used?
  
    ## an array is a data structure that stores a collection of elements, typically of the same data type, in contiguous memory locations
  
    ## provides a way to organize an access a fixed-size sequence of elements efficiently

    ## Python arrays can be represented using the built-in list data type or by using the array module

##### 2. Why are arrays used?

    ## Random Access -- able to directly access any element in the array by its index in constant time, regardless of the size of the array

    ## Efficient Storage -- elements are stored in contiguous memory locations which allows for more efficient storage
    
    ## Fixed Size -- fixed size at time of creation which allows for better memory allocation

    ## Ordered Elements -- arrays maintain the ordr of elements based on their indices; helpful for sorting or searching

### Array Declaration and initialization
    ## Array declaration and initialization refers to the process of creating an array and assigning initial values to its elements

    ## in Python can use the list or array modules

    ### Using the list data type:
        ### Lists are dynamic arrays that can store elements of different data types
        ### can be initialized using square brackets and separate with commas

    ## 1. using the list data type - list are dynamic arrays that can sort elements of different data types; initialize with square brackets

'----------------'
# declare an empty list
my_list = []

# declare and initialize a list with elements
numbers = [1,2,3,4]  ## list of integers
words = ['apple', 'banana', 'pineapple'] ## list of strings
mixed_list = ['hello', 1, True, 3.14]  ## list of different data types

    ### 2. In an array model, able to store elements of homogenous data type - useful when have a large collection of the same data type

'-----------------'

import array
int_array = array.array('i',[1,2,3,4,5]) ## declare an array of integers
float_array = array.array('f', [1.0, 2.5, 3.4, 5.6])


    ### 3. List Comprehension
        ### List comprehensions allow you to create lists based on existing lists or other iterable objects

squares = [x**2 for x in range(1,6)]
## output = [1,,4,9,16,25]

list_conditional = [x for x in range(1,11) if x % 2 ==0]
# output = [2,4,6,8,10]

##### Python's lists are dynamic arrays, meaning they can grow or shrink in size as needed, whereas arrays from the array module have a fixed size determined at the time of creation.

#####  3. Accessing Aray Elements - the process of retrieving or reading the value stored at a specific position in an array
    ## Accessing elements by index:
        #### In Python, array indices start from 0 for the first element and go up to n-1 for the last element, where n is the size of the array

fruits = ['apple','banana','melon','pineapple',]
fruit_1 = fruits[0]  # apple
fruits_2 = fruits[1] # banana
fruits_3 = fruits[2] # melon
fruits_4 = fruits[3] # pineapple

    ## Accessing elements by negative indexing
        ### Python also supports negative indexing, which allows you to access elements from the end of the array
fruit_1 = fruits[-4]  ## apple
fruit_2 = fruits[-3]  ## banana
fruit_3 = fruits[-2]  ## melon
fruits_4 = fruits[-1] ## pineapple

    ## Accessing elements in a multi-dimensional array -arrays that contain other arrays as elements
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(matrix[0][0])  # Output: 1
print(matrix[1][2])  # Output: 6
print(matrix[2][1])  # Output: 8

    ## Accessing elements using loops to iterate voer the array
numbers = [1,2,3,4]
for num in numbers:
    print(num)
