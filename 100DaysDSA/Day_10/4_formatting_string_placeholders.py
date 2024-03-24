### String formatting with placeholders allows you to create dynamic and reusable strings by inserting values into predefined placeholders within a string template. 
### Python provides several ways to achieve this, including the % operator, the str.format() method, and f-strings (formatted string literals).

## 1. Using the % Operator:
    ## The % operator is the oldest way of string formatting in Python.
    ## It uses % placeholders within the string and substitutes them with values from a tuple or dictionary.

name = "Alice"
age = 25
formatted_string = "My name is %s and I'm %d years old." % (name, age)
print(formatted_string)  # Output: "My name is Alice and I'm 25 years old."

## 2. Using the str.format() Method:
    ## The str.format() method is a more modern and flexible approach to string formatting.
    ## It uses {} placeholders within the string and substitutes them with values passed as arguments to the format() method.  ##

name = "Bob"
age = 30
formatted_string = "My name is {} and I'm {} years old.".format(name, age)
print(formatted_string)  # Output: "My name is Bob and I'm 30 years old."

## 3. Using f-strings (Formatted String Literals):
    ## f-strings, introduced in Python 3.6, provide a concise and readable way to embed expressions inside string literals.
    ## They are denoted by prefixing the string with the letter f or F

name = "Charlie"
age = 35
formatted_string = f"My name is {name} and I'm {age} years old."
print(formatted_string)  # Output: "My name is Charlie and I'm 35 years old."

## 4. Named Placeholders:
    ## Both str.format() and f-strings support named placeholders, allowing you to refer to values by their names instead of positions.

person = {"name": "David", "age": 40}
formatted_string = "My name is {name} and I'm {age} years old.".format(**person)
print(formatted_string)  # Output: "My name is David and I'm 40 years old."

## 5. Alignment and Formatting Options:
    ## Both str.format() and f-strings support additional formatting options, such as alignment, padding, and precision

value = 3.14159
formatted_string = "The value is {:.2f}".format(value)
print(formatted_string)  # Output: "The value is 3.14"

value = 42
formatted_string = f"The value is {value:>5}"
print(formatted_string)  # Output: "The value is    42"