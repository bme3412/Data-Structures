## String matching algorithms are used to find occurrences of a pattern string within a larger text string. 
    ## The goal is to determine whether the pattern exists in the text and, if so, at what positions

## 1. Brute Force Algorithm:
    ## The brute force approach involves comparing each character of the pattern with each character of the text until a match is found or the end of the text is reached.

    ## It has a time complexity of O(m * n), where m is the length of the pattern and n is the length of the text.

    ## While simple to understand and implement, the brute force algorithm can be inefficient for large texts and patterns.

## 2. Knuth-Morris-Pratt (KMP) Algorithm:
    ## The KMP algorithm is an efficient string matching algorithm that improves upon the brute force approach.
    
    ## It utilizes the observation that when a mismatch occurs, the pattern itself contains sufficient information to determine the next position to start the matching process.
    
    ### The KMP algorithm preprocesses the pattern to compute a "failure function" or "prefix function" that indicates how much to shift the pattern when a mismatch occurs.

    ### The failure function helps avoid unnecessary comparisons and allows the algorithm to skip ahead to the next potential match position.

    ### The time complexity of the KMP algorithm is O(m + n), making it more efficient than the brute force approach.

def kmp_search(pattern, text):
    m = len(pattern)
    n = len(text)
    lps = [0] * m
    compute_lps(pattern, m, lps)
    i = j = 0
    while i < n:
        if pattern[j] == text[i]:
            i += 1
            j += 1
        if j == m:
            print("Pattern found at index", i - j)
            j = lps[j - 1]
        elif i < n and pattern[j] != text[i]:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1

def compute_lps(pattern, m, lps):
    len = 0
    lps[0] = 0
    i = 1
    while i < m:
        if pattern[i] == pattern[len]:
            len += 1
            lps[i] = len
            i += 1
        else:
            if len != 0:
                len = lps[len - 1]
            else:
                lps[i] = 0
                i += 1

# Example usage
text = "ABABDABACDABABCABAB"
pattern = "ABABCABAB"
kmp_search(pattern, text)

    
## The compute_lps function preprocesses the pattern to compute the failure function (lps) based on the longest proper prefix that is also a suffix. 

## The kmp_search function then uses the failure function to efficiently search for occurrences of the pattern in the text.

## The KMP algorithm avoids unnecessary comparisons by utilizing the failure function to skip ahead when a mismatch occurs. This makes it more efficient than the brute force approach, especially for large texts and patterns.