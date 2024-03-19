### Searching for substrings is a common task in string manipulation, where you aim to find the occurrence or position of a specific substring within a larger string

## 1. The in operator is the simplest way to check if a substring exists within a string.
    ## It returns True if the substring is found and False otherwise

str1 = "Hello, World!"
if "World" in str1:
    print("Substring found!")
else:
    print("Substring not found!")

## 2. The find() Method - The find() method returns the index of the first occurrence of a substring within a string

str1 = "Hello, World!"
index = str1.find("World")
if index != -1:
    print(f"Substring found at index {index}")
else:
    print("Substring not found!")

## 3. The rfind() Method - The rfind() method is similar to find(), but it returns the index of the last occurrence of a substring within a string

str1 = "Hello, World! Hello, Python!"
index = str1.rfind("Hello")
if index != -1:
    print(f"Last occurrence of substring found at index {index}")
else:
    print("Substring not found!")

## 4. The index() Method - The index() method is similar to find(), but it raises a ValueError if the substring is not found

str1 = "Hello, World!"
try:
    index = str1.index("Python")
    print(f"Substring found at index {index}")
except ValueError:
    print("Substring not found!")

## 5. The count() Method - The count() method returns the number of occurrences of a substring within a string

str1 = "Hello, World! Hello, Python!"
count = str1.count("Hello")
print(f"Substring 'Hello' occurs {count} times")

