prompt = """Reverse a String: Problem: Given a string, write a function to reverse the string in-place."""

def reverseString(s):
    reversed_string = s[::-1]
    return reversed_string

print(reverseString('basketball'))

### but because this is slicing it creates a new string
## time complexity of O(n) and a 
## space complexity of O(n) to store the list of characters
### there are more efficient ways to do this

def reverseString_2(s):
    # convert string to a list
    s_list = list(s)
    
    # create pointers so that can traverse the string
    left = 0
    right = len(s_list)-1

    # conditional so that as long as the index of the left-most is less than the index of the right-most index value
    ## then need to increment to the next index value, and decrement to
    while left < right:
        s_list[left], s_list[right] = s_list[right], s_list[left]
        left +=1
        right -=1
    return ''.join(s_list)

## time complexity of O(n) and a 
## space complexity of O(n) to store the list of characters

print(reverseString_2('hockey'))
