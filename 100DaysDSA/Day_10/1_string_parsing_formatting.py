#####################################
##  String Parsing + Formatting    ##
#####################################

### String parsing involves extracting useful information from strings, while string formatting is the process of creating strings with a specific structure or layout.

## 1. String Splitting:
    ### Use the split() method to split a string into a list of substrings based on a delimiter.

text = "apple,banana,cherry,date"
fruits = text.split(",")
print(fruits)  # Output: ['apple', 'banana', 'cherry', 'date']

## 2. String Joining:
    ## Use the join() method to concatenate a list of strings into a single string with a specified separator.         

fruits = ['apple', 'banana', 'cherry']
text = ", ".join(fruits)
print(text)  # Output: "apple, banana, cherry"

## 3. String Stripping:
    ## Use the strip(), lstrip(), or rstrip() methods to remove leading and/or trailing whitespace or specific characters from a string.

text = "   Hello, World!   "
stripped_text = text.strip()
print(stripped_text)  # Output: "Hello, World!"

## 4. String Formatting with f-strings (Python 3.6+):
    ## Use f-strings to embed expressions inside string literals for easy and readable string formatting.

name = "Alice"
age = 25
print(f"My name is {name} and I'm {age} years old.")
# Output: "My name is Alice and I'm 25 years old."

## 5. String Formatting with format() method:
    ## Use the format() method to create formatted strings by replacing placeholders with values

name = "Bob"
age = 30
text = "My name is {} and I'm {} years old.".format(name, age)
print(text)  # Output: "My name is Bob and I'm 30 years old."

## 6. Regular Expressions (Regex):
    ## Use the re module for advanced string parsing and pattern matching.

import re

text = "The quick brown fox jumps over the lazy dog."
pattern = r"\b\w{4}\b"
matches = re.findall(pattern, text)
print(matches)  # Output: ['quick', 'brown', 'jumps', 'lazy']

## 7. String Slicing:
    ## Extract substrings from a string using slicing notation.

text = "Hello, World!"
substring = text[7:12]
print(substring)  # Output: "World"