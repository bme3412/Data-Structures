######################
## Intro to Strings ##
######################

## 1. Intro to Strings - A string is a sequence of characters enclosed in single quotes ('') or double quotes ("")

# example:
what_is_a_string = "Hello, World!" 

## 2. Creating and Assigning Strings
    ## Assigning strings to a variable
define_string_variable = "Welcome to Python programming!"

    ## Creating multi-line strings using triple quotes
define_multi_line_string = '''Roses are red,
Violets are blue,
Python is awesome,
And so are you!'''

## 3. Accessing Characters in a string
    ## Accessing individual characters using indexing
string_for_indexing = "Hello"
print(string_for_indexing[0])  # Output: 'H'
print(string_for_indexing[1])  # Output: 'e'

    ## Negative indexing to access characters from the end
multi_line_string = "Hello"
print(multi_line_string[-1])  # Output: 'o'
print(multi_line_string[-2])  # Output: 'l'

## 4. String Slicing
    # Extracting substrings using slicing
extract_substrings_slicing = "Hello, World!"
print(extract_substrings_slicing[0:5])  # Output: 'Hello'
print(extract_substrings_slicing[7:])   # Output: 'World!'

    # Slicing with a step
slicing_with_step = "Hello, World!"
print(slicing_with_step[0:10:2])  # Output: 'Hlo o'

## 5. String Methods
    # len(): Returns the length of a string

length_string = "Hello"
print(len(length_string))  # Output: 5

    # lower() and upper(): Convert a string to lowercase or uppercase
change_case_string = "Hello"
print(change_case_string.lower())  # Output: 'hello'
print(change_case_string.upper())  # Output: 'HELLO'

    # strip(): Removes leading and trailing whitespace from a string
strip_string = "   Hello, World!   "
print(strip_string.strip())  # Output: 'Hello, World!'

    # split(): Splits a string into a list of substrings based on a delimiter.
split_string = "Hello, World!"
print(split_string.split(", "))  # Output: ['Hello', 'World!']

    # join(): Joins a list of strings into a single string using a separator.
words_to_join = ['Hello', 'World!']
print(', '.join(words_to_join))  # Output: 'Hello, World!'

## 6. String Formatting
    # Using the format() method
name = "Alice"
age = 25
print("My name is {} and I'm {} years old.".format(name, age))
    
    # Using f-strings
name = "Bob"
age = 30
print(f"My name is {name} and I'm {age} years old.")

## 7. String Concatenation
    # Concatenating strings using the + operator
str1 = "Hello"
str2 = "World"
result = str1 + ", " + str2 + "!"
print(result)  # Output: 'Hello, World!'