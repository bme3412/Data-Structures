### Substring extraction is the process of obtaining a portion of a string based on specific criteria, such as start and end indices or certain patterns

## 1. Slicing - Slicing allows to extract a substring by specifying the start and end indices
    ## The syntax is string[start:end], where start is inclusive and end is exclusive.

str1 = "Hello, World!"
substring = str1[0:5]
print(substring)  # Output: "Hello"

## 2. Slicing with a Step - You can also specify a step value to extract characters at regular intervals.
    ## The syntax is string[start:end:step]

str1 = "Hello, World!"
substring = str1[0:12:2]
print(substring)  # Output: "Hlo ol!"

## 3. Negative Indexing - Python allows negative indexing to count from the end of the string

str1 = "Hello, World!"
substring = str1[-6:-1]
print(substring)  # Output: "World"

## 4. Substring Search - The find() method returns the index of the first occurrence of a substring within a string
    ## If the substring is not found, it returns -1

str1 = "Hello, World!"
index = str1.find("World")
if index != -1:
    substring = str1[index:]
    print(substring)  # Output: "World!"

## 5. Regular Expressions - Python's re module provides powerful tools for substring extraction using regular expressions

import re

str1 = "The quick brown fox jumps over the lazy dog."
pattern = r"quick.*fox"
match = re.search(pattern, str1)
if match:
    substring = match.group()
    print(substring)  # Output: "quick brown fox"

## 6. Split and Join - You can split a string into a list of substrings based on a delimiter and then extract specific substrings from the list

str1 = "apple,banana,cherry,date"
fruits = str1.split(",")
substring = ",".join(fruits[1:3])
print(substring)  # Output: "banana,cherry"