##### Part 1 = Traversing an Array
    ## traversing an array means accessing and processing each element of the array in a systematic manner
    ## allows to perform operations on individual elements or compute aggregate results based on the array elements

    # 1. Using a For loop - The most common way to traverse an array; allows to iterate over each element of the array in a sequential manner
traverse_array_numbers = [1,2,3,4,5]
for num in traverse_array_numbers:
    print(num)

output = """1
2
3
4
5"""
    # 2. Using the range() function - to access the array elements along with their indices, can use the range() function in combination with the len() function to generate a sequence of indices 

range_fruits = ['apple', 'banana', 'orange', 'grape']
for i in range(len(range_fruits)):
    print(f"Index: {i}, Element: {range_fruits[i]}")

output = """Index: 0, Element: apple
Index: 1, Element: banana
Index: 2, Element: orange
Index: 3, Element: grape"""

    # 3. Using the enumerate() function - convenient way to iterate over an array while getting both the index and the element in each iteration

enumerate_fruits = ['apple', 'banana', 'orange', 'grape']
for i, fruit in enumerate(enumerate_fruits):
    print(f"Index: {i}, Fruit: {fruit}") 

output="""Index: 0, Element: apple
Index: 1, Element: banana
Index: 2, Element: orange
Index: 3, Element: grape"""

    # 4. Traversing a multidimensional array: use nested loops to access elements in each dimension
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Traversing the 2D array
for row in matrix:
    for num in row:
        print(num, end=' ')
    print()
output="""1 2 3
4 5 6
7 8 9"""

'--------------------------------------------------------'

##### Part 2 = Inserting elements into an array
    ## 1. Inserting elements into a list:

        ###  the append() method allows you to add an element to the end of a list
insert_fruits = ['apple', 'banana', 'orange']
insert_fruits.append('grape')
print(insert_fruits)  # Output: ['apple', 'banana', 'orange', 'grape']

        ### The insert() method allows you to insert an element at a specified index in a list
insert_index_fruits = ['apple', 'banana', 'orange']
insert_index_fruits.insert(1, 'grape')
print(insert_index_fruits)  # Output: ['apple', 'grape', 'banana', 'orange']

        ### The extend() method allows you to append multiple elements from another iterable (such as a list or tuple) to the end of a list
extend_fruits = ['apple', 'banana', 'orange']
more_fruits = ['grape', 'kiwi']
extend_fruits.extend(more_fruits)
print(extend_fruits)  # Output: ['apple', 'banana', 'orange', 'grape', 'kiwi']

    ## 2. Inserting elements into an array:
        
        ### The append() method allows you to add an element to the end of an array
import array

append_array_numbers = array.array('i', [1, 2, 3])
append_array_numbers.append(4)
print(append_array_numbers)  # Output: array('i', [1, 2, 3, 4])

        ### The insert() method allows you to insert an element at a specified index in an array
import array

insert_array_numbers = array.array('i', [1, 2, 3])
insert_array_numbers.insert(1, 5)
print(insert_array_numbers)  # Output: array('i', [1, 5, 2, 3])

        ### The extend() method allows you to append multiple elements from another iterable (such as a list or tuple) to the end of an array
import array

extend_array_numbers = array.array('i', [1, 2, 3])
more_numbers = array.array('i', [4, 5])
extend_array_numbers.extend(more_numbers)
print(extend_array_numbers)  # Output: array('i', [1, 2, 3, 4, 5])


'--------------------------------------------------------'

##### Part 3: Deleting elements from a list/ array
    ## 1. Deleting elements from a list - The remove() method allows you to remove the first occurrence of a specified element from a list

remove_fruits = ['apple', 'banana', 'orange', 'banana', 'grape']
remove_fruits.remove('banana')
print(remove_fruits)  # Output: ['apple', 'orange', 'banana', 'grape']

    ## 2. Removie items from list at specified index - The pop() method allows you to remove and return an element at a specified index from a list

remove_index_fruits = ['apple', 'banana', 'orange', 'grape']
removed_fruit = remove_index_fruits.pop(1)
print(removed_fruit)  # Output: 'banana'
print(remove_index_fruits)  # Output: ['apple', 'orange', 'grape']

    ## 3. Removing elements using slicing: Can use slicing to remove a range of elements from a list by assigning an empty slice to the desired range

remove_slice_fruits = ['apple', 'banana', 'orange', 'grape', 'kiwi']
remove_slice_fruits[1:4] = []
print(remove_slice_fruits)  # Output: ['apple', 'kiwi']

    ## 4. Removing all elements - The clear() method allows you to remove all elements from a list, leaving it empty

remove_clear_fruits = ['apple', 'banana', 'orange']
remove_clear_fruits.clear()
print(remove_clear_fruits)  # Output: []

    # 5. Deleting elements from an array using the array module - the pop() method allows you to remove and return an element at a specified index from an array

import array

array_pop_numbers = array.array('i', [1, 2, 3, 4, 5])
removed_number = array_pop_numbers.pop(2)
print(removed_number)  # Output: 3
print(array_pop_numbers)  # Output: array('i', [1, 2, 4, 5])

    # 6.  Removing elements using slicing - You can use slicing to remove a range of elements from an array by assigning an empty slice to the desired range.

import array

slice_array_numbers = array.array('i', [1, 2, 3, 4, 5])
slice_array_numbers[1:4] = array.array('i', [])
print(slice_array_numbers)  # Output: array('i', [1, 5])