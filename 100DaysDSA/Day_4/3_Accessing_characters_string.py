### In Python, you can access individual characters within a string using indexing. 
    ### String indexing allows you to retrieve a specific character from a string based on its position

## Indexing
    # Each character in a string is assigned a positive index starting from 0 for the first character, 1 for the second character

my_string = "Hello"
print(my_string[0])  # Output: 'H'
print(my_string[1])  # Output: 'e'
print(my_string[4])  # Output: 'o'

## Negative Indexing
    # Python also supports negative indexing, which allows you to access characters from the end of the string
    # The last character has an index of -1, the second-to-last character has an index of -2, and so on

my_string = "Hello"
print(my_string[-1])  # Output: 'o'
print(my_string[-2])  # Output: 'l'
print(my_string[-5])  # Output: 'H'

## Accessing Characters in a Loop
    # You can use a loop to iterate over each character in a string and perform operations on them

my_string = "Hello"
for char in my_string:
    print(char)
# Output:
# 'H'
# 'e'
# 'l'
# 'l'
# 'o'

## Accessing Characters with Built-in Functions
    ## The ord() function returns the Unicode code point of a character
    ## The chr() function returns the character corresponding to a given Unicode code point

my_string = "Hello"
print(ord(my_string[0]))  # Output: 72
print(chr(72))  # Output: 'H'

## Handling Index Out of Range
    ## If you try to access an index that is out of the valid range for a string, Python will raise an IndexError

my_string = "Hello"
index=5
if 0 <= index < len(my_string):
    print(my_string[index])
else:
    print("Index out of range")