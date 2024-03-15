problem = """ Given two strings s and t, write a function to determine if t is an anagram of s"""

## need to be aware of case sensitivity
## need to count the occurencs of each string, and not the order
## dictionary data strucutre is most appropriate

## given 2 strings, s and t

def anagram(s, t):
    # convert to lower case
    s_lower = s.lower()
    t_lower = t.lower()

    # instantiate empty dicts to store each char of the string
    s_dict = {}
    t_dict = {}

    ## count the occurences of each item and store in each dict
    for char in s_lower:
        s_dict[char] = s_dict.get(char, 0) +1
        
    for char in t_lower:
        t_dict[char] = t_dict.get(char, 0) +1

    ## return conditional to check if dictionaries match ==

    return s_dict == t_dict

s = 'listen'
t = 'silent'
print(anagram(s,t))

s1= 'hockey'
t1 = 'football'
print(anagram(s1, t1))

def anagram_listcomp(s, t):
    # convert to lower case
    s_lower = s.lower()
    t_lower = t.lower()

    # instantiate empty dicts to store each char of the string
    s_dict = {}
    t_dict = {}

    ## use list comprehension to count
    s_dict = [s_lower.count(char) for char in s_lower]
    t_dict = [t_lower.count(char) for char in t_lower]

    return s_dict == t_dict
print(anagram_listcomp(s,t))
print(anagram_listcomp(s1, t1))


#### time complexity of O(n)
### space complexity of O(n) to store the character counts