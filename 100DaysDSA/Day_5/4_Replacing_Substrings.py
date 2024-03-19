### Replacing substrings is another common task in string manipulation, where you replace occurrences of a specific substring within a string with another substring

## 1. The replace() Method - The replace() method is the most straightforward way to replace substrings within a string

str1 = "Hello, World!"
new_str = str1.replace("World", "Python")
print(new_str)  # Output: "Hello, Python!"

## 2. The replace() Method with Count - You can also specify the maximum number of occurrences to replace using the count parameter in the replace() method

str1 = "Hello, World! Hello, Python!"
new_str = str1.replace("Hello", "Hi", 1)
print(new_str)  # Output: "Hi, World! Hello, Python!"

## 3. Translation Tables with str.translate() - The translate() method allows you to perform character-level replacements using translation tables

str1 = "Hello, World!"
table = str.maketrans("eo", "EO")
new_str = str1.translate(table)
print(new_str)  # Output: "HEllO, WOrld!"