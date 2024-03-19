#########################
## String Manipulation ##
######################### 

### String manipulation allows you to process, transform, and extract information from text data

## 1. String Concatenation - You can concatenate strings using the + operator or by using string formatting

str1 = "Hello"
str2 = "World"
result = str1 + " " + str2
print(result)  # Output: "Hello World"

## 2. String Slicing - Slicing allows you to extract a substring from a string by specifying the start and end indices

str1 = "Hello, World!"
substring = str1[7:12]
print(substring)  # Output: "World"

## 3. String Splitting - You can split a string into a list of substrings based on a delimiter using the split() method

str1 = "apple,banana,cherry"
fruits = str1.split(",")
print(fruits)  # Output: ["apple", "banana", "cherry"]

## 4. String Joining - The join() method allows you to join a list of strings into a single string using a specified delimiter

fruits = ["apple", "banana", "cherry"]
result = ", ".join(fruits)
print(result)  # Output: "apple, banana, cherry"

## 5. String Replacement - The replace() method replaces occurrences of a substring with another substring

str1 = "Hello, World!"
result = str1.replace("World", "Python")
print(result)  # Output: "Hello, Python!"

## 6. String Formatting - Python provides various ways to format strings, such as using % operator, str.format() method, or f-strings 

name = "Alice"
age = 25
result = f"My name is {name} and I'm {age} years old."
print(result)  # Output: "My name is Alice and I'm 25 years old."

## 7. String Methods - Python offers numerous built-in string methods for tasks like case conversion (upper(), lower()), checking prefixes/suffixes (startswith(), endswith()), stripping whitespace (strip())

str1 = "   Hello, World!   "
result = str1.strip().upper()
print(result)  # Output: "HELLO, WORLD!"