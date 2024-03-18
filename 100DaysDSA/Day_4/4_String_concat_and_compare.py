### String Concatenation - String concatenation is the process of joining two or more strings together to create a new string
    ### In Python, you can concatenate strings using the + operator

str1 = "Hello"
str2 = "World"
result = str1 + " " + str2
print(result)  # Output: "Hello World"

### String Comparison - Python allows you to compare strings using comparison operators such as ==, !=, <, >, <=, and >=

    ## Equality comparison
        ## The == operator checks if two strings are equal; The != operator checks if two strings are not equal

str1 = "Hello"
str2 = "Hello"
str3 = "World"

print(str1 == str2)  # Output: True
print(str1 == str3)  # Output: False
print(str1 != str3)  # Output: True

### Case-Insensitive Comparison

    ## If you want to compare strings ignoring the case (uppercase or lowercase), you can convert the strings to a common case before comparison

str1 = "Hello"
str2 = "hello"

print(str1 == str2)             # Output: False
print(str1.lower() == str2.lower())  # Output: True

## Comparing Strings with Built-in Functions
    # Python provides built-in functions like min() and max() that can be used to find the minimum and maximum strings based on their lexicographic order

str1 = "Apple"
str2 = "Banana"
str3 = "Orange"

print(min(str1, str2, str3))  # Output: "Apple"
print(max(str1, str2, str3))  # Output: "Orange"