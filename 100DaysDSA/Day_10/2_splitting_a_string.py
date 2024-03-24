### Splitting a string involves dividing a string into smaller substrings based on a specified delimiter or separator. The split() method in Python is commonly used for this purpose.

## 1. Basic Splitting:
     ##The split() method splits a string into a list of substrings based on a delimiter.
    ## If no delimiter is specified, it splits the string based on whitespace (spaces, tabs, newlines).

text = "apple,banana,cherry,date"
fruits = text.split(",")
print(fruits)  # Output: ['apple', 'banana', 'cherry', 'date']

## 2. Specifying the Delimiter:
    ## You can specify the delimiter as an argument to the split() method.
    ## The delimiter can be a single character or a string.

text = "apple:banana:cherry:date"
fruits = text.split(":")
print(fruits)  # Output: ['apple', 'banana', 'cherry', 'date']

## 3. Limiting the Number of Splits:
    ## By default, split() splits the string at every occurrence of the delimiter.
    ## You can limit the number of splits by specifying the maxsplit parameter.

text = "apple,banana,cherry,date"
fruits = text.split(",", maxsplit=2)
print(fruits)  # Output: ['apple', 'banana', 'cherry,date']


## 4. Splitting on Multiple Delimiters:
    ## To split a string based on multiple delimiters, you can use regular expressions with the re.split() function.

import re

text = "apple,banana:cherry;date"
fruits = re.split(r'[,;:]', text)
print(fruits)  # Output: ['apple', 'banana', 'cherry', 'date']

## 5. Handling Empty Substrings:
    ## When splitting a string, you may encounter empty substrings if there are consecutive delimiters or if the string starts or ends with a delimiter.
    ## By default, split() includes empty substrings in the resulting list.

text = "apple,,banana,cherry,"
fruits = text.split(",")
print(fruits)  # Output: ['apple', '', 'banana', 'cherry', '']

## 6. Splitting Lines:
    ## The splitlines() method is specifically used to split a string into a list of lines.
    ## It splits the string at line boundaries (e.g., newline characters).

text = "apple\nbanana\ncherry"
fruits = text.splitlines()
print(fruits)  # Output: ['apple', 'banana', 'cherry']