### String Length
    ### You can find the length of a string using the len() function, which returns the number of characters in the string

my_string = "Hello, World!"
print(len(my_string))  # Output: 13

### String Indexing
    ### You can use positive or negative indexing to access characters from the beginning or end of the string

my_string = "Hello"
print(my_string[0])  # Output: 'H'
print(my_string[-1])  # Output: 'o'

### String Slicing
    ### Slicing allows you to extract a substring from a string by specifying a range of indices

my_string = "Hello, World!"
print(my_string[0:5])    # Output: "Hello"
print(my_string[7:])     # Output: "World!"
print(my_string[0:10:2])  # Output: "Hlo o"

### String Membership
    ### You can check if a substring exists within a string using the in or not in operators

my_string = "Hello, World!"
print("Hello" in my_string)     # Output: True
print("Python" not in my_string)  # Output: True

### String Methods
    ### Python provides several built-in string methods that allow you to perform various operations on strings
        # lower() and upper(): Convert the string to lowercase or uppercase.
        # strip(), lstrip(), rstrip(): Remove leading and/or trailing whitespace.
        # split(): Split the string into a list of substrings based on a delimiter.
        # join(): Join a list of strings into a single string using a separator.
        # replace(): Replace occurrences of a substring with another substring.
        # startswith() and endswith(): Check if the string starts or ends with a specific substring

my_string = "  Hello, World!  "
print(my_string.strip())  # Output: "Hello, World!"
print(my_string.lower())  # Output: "  hello, world!  "
print(my_string.split(", "))  # Output: ["  Hello", "World!  "]

words = ["Hello", "World"]
print("-".join(words))  # Output: "Hello-World"

my_string = "Hello, World!"
print(my_string.replace("World", "Python"))  # Output: "Hello, Python!"
print(my_string.startswith("Hello"))  # Output: True